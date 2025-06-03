import os

import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_titles(content: str):
    prompt = (
        "Generate three creative and relevant blog post titles for the following content:\n\n"
        f"{content}\n\nTitles:\n"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can use "gpt-4" if allowed
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=60,
        n=1
    )

    text = response["choices"][0]["message"]["content"]
    return [title.strip("- ").strip() for title in text.strip().split("\n") if title.strip()]
