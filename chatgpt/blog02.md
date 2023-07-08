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

OpenAI接下来会把重点放在Chat Completions API，不再投入精力支持Completions API。

从2023年1月4日开始，Completions API目前可以使用的一些模型会下线，开发者要继续使用Completions API，得使用新模型，参考如下表格：

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

同时，OpenAI也把Completions API在官网的API文档里标记为`legacy`，不推荐大家继续使用了。

所以还在用Completions API的赶紧去拥抱Chat Completions API吧。

* 如果开发者使用的是基于GPT-3模型的稳定模型版本，例如`ada`, `babbage`, `curie`, `davinci`，那代码可以不用修改，这些稳定版本的模型底层会在2024年1月4日后自动升级为上面表格里右侧的新模型。

  右侧的新模型在接下来几周开放测试，调用API的时候指定新Model的名字即可，例如 	`ada-002`, `babbage-002`, `curie-002`, `davinci-002`。

* 如果开发者使用的是其他旧模型名称，例如 `text-davinci-003`，那就需要在手工修改API里调用的模型名称为`gpt-3.5-turbo-instruct`，这个新模型也会在接下来几周开放测试。

## 废弃Embedding旧模型

从2024年1月4日开始，只能使用text-embedding-ada-002这个Embedding Model，其它Embedding Model都会下线，不能再使用。

text-embedding-ada-002是2022年12月上线的，比其它Embedding Model更强大而且成本更低。现在99%的embedding API调用都在使用这个模型。

这对使用旧模型来做embedding的开发者来说是一个痛苦的事情，因为不同模型embedding的结果是不一样的，开发者需要在旧模型下线前提前做好适配和测试。

OpenAI官方承诺会补偿旧模型的用户。

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

目前Edits API可以使用`text-davinci-edit-001` 和`code-davinci-edit-001`这2个模型。

从2024年1月4日开始，Edits API不能使用这2个模型，要继续使用Edits API，得使用GPT-3.5 Turbo模型。

但是官方不再建议大家使用Edits API了，这个API也会废弃。

我们建议直接使用Chat Completions API来替代Edits API，如下例所示：

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

* [手把手教会你如何通过ChatGPT API实现上下文对话](https://mp.weixin.qq.com/s?__biz=Mzg2MTcwNjc1Mg==&mid=2247484749&idx=1&sn=ed175291674fb402fc50c588b82d25ee&chksm=ce124a22f965c334a43272ad05ea4981c055bb2d66a23fffab64fd449eea2dc6eeebc9679780#rd)
* [ChatGPT API重大升级-必知必会](https://mp.weixin.qq.com/s?__biz=Mzg2MTcwNjc1Mg==&mid=2247484810&idx=1&sn=9583a27435c000865544991e0c4801c7&chksm=ce124ae5f965c3f322a847fcc5e89afe819f617d4ea77f1d54434d89cbf43f47e20139674dd1#rd)
* [ChatGPT必会知识点](https://mp.weixin.qq.com/s?__biz=Mzg2MTcwNjc1Mg==&mid=2247484790&idx=1&sn=643b8cb0d003e8fc0914c9f713b187de&chksm=ce124a19f965c30f5f04f0c1a6f4aeac549e28184361c5dc77a00d4b149177fa8d8765c3e691#rd)
* [baichuan-7B: 开源可商用支持中英文的最好大模型](https://mp.weixin.qq.com/s?__biz=Mzg2MTcwNjc1Mg==&mid=2247484799&idx=1&sn=b485d2cdff0e536436b19697c9d759bb&chksm=ce124a10f965c3061afd5d2919bc34665ee89b0d8abbabb88b434fc3a33282ca260f0d11ed86#rd)
* [轩辕：首个千亿级中文金融对话模型](https://mp.weixin.qq.com/s?__biz=Mzg2MTcwNjc1Mg==&mid=2247484779&idx=1&sn=d983839154a79a9f0d21e327b5e9a557&chksm=ce124a04f965c3128b3a000182fe4e30c805540dd7bd8340602d749069744556658752c17f5a#rd)
* [逼近GPT-4！BLOOMChat: 开源可商用支持多语言的大语言模型](https://mp.weixin.qq.com/s?__biz=Mzg2MTcwNjc1Mg==&mid=2247484766&idx=1&sn=ccecd302b889a73b46c8d804f713bc25&chksm=ce124a31f965c32749d27391ecbfd185ae48f9a1e30aeed5d5fc2b0de97b3f06e9116d85e61b#rd)
* [一文汇总开源大语言模型，人人都可以拥有自己的ChatGPT](https://mp.weixin.qq.com/s?__biz=Mzg2MTcwNjc1Mg==&mid=2247484753&idx=1&sn=39448f762b4a0bc108272de5e3036619&chksm=ce124a3ef965c328ba7e160b85bb8b8fbfaefd90e007738e97b5beec75003982b88859478438#rd)



## 总结

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，了解主流LLM相关知识。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://openai.com/blog/gpt-4-api-general-availability