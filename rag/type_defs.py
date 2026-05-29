from typing import TypedDict

# Amazon Kendra response structures
class KendraDocumentExcerpt(TypedDict):
    Text: str

class KendraResultItem(TypedDict):
    DocumentExcerpt: KendraDocumentExcerpt

class KendraQueryResponse(TypedDict):
    ResultItems: list[KendraResultItem]

# Bedrock Converse response structures
class BedrockMessageContent(TypedDict):
    text: str

class BedrockMessage(TypedDict):
    content: list[BedrockMessageContent]

class BedrockOutput(TypedDict):
    message: BedrockMessage

class BedrockConverseResponse(TypedDict):
    output: BedrockOutput
