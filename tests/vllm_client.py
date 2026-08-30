from openai import OpenAI
 
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed-for-local-dev",
)
 
response = client.chat.completions.create(
    model="Qwen/Qwen2.5-0.5B-Instruct",
    messages=[
        {"role": "user", "content": "Write a concise checklist for vLLM deployment."}
    ],
    temperature=0.2,
    max_tokens=180,
)
 
print(response.choices[0].message.content)