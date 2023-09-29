# ChatGPT最佳实践系列第6篇-系统化测试

## 背景

OpenAI官方详细介绍了ChatGPT使用的最佳实践，不仅适用于使用ChatGPT网站进行直接对话的用户，还适用于通过OpenAI API接入的开发者。

掌握了这些最佳实践，就能更好地利用GPT大模型。

本文是ChatGPT使用最佳实践系列第6篇 - 系统化测试。

大模型评测是大模型技术体系里很重要的一环。大模型本身经常做变更，那如何评价大模型变更前后的效果呢？

有人工评测的，也有靠模型去评测的。基于模型的评测(model-based evals)对于内容特别长的回答是有帮助的，因为这类回答靠人工是比较难评价孰好孰差的。

那什么时候需要人工评测，什么时候需要基于模型的评测呢？这个界限其实比较模糊，不好界定，需要在具体实践过程中去摸索。

[OpenAI Evals](https://github.com/openai/evals) 是一个开源的软件框架，提供了一系列工具，可以用来对大模型做自动化评测。



## 策略：对比模型输出结果和标准答案

### 场景1：假设明确知道问题的正确答案应该包含的既定事实

对于这个场景，我们可以向大模型提问，让大模型告诉我们这个回答包含了多少个事实。

我们可以给大模型设定如下的system message：

| system | You will be provided with text delimited by triple quotes that is supposed to be the answer to a question. Check if the following pieces of information are directly contained in the answer: <br><br/>- Neil Armstrong was the first person to walk on the moon. <br/>- The date Neil Armstrong first walked on the moon was July 21, 1969.<br/> For each of these points perform the following steps:<br/><br/> 1 - Restate the point. <br/>2 - Provide a citation from the answer which is closest to this point. <br/>3 - Consider if someone reading the citation who doesn't know the topic could directly infer the point. Explain why or why not before making up your mind. <br/>4 - Write "yes" if the answer to 3 was yes, otherwise write "no". <br/><br/>Finally, provide a count of how many "yes" answers there are. Provide this count as {"count": \<insert count here\>}. |
| ------ | ------------------------------------------------------------ |

以下user输入的回答包含了以上system message里指定的2个事实：

| system    | \<insert system message above\>                              |
| --------- | ------------------------------------------------------------ |
| user      | """Neil Armstrong is famous for being the first human to set foot on the Moon. This historic event took place on July 21, 1969, during the Apollo 11 mission.""" |
| assistant | 1 - Neil Armstrong was the first person to walk on the moon.<br/>2 - "Neil Armstrong is famous for being the first human to set foot on the Moon."<br/>3 - Yes, someone reading the citation could directly infer that Neil Armstrong was the first person to walk on the moon because it explicitly states that he was the first human to set foot on the Moon.<br/>4 - Yes<br/><br/>1 - The date Neil Armstrong first walked on the moon was July 21, 1969.<br/>2 - "This historic event took place on July 21, 1969, during the Apollo 11 mission."<br/>3 - Yes, someone reading the citation could directly infer that Neil Armstrong first walked on the moon on July 21, 1969 because it explicitly states the date of the event.<br/>4 - Yes<br/><br/>{"count": 2} |

可以通过这个链接进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-1)。



以下user输入的回答只包含了以上system message里指定的1个事实：

| system    | \<insert system message above\>                              |
| --------- | ------------------------------------------------------------ |
| user      | """Neil Armstrong made history when he stepped off the lunar module, becoming the first person to walk on the moon.""" |
| assistant | 1 - Restate the point: Neil Armstrong was the first individual to set foot on the moon.<br/>2 - Citation from the answer: "Neil Armstrong made history when he stepped off the lunar module, becoming the first person to walk on the moon."<br/>3 - Consider if someone reading the citation who doesn't know the topic could directly infer the point: Yes, the citation directly states that Neil Armstrong was the first person to walk on the moon.<br/>4 - Write "yes" if the answer to 3 was yes, otherwise write "no": Yes<br/><br/>1 - Restate the point: Neil Armstrong first walked on the moon on July 21, 1969.<br/>2 - Citation from the answer: There is no citation from the answer that provides this information.<br/>3 - Consider if someone reading the citation who doesn't know the topic could directly infer the point: No, the citation does not provide a date for when Neil Armstrong first walked on the moon.<br/>4 - Write "yes" if the answer to 3 was yes, otherwise write "no": No<br/><br/>{"count": 1} |

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-2)。



以下user输入的回答完全没有包含任何system message里指定的事实：

| system    | \<insert system message above\>                              |
| --------- | ------------------------------------------------------------ |
| user      | """In the summer of '69, a voyage grand, Apollo 11, bold as legend's hand. Armstrong took a step, history unfurled, "One small step," he said, for a new world.""" |
| assistant | 1 - The point is that Neil Armstrong was the first person to walk on the moon.<br/>2 - The closest citation from the answer is: "Armstrong took a step, history unfurled."<br/>3 - Someone reading the citation who doesn't know the topic could infer that Armstrong did something significant, but it doesn't directly state that he was the first person to walk on the moon. The phrase "history unfurled" suggests a significant event, but it doesn't specify what that event was.<br/>4 - No<br/><br/>1 - The point is that the date Neil Armstrong first walked on the moon was July 21, 1969.<br/>2 - The closest citation from the answer is: "In the summer of '69, a voyage grand."<br/>3 - Someone reading the citation who doesn't know the topic could infer that a significant event happened in the summer of 1969, but it doesn't directly state that this was the date Neil Armstrong first walked on the moon.<br/>4 - No<br/><br/>{"count": 0} |

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-3)



