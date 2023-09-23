# ChatGPT最佳实践系列第6篇-系统化测试

## 背景

OpenAI官方详细介绍了ChatGPT使用的最佳实践，不仅适用于使用ChatGPT网站进行直接对话的用户，还适用于通过OpenAI API接入的开发者。

掌握了这些最佳实践，就能更好地利用GPT大模型。

本文是ChatGPT使用最佳实践系列第6篇 - 系统化测试。

Sometimes it can be hard to tell whether a change — e.g., a new instruction or a new design — makes your system better or worse. Looking at a few examples may hint at which is better, but with small sample sizes it can be hard to distinguish between a true improvement or random luck. Maybe the change helps performance on some inputs, but hurts performance on others.

Evaluation procedures (or "evals") are useful for optimizing system designs. Good evals are:

- Representative of real-world usage (or at least diverse)
- Contain many test cases for greater statistical power (see table below for guidelines)
- Easy to automate or repeat

| DIFFERENCE TO DETECT | SAMPLE SIZE NEEDED FOR 95% CONFIDENCE |
| :------------------- | :------------------------------------ |
| 30%                  | ~10                                   |
| 10%                  | ~100                                  |
| 3%                   | ~1,000                                |
| 1%                   | ~10,000                               |

Evaluation of outputs can be done by computers, humans, or a mix. Computers can automate evals with objective criteria (e.g., questions with single correct answers) as well as some subjective or fuzzy criteria, in which model outputs are evaluated by other model queries. [OpenAI Evals](https://github.com/openai/evals) is an open-source software framework that provides tools for creating automated evals.

Model-based evals can be useful when there exists a range of possible outputs that would be considered equally high in quality (e.g. for questions with long answers). The boundary between what can be realistically evaluated with a model-based eval and what requires a human to evaluate is fuzzy and is constantly shifting as models become more capable. We encourage experimentation to figure out how well model-based evals can work for your use case.

## 策略：

Suppose it is known that the correct answer to a question should make reference to a specific set of known facts. Then we can use a model query to count how many of the required facts are included in the answer.

For example, using the following system message:

SYSTEM

You will be provided with text delimited by triple quotes that is supposed to be the answer to a question. Check if the following pieces of information are directly contained in the answer: - Neil Armstrong was the first person to walk on the moon. - The date Neil Armstrong first walked on the moon was July 21, 1969. For each of these points perform the following steps: 1 - Restate the point. 2 - Provide a citation from the answer which is closest to this point. 3 - Consider if someone reading the citation who doesn't know the topic could directly infer the point. Explain why or why not before making up your mind. 4 - Write "yes" if the answer to 3 was yes, otherwise write "no". Finally, provide a count of how many "yes" answers there are. Provide this count as {"count": <insert count here>}.

Here's an example input where both points are satisfied:

SYSTEM

<insert system message above>

USER

"""Neil Armstrong is famous for being the first human to set foot on the Moon. This historic event took place on July 21, 1969, during the Apollo 11 mission."""

[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-1)

Here's an example input where only one point is satisfied:

SYSTEM

<insert system message above>

USER

"""Neil Armstrong made history when he stepped off the lunar module, becoming the first person to walk on the moon."""

[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-2)

Here's an example input where none are satisfied:

SYSTEM

<insert system message above>

USER

"""In the summer of '69, a voyage grand, Apollo 11, bold as legend's hand. Armstrong took a step, history unfurled, "One small step," he said, for a new world."""

[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-3)

There are many possible variants on this type of model-based eval. Consider the following variation which tracks the kind of overlap between the candidate answer and the gold-standard answer, and also tracks whether the candidate answer contradicts any part of the gold-standard answer.

SYSTEM

Use the following steps to respond to user inputs. Fully restate each step before proceeding. i.e. "Step 1: Reason...". Step 1: Reason step-by-step about whether the information in the submitted answer compared to the expert answer is either: disjoint, equal, a subset, a superset, or overlapping (i.e. some intersection but not subset/superset). Step 2: Reason step-by-step about whether the submitted answer contradicts any aspect of the expert answer. Step 3: Output a JSON object structured like: {"type_of_overlap": "disjoint" or "equal" or "subset" or "superset" or "overlapping", "contradiction": true or false}

Here's an example input with a substandard answer which nonetheless does not contradict the expert answer:

SYSTEM

<insert system message above>

USER

Question: """What event is Neil Armstrong most famous for and on what date did it occur? Assume UTC time.""" Submitted Answer: """Didn't he walk on the moon or something?""" Expert Answer: """Neil Armstrong is most famous for being the first person to walk on the moon. This historic event occurred on July 21, 1969."""

[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-4)

Here's an example input with answer that directly contradicts the expert answer:

SYSTEM

<insert system message above>

USER

Question: """What event is Neil Armstrong most famous for and on what date did it occur? Assume UTC time.""" Submitted Answer: """On the 21st of July 1969, Neil Armstrong became the second person to walk on the moon, following after Buzz Aldrin.""" Expert Answer: """Neil Armstrong is most famous for being the first person to walk on the moon. This historic event occurred on July 21, 1969."""

[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-5)

Here's an example input with a correct answer that also provides a bit more detail than is necessary:

SYSTEM

<insert system message above>

USER

Question: """What event is Neil Armstrong most famous for and on what date did it occur? Assume UTC time.""" Submitted Answer: """At approximately 02:56 UTC on July 21st 1969, Neil Armstrong became the first human to set foot on the lunar surface, marking a monumental achievement in human history.""" Expert Answer: """Neil Armstrong is most famous for being the first person to walk on the moon. This historic event occurred on July 21, 1969."""

[Open in Playground](https://platform.openai.com/playground/p/default-model-based-eval-6)

## 总结

本文是ChatGPT使用最佳实践系列第6篇 - 系统化测试。

详细讲述了3个策略，以上策略不仅适用于GPT模型，还适用于其它大语言模型。

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，可以看到所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://platform.openai.com/docs/guides/gpt-best-practices