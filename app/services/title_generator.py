import os

import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def suggest_titles(content: str):
    prompt = f"Suggest 3 creative and catchy blog post titles for the following content:\n\n{content}"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative blog writer."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60
    )
    
    titles = response['choices'][0]['message']['content'].strip().split("\n")
    return {"suggested_titles": titles}
