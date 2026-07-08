from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

def ask_web_question(question, history=""):
    prompt = f"""
You are DocuMind AI.

Answer the user's question clearly and helpfully.

If the question needs latest/current information, say:
"Live web search is not enabled yet."

Chat history:
{history}

User question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content