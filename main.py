import boto3
import json

KENDRA_INDEX_ID = '37a5086d-b7c2-410b-bfcb-b8d4e44b3e45'
MODEL_ID = 'us.amazon.nova-2-lite-v1:0'
KENDRA_SERVICE = 'kendra'
BEDROCK_SERVICE = 'bedrock-runtime'
CT_JSON = 'application/json'

kendra = boto3.client(KENDRA_SERVICE)
bedrock = boto3.client(BEDROCK_SERVICE)

def get_response_subset(response, max_length_per_result=300, max_results=5):
    if 'ResultItems' in response and response['ResultItems']:
        items = []
        processed = 0
        for item in response['ResultItems']:
            if processed >= max_results:
                break

            if 'DocumentExcerpt' in item and 'Text' in item['DocumentExcerpt']:
                items.append(item['DocumentExcerpt']['Text'][:max_length_per_result])
                processed += 1

        combined_text = " ".join(items)
        return combined_text
    
    return "No relevant policies found."

def retrieve_context(user_question):
    # Query Amazon Kendra for the relevant policy
    response = kendra.query(
        IndexId=KENDRA_INDEX_ID,
        QueryText=user_question
    )
    return get_response_subset(response)

def build_prompt(user_question, context):
    # Combine instructions, context, and the user's question
    prompt = f"""You are a helpful customer support assistant for a stationery store called Ada Stationery.
    Produce answers in plain text only. Markdown formatting is not supported.
    Answer the user's question using ONLY the provided context.
    Do not use any information that is not included in the context.
    If the context does not contain the answer, respond with "I don't know based on the information available to me."
    
    Context: {context}
    
    Question: {user_question}"""
    return prompt

def make_nova_payload(prompt, max_tokens=300):
    payload = {
        "messages": [
            {"role": "user", "content": [{"text": prompt}]}
        ],
        "inferenceConfig": {
            "maxTokens": max_tokens
        }
    }
    return json.dumps(payload)

def generate_answer(prompt):
    # Send the prompt to a Foundation Model via Amazon Bedrock
    payload = make_nova_payload(prompt)

    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(payload),
        contentType=CT_JSON
    )

    response_body = json.loads(response['body'].read())
    # return response_body['completion']
    content = response_body['output']['message']['content']
    
    return content[0]['text'] if content and 'text' in content[0] else "No answer generated."

# --- Test the Co-Pilot ---
# question = "Can I return a leather journal if I had my initials embossed on it?"
# question = "What paper types are best for ballpoint pens?"
question = "What paper types are best for glass quill pens?"
# question = "How much wood could a woodchuck chuck if a woodchuck could chuck wood?"
# question = "What paper could provide a pleasing mouth feel for a woodchuck to chew on while chucking wood?"
# question = "What can I make for dinner on a budget?"
retrieved_text = retrieve_context(question)
# print("Retrieved Context:", retrieved_text)
final_prompt = build_prompt(question, retrieved_text)
# print("Final Prompt:", final_prompt)

print(generate_answer(final_prompt))
