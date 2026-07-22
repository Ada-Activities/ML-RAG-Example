from dotenv import load_dotenv
from rag.core import (
    build_system_instructions,
    Config,
    generate_answer,
    initialize_bedrock_client,
    initialize_kendra_client,
    retrieve_context,
)

def main() -> None:
    # Load environment variables from .env file if present
    load_dotenv()

    # Load and validate settings structure
    config = Config.from_env()

    # Initialize AWS clients
    kendra_client = initialize_kendra_client()
    bedrock_client = initialize_bedrock_client()

    # Bank of sample questions
    answer = "Follow the livecode directions to explore this code."
    question = "Can I return a leather journal if I had my initials embossed on it?"
    # question = "What paper types are best for ballpoint pens?"
    # question = "What paper types are best for glass quill pens?"
    # question = "How much wood could a woodchuck chuck if a woodchuck could chuck wood?"
    # question = "What paper could provide a pleasing mouth feel for a woodchuck to chew on while chucking wood?"
    # question = "What can I make for dinner on a budget?"

    # Retrieve relevant context from Kendra index
    # retrieved_text = retrieve_context(kendra_client, config, question)

    # Build the system prompt to include with the request to Bedrock
    # system_instructions = build_system_instructions(retrieved_text)

    # Get Bedrock to answer the question, providing the relevant context
    # answer = generate_answer(bedrock_client, config, system_instructions, question)

    # Print the answer
    print(answer)

if __name__ == "__main__":
    main()
