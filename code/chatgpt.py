import os
import time
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

print(openai.Model.retrieve("gpt-3.5-turbo"))

start_time = time.time()
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "为什么喜欢狗"}
  ],
)
end_time = time.time()
print("time cost:", end_time-start_time)
print(completion.choices[0].message.content)
print(completion.usage.total_tokens)