### 场景2：让大模型直接比较2个回答

如果我们知道问题的标准答案，这个时候可以让大模型来评估模型输出的回答和标准答案之间的重合度，以及模型给的回答是否和标准答案有冲突。

我们可以给大模型设定如下system message:

| system | Use the following steps to respond to user inputs. Fully restate each step before proceeding. i.e. "Step 1: Reason...". <br><br>Step 1: Reason step-by-step about whether the information in the submitted answer compared to the expert answer is either: disjoint, equal, a subset, a superset, or overlapping (i.e. some intersection but not subset/superset). <br/><br/>Step 2: Reason step-by-step about whether the submitted answer contradicts any aspect of the expert answer. <br/><br/>Step 3: Output a JSON object structured like: {"type_of_overlap": "disjoint" or "equal" or "subset" or "superset" or "overlapping", "contradiction": true or false} |
| ------ | ------------------------------------------------------------ |



以下是一个示例，模型给的回答(Submitted Answer)只是标准答案(Expert Answer)内容的一个子集，和标准答案之间没有内容上的冲突，标准答案更优。

| system    | \<insert system message above\>                              |
| --------- | ------------------------------------------------------------ |
| user      | Question: """What event is Neil Armstrong most famous for and on what date did it occur? Assume UTC time.""" <br><br/>Submitted Answer: """Didn't he walk on the moon or something?""" <br/><br/>Expert Answer: """Neil Armstrong is most famous for being the first person to walk on the moon. This historic event occurred on July 21, 1969.""" |
| assistant | Step 1: Reasoning about the relationship between the submitted answer and the expert answer, it can be seen that the submitted answer is a subset of the expert answer. The submitted answer mentions that Neil Armstrong walked on the moon, which is part of the expert answer. However, it does not provide the date of the event, which is included in the expert answer.<br/><br/>Step 2: Reasoning about whether the submitted answer contradicts any aspect of the expert answer, it can be seen that there is no contradiction. The submitted answer does not provide any information that goes against the expert answer.<br/><br/>Step 3: The output JSON object would be structured as follows: {"type_of_overlap": "subset", "contradiction": false}. |

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-4)。



以下是一个示例，模型给的回答(Submitted Answer)与标准答案(Expert Answer)有冲突，模型给的回答是错误的。

| system    | \<insert system message above\>                              |
| --------- | ------------------------------------------------------------ |
| user      | Question: """What event is Neil Armstrong most famous for and on what date did it occur? Assume UTC time.""" <br><br>Submitted Answer: """On the 21st of July 1969, Neil Armstrong became the second person to walk on the moon, following after Buzz Aldrin.""" <br/><br/>Expert Answer: """Neil Armstrong is most famous for being the first person to walk on the moon. This historic event occurred on July 21, 1969.""" |
| assistant | Step 1: The information in the submitted answer compared to the expert answer is overlapping. Both answers agree on the date of the event, July 21, 1969. However, they disagree on the order of the moonwalkers. The submitted answer states that Neil Armstrong was the second person to walk on the moon, while the expert answer states that he was the first.<br/><br/>Step 2: The submitted answer contradicts the expert answer. The expert answer states that Neil Armstrong was the first person to walk on the moon, while the submitted answer incorrectly states that he was the second, following Buzz Aldrin.<br/><br/>Step 3: The output JSON object would be structured as follows: {"type_of_overlap": "overlapping", "contradiction": true}. |

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-5)。



以下是一个示例，模型给的回答(Submitted Answer)比标准答案(Expert Answer)要更好。

| system    | \<insert system message above\>                              |
| --------- | ------------------------------------------------------------ |
| user      | Question: """What event is Neil Armstrong most famous for and on what date did it occur? Assume UTC time."""<br/><br/>Submitted Answer: """At approximately 02:56 UTC on July 21st 1969, Neil Armstrong became the first human to set foot on the lunar surface, marking a monumental achievement in human history."""<br/><br/>Expert Answer: """Neil Armstrong is most famous for being the first person to walk on the moon. This historic event occurred on July 21, 1969.""" |
| assistant | Step 1: Reasoning about the relationship between the submitted answer and the expert answer, it can be observed that the submitted answer contains all the information present in the expert answer and even provides additional details such as the exact time of the event. Therefore, the submitted answer is a superset of the expert answer.<br/><br/>Step 2: Reasoning about whether the submitted answer contradicts any aspect of the expert answer, it can be seen that there is no contradiction. Both answers agree that Neil Armstrong is most famous for being the first person to walk on the moon and that this event occurred on July 21, 1969.<br/><br/>Step 3: Outputting a JSON object structured as requested, the result would be: {"type_of_overlap": "superset", "contradiction": false}. |

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-6)。



## 总结

本文是ChatGPT使用最佳实践系列第6篇 - 系统化测试。

详细讲述了1个策略，以上策略不仅适用于GPT模型，还适用于其它大语言模型。

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，可以看到所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://platform.openai.com/docs/guides/gpt-best-practices