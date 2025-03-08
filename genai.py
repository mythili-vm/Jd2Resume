import os
from openai import OpenAI

def get_ai_response(role,content):
    token = os.environ["GITHUB_TOKEN"]
    endpoint = "https://models.inference.ai.azure.com"
    model_name = "gpt-4o"

    client = OpenAI(
        base_url=endpoint,
        api_key=token,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": role,
            },
            {
                "role": "user",
                "content": content,
            }
        ],
        temperature=1.0,
        top_p=1.0,
        max_tokens=1000,
        model=model_name
    )
    return response.choices[0].message.content