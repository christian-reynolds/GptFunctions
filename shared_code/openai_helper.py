import openai
import os

def get_openai_response(prompt, model="gpt-4"):
    openai.api_key = os.environ["OpenAIApiKey"]
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']