# 重磅：GPT-4 API全面开放使用

## 背景

相信很多申请GPT-4 API的开发者都收到OpenAI的邮件通知了，从2023.07.06开始，所有OpenAI的API付费用户都可以使用GPT-4了。

目前所有大语言模型的评测中，毫无疑问GPT-4是最亮眼的那颗星。

有了GPT-4的API，意味着开发者可以做出功能更强大、体验更好的应用。

此外，OpenAI官方表示要废弃Completions API，该API目前可以使用的一些Model也要在2024年1月4号下线。后续OpenAI的规划是让开发者都使用Chat Completions API。

另外，Embedding的部分模型以及Edits API也会在2024年1月4号下线。

## GPT-4 API全面开放

GPT-4是目前最强大的大语言模型，从3月份开放API以来，已经有数百万的开发者进行了申请，有非常多成功的[应用](https://openai.com/customer-stories)是基于GPT-4 API开发的。

从2023.07.06开始，只要有过API付费记录的开发者都可以使用GPT-4 8K上下文版本的API了。

新申请的开发者预计2023年7月底会审批通过，然后会基于已有的计算能力提升API的使用流控(rate limit)，让开发者可以更顺畅地使用GPT-4 API。

GPT-3.5 Turbo, DALL.E和Whisper API也都会全部开放出来给开发者使用。

预计2023年下半年，基于GPT-4和GPT-3.5 Turbo模型的微调(fine-tuning)也会开放出来。

## 废弃Completions API

OpenAI在2023年3月份引入了[Chat Completions API](https://platform.openai.com/docs/guides/gpt/chat-completions-api)，现在有大约97%的API使用量都来源于Chat Completions API。

Completions API是在2020年6月份引入的，当时是为了给开发者提供和OpenAI语言模型交互的能力。

现在有了Chat Completions API后，其实可以覆盖Completions API的功能，而且Chat Completions API更为强大，可以满足非常多的使用场景和对话需求。

下面简单介绍几种Chat Completions API的使用场景：



* 文本总结(Text summarization)

```bash
System
Summarize this message in max 10 words.

User
Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. It is named after the Roman god Jupiter. When viewed from Earth, Jupiter can be bright enough for its reflected light to cast visible shadows, and is on average the third-brightest natural object in the night sky after the Moon and Venus.

Assistant
Jupiter: Largest planet, visible to the naked eye at night.
```



* 代码补全(Code completion)

```bash
System
Complete the following code.


User
def fibonacci(num):


Assistant
if num == 0:
  return 0
elif num == 1:
  return 1
else:
  fib = [0, 1]
  for i in range(2, num + 1):
     fib.append(fib[i-1] + fib[i-2])
  return fib[num]
```



* 小样本学习(Few-shot learning)

```bash
System
You translate corporate jargon into plain English.


User
New synergies will help drive top-line growth.


Assistant
Working well together will make more money.


User
Let’s circle back when we have more bandwidth to touch base on opportunities for increased leverage.


Assistant
When we’re less busy, let’s talk about how to do better.


User
This late pivot means we don’t have time to boil the ocean for the client deliverable.


Assistant
Because of this sudden change, we don’t have enough time to complete the entire project for the client.

We plan to continue investing most of our platform efforts in this direction, as we believe it will offer an increasingly capable and easy-to-use experience for developers. We’re working on closing the last few remaining gaps of the Chat Completions API quickly, such as log probabilities for completion tokens and increased steerability to reduce the “chattiness” of responses.
```



## 废弃Completions API的旧模型

As part of our increased investment in the Chat Completions API and our efforts to optimize our compute capacity, in 6 months we will be retiring some of our older models using the Completions API. While this API will remain accessible, we will label it as “legacy” in our developer documentation starting today. We plan for future model and product improvements to focus on the Chat Completions API, and do not have plans to publicly release new models using the Completions API.

Starting January 4, 2024, [older completion models](https://platform.openai.com/docs/deprecations) will no longer be available, and will be replaced with the following models:

| **Older model**       | **New model**          |
| --------------------- | ---------------------- |
| ada                   | ada-002                |
| babbage               | babbage-002            |
| curie                 | curie-002              |
| davinci               | davinci-002            |
| davinci-instruct-beta | gpt-3.5-turbo-instruct |
| curie-instruct-beta   |                        |
| text-ada-001          |                        |
| text-babbage-001      |                        |
| text-curie-001        |                        |
| text-davinci-001      |                        |
| text-davinci-002      |                        |
| text-davinci-003      |                        |

Applications using the stable model names for base GPT-3 models (`ada`, `babbage`, `curie`, `davinci`) will automatically be upgraded to the new models listed above on January 4, 2024. The new models will also be accessible in the coming weeks for early testing by specifying the following model names in API calls: `ada-002`, `babbage-002`, `curie-002`, `davinci-002`.

Developers using other older completion models (such as `text-davinci-003`) will need to manually upgrade their integration by January 4, 2024 by specifying `gpt-3.5-turbo-instruct` in the “model” parameter of their API requests. `gpt-3.5-turbo-instruct` is an InstructGPT-style model, trained similarly to `text-davinci-003`. This new model is a drop-in replacement in the Completions API and will be available in the coming weeks for early testing.

Developers wishing to continue using their fine-tuned models beyond January 4, 2024 will need to fine-tune replacements atop the new base GPT-3 models (`ada-002`, `babbage-002`, `curie-002`, `davinci-002`), or newer models (`gpt-3.5-turbo`, `gpt-4`). Once this feature is available later this year, we will give priority access to GPT-3.5 Turbo and GPT-4 fine-tuning to users who previously fine-tuned older models. We acknowledge that migrating off of models that are fine-tuned on your own data is challenging. We will be providing support to users who previously fine-tuned models to make this transition as smooth as possible.

In the coming weeks, we will reach out to developers who have recently used these older models, and will provide more information once the new completion models are ready for early testing.

## 废弃Embedding旧模型

Users of older embeddings models (e.g., `text-search-davinci-doc-001`) will need to migrate to `text-embedding-ada-002` by January 4, 2024. We released `text-embedding-ada-002` in December 2022, and have found it more capable and cost effective than previous models. Today `text-embedding-ada-002` accounts for 99.9% of all embedding API usage.

We recognize this is a significant change for developers using those older models. Winding down these models is not a decision we are making lightly. We will cover the financial cost of users re-embedding content with these new models. We will be in touch with impacted users over the coming days.

| **Older model**               | **New model**          |
| ----------------------------- | ---------------------- |
| code-search-ada-code-001      | text-embedding-ada-002 |
| code-search-ada-text-001      |                        |
| code-search-babbage-code-001  |                        |
| code-search-babbage-text-001  |                        |
| text-search-ada-doc-001       |                        |
| text-search-ada-query-001     |                        |
| text-search-babbage-doc-001   |                        |
| text-search-babbage-query-001 |                        |
| text-search-curie-doc-001     |                        |
| text-search-curie-query-001   |                        |
| text-search-davinci-doc-001   |                        |
| text-search-davinci-query-001 |                        |
| text-similarity-ada-001       |                        |
| text-similarity-babbage-001   |                        |
| text-similarity-curie-001     |                        |
| text-similarity-davinci-001   |                        |

## 废弃Edits API

通过Edits API

Users of the Edits API and its associated models (e.g., `text-davinci-edit-001` or `code-davinci-edit-001`) will need to migrate to GPT-3.5 Turbo by January 4, 2024. 

The Edits API beta was an early exploratory API, meant to enable developers to return an edited version of the prompt based on instructions. 

We took the feedback from the Edits API into account when developing `gpt-3.5-turbo` and the Chat Completions API, which can now be used for the same purpose:

```bash
System
Apply the change requested by the user to the code.


User
def fibonacci(num):
  if num <= 1:
    return num
  else:
    return fibonacci(num-1) + fibonacci(num-2)
print(fibonacci(10))


User
Rename the function to fib.


Assistant
def fib(num):
  if num <= 1:
    return num
  else:
    return fib(num-1) + fib(num-2)
print(fib(10))
```



## 相关阅读

* 





## 总结

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，了解主流LLM相关知识。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://openai.com/blog/gpt-4-api-general-availability