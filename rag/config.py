import os
from dataclasses import dataclass

@dataclass
class Config:
    kendra_index_id: str
    bedrock_model_id: str

    @classmethod
    def from_env(cls) -> 'Config':
        """Load configuration from environment variables."""
        kendra_index_id = os.environ.get('KENDRA_INDEX_ID')
        if not kendra_index_id:
            raise ValueError("KENDRA_INDEX_ID environment variable is missing. Please set it in your environment or .env file.")

        model_id = os.environ.get('BEDROCK_MODEL_ID')
        if not model_id:
            raise ValueError("BEDROCK_MODEL_ID environment variable is missing. Please set it in your environment or .env file (e.g. us.amazon.nova-2-lite-v1:0).")

        return cls(kendra_index_id=kendra_index_id, bedrock_model_id=model_id)
