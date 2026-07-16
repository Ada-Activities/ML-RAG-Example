# ML-RAG-Example

A minimal Retrieval-Augmented Generation (RAG) example using Amazon Kendra for retrieval and Amazon Bedrock for generation. This repository demonstrates a small pipeline that queries a Kendra index, builds a system prompt with retrieved context, and asks a Bedrock model to generate an answer.

## Project structure

- `rag/` — package containing the core modules:
  - `rag/core.py` — main application logic (clients, retrieval, prompt building, generation)
  - `rag/config.py` — `Config` dataclass and environment loading
  - `rag/constants.py` — constants and prompt template
  - `rag/type_defs.py` — TypedDict definitions for AWS responses
- `main.py` — provides an entry point to run the example
- `requirements.txt` — Python dependencies
- `resources/` — example documents that will be indexed in Kendra

## Prerequisites

- `aws` CLI configured with appropriate credentials and permissions
- Python 3.10+
- An AWS account with access to Amazon Kendra and Amazon Bedrock
- Environment variables set: `KENDRA_INDEX_ID` and `BEDROCK_MODEL_ID`

Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Environment

Create a `.env` file or export the required variables in your shell:

```env
KENDRA_INDEX_ID=your-kendra-index-id
BEDROCK_MODEL_ID=us.amazon.nova-2-lite-v1:0
```

Nova 2 Lite is a good choice for this example, but you can select any Bedrock model that suits your needs. Refer to the Lab Walkthrough document for guidance on selecting a model.

## Running

Run the project from the repository root:

```bash
python main.py
```

Edit `main.py` to change the sample question or behavior.

## Notes

- This example expects to use the credentials and permissions of the AWS CLI profile configured on your machine. If the example fails to run due to permissions, try refreshing your AWS credentials with `aws login`.
- The code is intentionally minimal for learning and demonstration; adapt error handling, logging, and configuration to your needs.
- If concepts like `dataclass` or `TypedDict` are new, refer to the Python documentation for more details on these features.
- Information about setting up Kendra and selecting Bedrock models are provided in the Livecode Steps document.
