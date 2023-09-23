# ChatGPT最佳实践系列第5篇-使用外部工具

## 背景

OpenAI官方详细介绍了ChatGPT使用的最佳实践，不仅适用于使用ChatGPT网站进行直接对话的用户，还适用于通过OpenAI API接入的开发者。

掌握了这些最佳实践，就能更好地利用GPT大模型。

本文是ChatGPT使用最佳实践系列第5篇 - 使用外部工具。



## 策略1：使用向量搜索来实现高效知识检索

用户提问的时候，如果能拿到和问题有关的信息，是有助于大模型提升回答效果的。

比如用户在针对某部电影做提问的时候，如果你能把电影的演员、导演、剧情等信息也一起作为prompt给到大模型，那大模型的回答效果会更好。

而且这一招也能解决时效性的问题，因为可以针对用户的提问实时检索最新信息，然后一起作为prompt喂给大模型。

比如Google的Bard和Baichuan就引入了搜索增强来解决时效性问题。

要实现上面说的高效检索，就可以用到向量检索的技术。

向量检索是把输入的文本转化成一个vector向量，然后基于向量之间的相似度衡量就可以找到相似的文本数据。

现在基于大模型做知识库助手，就是使用向量检索到方案来实现的。

具体用例可以参考：[OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/vector_databases/Using_vector_databases_for_embeddings_search.ipynb)。

## 策略2：让大模型写代码来实现精确计算

让GPT直接做精确的数值计算或者逻辑很复杂的计算是不靠谱的。

但是，我们可以让GPT编写计算代码，然后我们自己本地运行GPT生成的代码来实现精确的计算。

比如下面的例子，你可以让通过system消息让大模型编写代码，把代码按照你预期的格式输出。然后你可以针对这个格式来解析大模型的输出代码，最后在你的运行环境执行代码，拿到计算结果。

| System    | You can write and execute Python code by enclosing it in triple backticks, e.g. <br>\```code goes here\```.<br> Use this to perform calculations. |
| --------- | ------------------------------------------------------------ |
| user      | Find all real-valued roots of the following polynomial: 3\*x\*\*5 - 5\*x\*\*4 - 3\*x\*\*3 - 7*x - 10. |
| assistant | To find the roots of the polynomial, we can use the `numpy.roots` function in Python. This function computes the roots of a polynomial with coefficients given in a list. The list represents the coefficients of the polynomial from highest degree to lowest.<br/><br/>Here is the Python code to find the roots of the polynomial:<br/><br/>\```python<br/>import numpy as np<br/><br/># Coefficients of the polynomial<br/>coeff = [3, -5, -3, 0, -7, -10]<br/><br/># Compute the roots<br/>roots = np.roots(coeff)<br/><br/># Print only real roots<br/>real_roots = [root for root in roots if np.isreal(root)]<br/>print(real_roots)<br/>```<br/>Please note that the roots may not be exact due to numerical precision issues. Also, the roots are not guaranteed to be real; they could be complex numbers. The code above filters out only the real roots. |
| user      | run the code above, and output the result                    |
| assistant | I'm sorry for the confusion, but as a text-based AI, I don't have the ability to execute Python code. However, you can run the code provided in your local Python environment or any online Python compiler to get the real-valued roots of the polynomial. |

大模型是无法直接运行代码的，需要在你本地环境运行。

可以在这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-code-execution)。

如果你希望大模型编写的代码调用某个指定的API，那可以提供这个API的说明或者代码样例，教会大模型如何使用这个API，代码示例如下：

| system    | You can write and execute Python code by enclosing it in triple backticks. Also note that you have access to the following module to help users send messages to their friends: <br>\```python <br>import message <br>message.write(to="John", message="Hey, want to meetup after work?")<br>``` |
| --------- | ------------------------------------------------------------ |
| user      | Let Alice know I'll meet her at the coffee shop at 10.       |
| assistant | Sure, I can help you with that. Here is the Python code to send the message to Alice.<br/><br/>\```python<br/>import message<br/>message.write(to="Alice", message="I'll meet you at the coffee shop at 10.")<br/>``` |

可以在这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-code-api)。

注意：在你本地环境执行大模型生成的代码要小心，不要想当然认为大模型生成的代码就是安全可靠的。最好在一个沙箱环境里运行大模型生成的代码，避免引入安全漏洞。

## 策略3：使用大模型的函数调用功能

Chat completions这个API允许在请求里传入函数定义，大模型可以根据用户提问来判断是否需要调用你传入的函数以及生成对应函数的实参，并且返回给用户，这个功能其实就是function call。

function call非常实用，可以针对准确性要求比较高的场景生成尽可能精确的回答。

比如，你问大模型今天深圳的气温是多少，GPT肯定是无法知晓的，因为它的训练数据只截止到2021年9月。

针对这种场景，你可以写一个function，参数是日期和城市，输出结果是气温。

你把这个function的定义传给作为参数传给GPT，GPT会根据你的提问来判断是否需要调用到你提供的function。

如果GPT认为需要调用到你的function才能回答提问的话，会把这个function的实参返回给你，并且告诉你具体要调用哪个的function。

更多细节可以参考我之前写的文章：[GPT函数调用教程](https://mp.weixin.qq.com/s?__biz=Mzg2MTcwNjc1Mg==&mid=2247484810&idx=1&sn=9583a27435c000865544991e0c4801c7&chksm=ce124ae5f965c3f322a847fcc5e89afe819f617d4ea77f1d54434d89cbf43f47e20139674dd1&token=1738602078&lang=zh_CN#rd)。

## 总结

本文是ChatGPT使用最佳实践系列第5篇 - 使用外部工具。

详细讲述了3个策略，以上策略不仅适用于GPT模型，还适用于其它大语言模型。

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，可以看到所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://platform.openai.com/docs/guides/gpt-best-practices