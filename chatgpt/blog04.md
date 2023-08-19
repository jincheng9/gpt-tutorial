# ChatGPT最佳实践系列-第2篇

## 背景

OpenAI官方详细介绍了ChatGPT使用的最佳实践，不仅适用于使用ChatGPT网站进行直接对话的用户，还适用于通过OpenAI API接入的开发者。

掌握了这些最佳实践，就能更好地利用GPT大模型。

本文是ChatGPT使用最佳实践系列第2篇 - 提供参考信息(provide reference text)。

GPT可能会自信地编造虚假的答案，尤其是在被询问深奥的话题或者要求提供引用内容或者URLs时。

就像做笔记可以帮助学生在考试中得到更好的成绩一样，为GPT提供参考信息也可以帮助大模型生成更准确的回答，减少捏造的答案。

## 策略1：引导模型根据已知信息来回答问题

用户提问时，如果我们可以把和问题相关的已知事实或者信息给到大模型，就可以引导模型根据我们提供的已知信息来回答问题，减少大模型捏造答案的可能性。

以下是构造Prompt的示例：

| SYSTEM | Use the provided articles delimited by triple quotes to answer questions. If the answer cannot be found in the articles, write "I could not find an answer." |
| ------ | ------------------------------------------------------------ |
| USER   | \<insert articles, each delimited by triple quotes\><br> Question:\<insert question here\> |

不过需要注意的是，由于GPT模型有上下文长度(context length)的限制，我们需要精准找到和问题相关的信息。

向量化(embedding)就可以用来实现高效的信息检索。

可以参考["Use embeddings-based search to implement efficient knowledge retrieval"](https://platform.openai.com/docs/guides/gpt-best-practices/tactic-use-embeddings-based-search-to-implement-efficient-knowledge-retrieval) 了解更多细节。



## 策略2：引导模型在回答里带上引用内容

如果Prompt里提供了和问题相关的参考文档，那就可以要求大模型在回答里引用Prompt里提供的文档中的相关内容。

以下是构造Prompt的示例：

| **SYSTEM** | You will be provided with a document delimited by triple quotes and a question. Your task is to answer the question using only the provided document and to cite the passage(s) of the document used to answer the question. If the document does not contain the information needed to answer this question then simply write: "Insufficient information." If an answer to the question is provided, it must be annotated with a citation. Use the following format for to cite relevant passages ({"citation": …}). |
| ---------- | ------------------------------------------------------------ |
| **USER**   | """\<insert document here\>""" <br>Question: \<insert question here\> |

注意：回答里的引用内容准确性是可以和Prompt里提供的内容做字符串匹配来验证的。

可以在这个链接里看效果：[Open in Playground](https://platform.openai.com/playground/p/default-answer-with-citation)。



## 总结

本文是ChatGPT使用最佳实践系列第2篇 - 提供参考信息(provide reference text)。

详细讲述了2个策略，以上策略不仅适用于GPT模型，还适用于其它大语言模型。

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，可以看到所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://platform.openai.com/docs/guides/gpt-best-practices