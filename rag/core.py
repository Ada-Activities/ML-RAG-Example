import boto3  # type: ignore
from botocore.client import BaseClient  # type: ignore
from botocore.exceptions import BotoCoreError, ClientError  # type: ignore
from .config import Config
from .type_defs import KendraQueryResponse, BedrockConverseResponse
from .constants import (
    KENDRA_SERVICE,
    BEDROCK_SERVICE,
    KEY_RESULT_ITEMS,
    KEY_DOC_EXCERPT,
    KEY_TEXT_UPPER,
    DEFAULT_NO_POLICIES,
    DEFAULT_NO_ANSWER,
    KEY_ROLE,
    KEY_USER,
    KEY_CONTENT,
    KEY_TEXT,
    KEY_MAX_TOKENS,
    KEY_OUTPUT,
    KEY_MESSAGE,
    PROMPT_TEMPLATE,
)

def initialize_kendra_client() -> BaseClient:
    """Initialize the Amazon Kendra client."""
    return boto3.client(KENDRA_SERVICE)

def initialize_bedrock_client() -> BaseClient:
    """Initialize the Amazon Bedrock client."""
    return boto3.client(BEDROCK_SERVICE)

def get_kendra_response_subset(response: KendraQueryResponse, max_length_per_result: int = 300, max_results: int = 5) -> str:
    items = []
    for item in response[KEY_RESULT_ITEMS][:max_results]:
        text = item[KEY_DOC_EXCERPT][KEY_TEXT_UPPER]
        if text:
            items.append(text[:max_length_per_result])

    return " ".join(items) if items else DEFAULT_NO_POLICIES

def retrieve_context(kendra_client: BaseClient, config: Config, user_question: str) -> str:
    # Query Amazon Kendra for the relevant policy
    try:
        response = kendra_client.query(
            IndexId=config.kendra_index_id,
            QueryText=user_question
        )
        return get_kendra_response_subset(response)
    except (BotoCoreError, ClientError) as e:
        print(f"Error querying Amazon Kendra: {e}")
        return DEFAULT_NO_POLICIES

def build_system_instructions(context: str) -> str:
    # Combine instructions, context, and the user's question
    return PROMPT_TEMPLATE.format(context=context)

def get_bedrock_response_text(response: BedrockConverseResponse) -> str:
    content_list = response[KEY_OUTPUT][KEY_MESSAGE][KEY_CONTENT]
    
    for content in content_list:
        if KEY_TEXT in content:
            return content[KEY_TEXT]

    return DEFAULT_NO_ANSWER

def generate_answer(bedrock_client: BaseClient, config: Config, system_instructions: str, question: str) -> str:
    # Send the prompt to a Foundation Model via Amazon Bedrock Converse API
    try:
        response = bedrock_client.converse(
            modelId=config.bedrock_model_id,
            messages=[
                {
                    KEY_ROLE: KEY_USER,
                    KEY_CONTENT: [{KEY_TEXT: question}]
                }
            ],
            system=[{KEY_TEXT: system_instructions}],
            inferenceConfig={
                KEY_MAX_TOKENS: 300
            }
        )

        return get_bedrock_response_text(response)

    except (BotoCoreError, ClientError) as e:
        print(f"Error generating answer with Amazon Bedrock: {e}")
        return DEFAULT_NO_ANSWER

