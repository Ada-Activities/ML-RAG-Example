from typing import Literal

# AWS Service Names
KENDRA_SERVICE = 'kendra'
BEDROCK_SERVICE = 'bedrock-runtime'

# Amazon Kendra Response Key Names
KEY_RESULT_ITEMS: Literal['ResultItems'] = 'ResultItems'
KEY_DOC_EXCERPT: Literal['DocumentExcerpt'] = 'DocumentExcerpt'
KEY_TEXT_UPPER: Literal['Text'] = 'Text'

# Fallback Responses
DEFAULT_NO_POLICIES = "No relevant policies found."
DEFAULT_NO_ANSWER = "No answer generated."

# Bedrock Converse API Key Names
KEY_ROLE: Literal['role'] = 'role'
KEY_USER: Literal['user'] = 'user'
KEY_CONTENT: Literal['content'] = 'content'
KEY_TEXT: Literal['text'] = 'text'
KEY_MAX_TOKENS: Literal['maxTokens'] = 'maxTokens'
KEY_OUTPUT: Literal['output'] = 'output'
KEY_MESSAGE: Literal['message'] = 'message'

# RAG System Instructions Prompt Template
PROMPT_TEMPLATE = """You are a helpful customer support assistant for a stationery store called Ada Stationery.
You only answer questions related to Ada Stationery's products, policies, and services. Politely decline questions outside this scope.
Produce answers in plain text only.
Markdown formatting is not supported.
Keep responses concise and professional. Avoid unnecessary elaboration.
Answer the user's question using ONLY the provided context.
Do not use any information that is not included in the context.
Do not infer, extrapolate, or combine context with outside knowledge.
If the context does not contain the answer, respond with "I don't know based on the information available to me."
If the context only partially answers the question, provide what you can and indicate that your information may be incomplete.
In your response, never explicitly mention the "context". Instead, refer to the information as "based on what I have available" rather than attributing it to specific sources.

--- BEGIN CONTEXT ---
{context}
--- END CONTEXT ---
"""
