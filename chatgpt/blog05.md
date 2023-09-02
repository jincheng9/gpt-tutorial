# ChatGPT最佳实践系列-第3篇

## 背景

OpenAI官方详细介绍了ChatGPT使用的最佳实践，不仅适用于使用ChatGPT网站进行直接对话的用户，还适用于通过OpenAI API接入的开发者。

掌握了这些最佳实践，就能更好地利用GPT大模型。

本文是ChatGPT使用最佳实践系列第3篇 - 将复杂任务拆分成更简单的子任务。

软件开发过程中，我们通常会把一个复杂的系统拆分成多个功能模块，这样整个系统更好理解，更容易维护。

这个原理同样适用于GPT大模型，因为复杂任务比简单任务有更高的错误率。如果把一个复杂的任务拆分成多个更为简单的子任务，大模型回答效果通常会更好。



## 策略1：对用户提问做分类

举个例子，如果你要做一个智能客服，用户的提问可能是非常多样的，有可能问产品信息，有有可能问技术问题，也有可能问账号信息等等。

为了能够精确回答客户的提问，我们可以先让大模型对用户的提问做分类，判断用户是在提问哪方面的问题。然后再根据用户提问的分类来给大模型输入对应的instruction指令，这样回答效果会更好。

参考如下示例：用户买了一个路由器，但是上不了网，于是用户做了如下提问

| system | You will be provided with customer service queries. Classify each query into a primary category and a secondary category. Provide your output in json format with the keys: primary and secondary.<br/><br/>Primary categories: Billing, Technical Support, Account Management, or General Inquiry.<br/><br/>Billing secondary categories:<br/>- Unsubscribe or upgrade<br/>- Add a payment method<br/>- Explanation for charge<br/>- Dispute a charge<br/><br/>Technical Support secondary categories:<br/>- Troubleshooting<br/>- Device compatibility<br/>- Software updates<br/><br/>Account Management secondary categories:<br/>- Password reset<br/>- Update personal information<br/>- Close account<br/>- Account security<br/><br/>General Inquiry secondary categories:<br/>- Product information<br/>- Pricing<br/>- Feedback<br/>- Speak to a human |
| ------ | ------------------------------------------------------------ |
| user   | I need to get my internet working again.                     |

我们可以通过system消息来让大模型先判断用户问题的分类，有了问题分类后，我们就可以把对应问题分类的instruction指令通过system消息告诉大模型，大模型再做回答。



| system | You will be provided with customer service inquiries that require troubleshooting for technical support. Help the user by:<br/><br/>- Ask them to check that all cables to/from the router are connected. Note that it is common for cables to come loose over time.<br/>- If all cables are connected and the issue persists, ask them which router model they are using<br/>- Now you will advise them how to restart their device: <br/>-- If the model number is MTD-327J, advise them to push the red button and hold it for 5 seconds, then wait 5 minutes before testing the connection.<br/>-- If the model number is MTD-327S, advise them to unplug and replug it, then wait 5 minutes before testing the connection.<br/>- If the customer's issue persists after restarting the device and waiting 5 minutes, connect them to IT support by outputting {"IT support requested"}.<br/>- If the user starts asking questions that are unrelated to this topic then confirm if they would like to end the current chat about troubleshooting and classify their request according to the following scheme:<br/><br/>Classify their query into a primary category and a secondary category. Provide your output in json format with the keys: primary and secondary.<br/><br/>Primary categories: Billing, Technical Support, Account Management, or General Inquiry.<br/><br/>Billing secondary categories:<br/>- Unsubscribe or upgrade<br/>- Add a payment method<br/>- Explanation for charge<br/>- Dispute a charge<br/><br/>Technical Support secondary categories:<br/>- Troubleshooting<br/>- Device compatibility<br/>- Software updates<br/><br/>Account Management secondary categories:<br/>- Password reset<br/>- Update personal information<br/>- Close account<br/>- Account security<br/><br/>General Inquiry secondary categories:<br/>- Product information<br/>- Pricing<br/>- Feedback<br/>- Speak to a human |
| ------ | ------------------------------------------------------------ |
| user   | I need to get my internet working again.                     |

* 只要大模型输出的结果是分类结果，我们就根据分类结果来重新构造system消息，重新向大模型提问。
* 如果大模型输出的结果不是问题分类结果，那我们就不用改变system消息，直接把大模型的结果返回给用户即可。

以上技术手段其实构造了一个状态机来回答用户的问题，非常适合于智能客服的场景。

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-decomposition-by-intent-classification-2)。



## 策略2：总结或者过滤长对话内容

GPT大模型有上下文长度的限制，比如GPT-4最多只支持32k上下文长度，具体每个模型的上下文长度限制参考[context length](https://platform.openai.com/docs/models/gpt-4)。

如果对话的轮次过多，或者对话内容过长(比如你让大模型帮你写论文等)，那把所有对话记录都发送给GPT就会超过GPT大模型的context length。

如何解决这个问题呢？有2个推荐的解决方案：

* 第一种，设定一个token阈值，如果你发现对话记录的长度要超过这个阈值了，就可以把之前的部分对话记录让大模型做一个汇总，然后把汇总内容作为system消息给到大模型，这样就可以解决发送所有对话记录给大模型导致超过大模型上下文长度限制的问题。或者开发者的后台程序可以异步的对对话记录做定期汇总。
* 第二种，根据用户的提问，从对话记录里筛选出最相关的对话记录，减少要发送的token数量。可以通过向量化检索的方式来实现筛选逻辑，具体可以参考 ["Use embeddings-based search to implement efficient knowledge retrieval"](https://platform.openai.com/docs/guides/gpt-best-practices/tactic-use-embeddings-based-search-to-implement-efficient-knowledge-retrieval)。

## 策略3：递归汇总长文档

假设我们要对长文档(比如一本书)做汇总，由于大模型有上下文长度限制(假设为L)，在单次的请求里，假设大模型汇总后的结果completion的长度为A，那发给大模型的prompt的长度不能超过L-N。

completion结果的长度A我们是可以在API层面指定max_token参数来限制的，那怎么能控制prompt的长度呢？

我们可以对长文档的每一个章节分别做summary，然后对多个章节的summary继续递归summary，直到整篇长文档被summary。

要详细了解如何对长文档做summary可以参考OpenAI之前基于GPT-3变种的研究工作[research](https://openai.com/research/summarizing-books)。



## 总结

本文是ChatGPT使用最佳实践系列第3篇 - 将复杂任务拆分成更简单的子任务。

详细讲述了3个策略，以上策略不仅适用于GPT模型，还适用于其它大语言模型。

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，可以看到所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://platform.openai.com/docs/guides/gpt-best-practices