import os
from groq import Groq

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def ask_web_question(question, history=""):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are DocuMind AI. Answer clearly and helpfully."
            },
            {
                "role": "user",
                "content": f"Chat history:\n{history}\n\nQuestion:\n{question}"
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content