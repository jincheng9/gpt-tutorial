# ChatGPT最佳实践系列第4篇-给GPT思考的时间

## 背景

OpenAI官方详细介绍了ChatGPT使用的最佳实践，不仅适用于使用ChatGPT网站进行直接对话的用户，还适用于通过OpenAI API接入的开发者。

掌握了这些最佳实践，就能更好地利用GPT大模型。

本文是ChatGPT使用最佳实践系列第4篇 - 给GPT思考的时间。

假设你被问到 17乘以28 是多少，大概率没办法立马给出回答。但是经过几秒的心算你就可以得到正确的结果。

GPT在做推理的时候也是同理，如果能给大模型思考的时间，让大模型分步推理，往往回答效果会更好。

## 策略1：引导大模型给出自己的解

直接让大模型立马给出结论往往不能达到最佳效果，比如下面的例子：

| system    | Determine if the student's solution is correct or not.       |
| --------- | ------------------------------------------------------------ |
| user      | Problem Statement: I'm building a solar power installation and I need help working out the financials. <br>- Land costs $100 / square foot <br>- I can buy solar panels for $250 / square foot <br>- I negotiated a contract for maintenance that will cost me a flat $100k per year, and an additional $10 / square foot <br>What is the total cost for the first year of operations as a function of the number of square feet. <br>Student's Solution: Let x be the size of the installation in square feet. 1. Land cost: 100x 2. Solar panel cost: 250x 3. Maintenance cost: 100,000 + 100x Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000 |
| assistant | The student's solution is correct.                           |

显然上面GPT给出的回答是错误的。

但是我们如果从第一性原理(第一性原理指的是，回归事物最基本的条件，将其拆分成各要素进行解构分析，从而找到实现目标最优路径的方法)出发，重新设计system消息，那大模型的回答效果可以更好，参考下面的例子：

| system    | First work out your own solution to the problem. Then compare your solution to the student's solution and evaluate if the student's solution is correct or not. Don't decide if the student's solution is correct until you have done the problem yourself. |
| --------- | ------------------------------------------------------------ |
| user      | Problem Statement: I'm building a solar power installation and I need help working out the financials. <br/>- Land costs $100 / square foot <br/>- I can buy solar panels for $250 / square foot <br/>- I negotiated a contract for maintenance that will cost me a flat $100k per year, and an additional $10 / square foot <br/>What is the total cost for the first year of operations as a function of the number of square feet. <br/>Student's Solution: Let x be the size of the installation in square feet. 1. Land cost: 100x 2. Solar panel cost: 250x 3. Maintenance cost: 100,000 + 100x Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000 |
| assistant | Let x be the size of the installation in square feet. <br>1. Land cost: 100x <br>2. Solar panel cost: 250x <br>3. Maintenance cost: 100,000 + 10x <br>Total cost: 100x + 250x + 100,000 + 10x = 360x + 100,000 <br><br>The student's solution is incorrect. They made an error in the maintenance cost calculation, using 100x instead of 10x. The correct total cost for the first year of operations is 360x + 100,000. |

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-avoid-rushing-to-a-conclusion)。

## 策略2：隐藏模型推理过程

在有些场景里我们其实并不希望暴露模型的推理过程。

比如上面的数学问题求解，如果直接暴露了模型推理过程，等于直接让学生知道了具体解题步骤。这种情况下，我们其实是希望大模型可以给出一些提示，引导解题错误的学生去思考，根据提示自己找到正确答案。

对于这种场景，就可以使用内心独白(inner monologue)或一系列的查询来隐藏模型的推理过程。

内心独白的具体思路就是把希望隐藏的内容让大模型以特定的格式返回，这样开发人员可以方便解析到，把这部分内容不返回前端，学生就只能看到我们希望他看到的内容了。

