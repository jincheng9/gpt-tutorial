# ChatGPT API帮助手册

本API帮助手册针对的是ChatGPT。

官方API只有Python和Node.js版本。

https://platform.openai.com/docs/guides/chat

API Reference: https://platform.openai.com/docs/api-reference/chat

其它编程语言的API由社区维护，可以参考如下链接：

社区API：https://platform.openai.com/docs/libraries/community-libraries

## Model限制

Chat API只支持特定的Model

https://platform.openai.com/docs/models/model-endpoint-compatibility

在调用Chat API的时候，model参数的值要遵循上面链接里的说明。

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

## stream参数

如果在ChatGPT官网和ChatGPT对话，你会发现ChatGPT的回答不是一次性全部给出，是分段给出的。

这是因为后台返回的completion就是分段给出的，模型计算出一部分结果就返回一部分。

通过API同样可以达到这个效果，需要用到stream参数。

stream: boolean, Optional, Defaults to false

如果stream参数设置为False，那ChatGPT会计算出全部结果后一次性返回，可能请求的耗时会比较长，影响用户体验。

如果stream参数设置为True，那就会返回增量结果，最后会返回一个标记，表示响应已经结束。

使用stream参数返回增量结果的Python代码样例：https://github.com/openai/openai-cookbook/blob/main/examples/How_to_stream_completions.ipynb

## token限制

单次请求的prompt和返回的completion的token加起来不能超过模型的context length。

每个model支持的最大token数量参考：https://platform.openai.com/docs/models

## rate limit

RPM: requests per minute

TPM: tokens per minute

参考：https://platform.openai.com/docs/guides/rate-limits/overview

## 注意事项

* 目前ChatGPT的API没有记忆上下文的功能。
  * 如果要实现多轮对话的上下文关联，需要开发者记录下ChatGPT返回的completion结果，然后每次发送prompt的时候，把之前所有的prompt和completion一起发送给ChatGPT。否则ChatGPT只能实现单轮对话(single-turn conversation)。
  * 这种实现上下文关联的多轮对话的方案带来的问题就是后面发送prompt请求时，携带的token数量会越来越多。


## References

* https://platform.openai.com/docs/api-reference
* https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28