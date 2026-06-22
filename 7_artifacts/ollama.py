# Connects to Ollama and runs a simple query 
from openai import OpenAI

openai = OpenAI(
    base_url="http://10.1.90.100:11434/v1",
    api_key="ollama"
)

question = "What is 2+2?"
messages = [{"role": "user", "content": question}]

response = openai.chat.completions.create(
    model="llama3.2:1b",
    messages=messages
)

print(response.choices[0].message.content)