| system | Follow these steps to answer the user queries. <br><br>Step 1 - First work out your own solution to the problem. Don't rely on the student's solution since it may be incorrect. Enclose all your work for this step within triple quotes ("""). <br/><br/>Step 2 - Compare your solution to the student's solution and evaluate if the student's solution is correct or not. Enclose all your work for this step within triple quotes ("""). <br/><br/>Step 3 - If the student made a mistake, determine what hint you could give the student without giving away the answer. Enclose all your work for this step within triple quotes ("""). <br/><br/>Step 4 - If the student made a mistake, provide the hint from the previous step to the student (outside of triple quotes). Instead of writing "Step 4 - ..." write "Hint:". |
| ------ | ------------------------------------------------------------ |
| user   | Problem Statement: \<insert problem statement\> <br><br>Student Solution: \<insert student solution\> |

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-inner-monologue)。

上面的方式我们叫内心独白(inner monologue)，除了这种方式，我们还可以通过一系列查询来隐藏模型推理过程，只把最后我们想要的结果返回给前端。

比如对于上面的数学问题，我们按照如下步骤做一系列查询：

第一步：先让大模型对问题进行求解：

| user | \<insert problem statement\> |
| ---- | ---------------------------- |

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-query-sequence-1)。

第二步：让大模型根据学生的回答以及自己的回答来分析学生回答是否正确。

| system | Compare your solution to the student's solution and evaluate if the student's solution is correct or not. |
| ------ | ------------------------------------------------------------ |
| user   | Problem statement: """\<insert problem statement\>""" <br><br>Your solution: """\<insert model generated solution\>""" <br><br>Student’s solution: """\<insert student's solution\>""" |

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-query-sequence-2)。

第三步：根据前2步的回答来构造system消息，让大模型在学生回答出错的情况下给出提示。

| system | You are a math tutor. If the student made an error, offer a hint to the student in a way that does not reveal the answer. If the student did not make an error, simply offer them an encouraging comment. |
| ------ | ------------------------------------------------------------ |
| user   | Problem statement: """\<insert problem statement\>""" <br><br>Your solution: """\<insert model generated solution\>""" <br/><br/>Student’s solution: """\<insert student's solution\>""" <br/><br/>Analysis: """\<insert model generated analysis from previous step\>""" |

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-query-sequence-3)。



## 策略3：询问模型在之前的回答中是否遗漏了内容

假设这样一个场景：我们需要GPT模型给出指定文档中，和某个问题相关的摘录。

在列出每一个摘录后，该模型需要确定是否应该开始写另一个摘录，还是回答结束应该停下来了。

如果源文档很大，模型常常过早停止，不能列出所有相关的摘录。

在这种情况下，我们可以向模型提问是否有缺失的摘录没有列出来，那GPT大模型会尝试找出遗漏的摘录内容，从而获得更好的回答效果。

| system    | You will be provided with a document delimited by triple quotes. Your task is to select excerpts which pertain to the following question: "What significant paradigm shifts have occurred in the history of artificial intelligence." <br><br>Ensure that excerpts contain all relevant context needed to interpret them - in other words don't extract small snippets that are missing important context. Provide output in JSON format as follows:<br><br> [{"excerpt": "..."}, <br>... <br>{"excerpt": "..."}] |
| --------- | ------------------------------------------------------------ |
| user      | """<insert document here>"""                                 |
| assistant | [{"excerpt": "the model writes an excerpt here"}, <br>... <br>{"excerpt": "the model writes another excerpt here"}] |
| user      | Are there more relevant excerpts? Take care not to repeat excerpts. Also ensure that excerpts contain all relevant context needed to interpret them - in other words don't extract small snippets that are missing important context. |

可以通过这个链接地址进行体验：[Open in Playground](https://platform.openai.com/playground/p/default-2nd-pass)。



## 总结

本文是ChatGPT使用最佳实践系列第4篇 - 给GPT思考的时间。

详细讲述了3个策略，以上策略不仅适用于GPT模型，还适用于其它大语言模型。

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，可以看到所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://platform.openai.com/docs/guides/gpt-best-practices