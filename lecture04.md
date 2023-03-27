# ChatGPT API帮助手册

本API帮助手册针对的是ChatGPT。

https://platform.openai.com/docs/guides/chat

https://platform.openai.com/docs/api-reference/chat

## token限制

单次请求的prompt和返回的completion的token加起来不能超过模型的context length。

每个model支持的最大token数量参考：https://platform.openai.com/docs/models

## rate limit

RPM: requests per minute

TPM: tokens per minute

参考：https://platform.openai.com/docs/guides/rate-limits/overview

## role

ChatGPT发送的messages参数里需要指定每个message的role。

```python
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

role: system，message里role为system，是为了让ChatGPT在对话过程中设定自己的行为，目前role为system的消息没有太大的实际作用，官方说法如下：

> [gpt-3.5-turbo-0301](https://platform.openai.com/docs/models) does not always pay strong attention to system messages. Future models will be trained to pay stronger attention to system messages.

role: user，表示提交prompt的一方。

role: assistant，表示给出completion响应的一方，实际上就是ChatGPT本身。

## 注意事项

* 目前ChatGPT的API没有记忆上下文的功能。
  * 如果要实现多轮对话的上下文关联，需要开发者记录下ChatGPT返回的completion结果，然后每次发送prompt的时候，把之前所有的prompt和completion一起发送给ChatGPT。否则ChatGPT只能实现单轮对话(single-turn conversation)。
  * 这种实现上下文关联的多轮对话的方案带来的问题就是后面发送prompt请求时，携带的token数量会越来越多。


## References

* https://platform.openai.com/docs/api-reference
* https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28