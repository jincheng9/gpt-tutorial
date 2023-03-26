import os
import time
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = []
while True:
    content = input("User: ")
    messages.append({"role": "user", "content": content})
    
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion
    answer = chat_response.choices[0].message.content
    total_tokens = chat_response.usage.total_tokens
    print(f'ChatGPT: {answer}')
    print(f'token number: {total_tokens}')
    print(chat_response)
    messages.append({"role": "assistant", "content": answer})