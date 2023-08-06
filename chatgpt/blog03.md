# ChatGPT使用最佳实践系列-第1篇

## 背景

This guide shares strategies and tactics for getting better results from GPTs. The methods described here can sometimes be deployed in combination for greater effect. We encourage experimentation to find the methods that work best for you.

Some of the examples demonstrated here currently work only with our most capable model, `gpt-4`. If you don't yet have access to `gpt-4` consider joining the [waitlist](https://openai.com/waitlist/gpt-4-api). In general, if you find that a GPT model fails at a task and a more capable model is available, it's often worth trying again with the more capable model.

[Six strategies for getting better results](https://platform.openai.com/docs/guides/gpt-best-practices/six-strategies-for-getting-better-results)

[Write clear instructions](https://platform.openai.com/docs/guides/gpt-best-practices/write-clear-instructions)

GPTs can’t read your mind. If outputs are too long, ask for brief replies. If outputs are too simple, ask for expert-level writing. If you dislike the format, demonstrate the format you’d like to see. The less GPTs have to guess at what you want, the more likely you’ll get it.

Tactics:

- [Include details in your query to get more relevant answers](https://platform.openai.com/docs/guides/gpt-best-practices/tactic-include-details-in-your-query-to-get-more-relevant-answers)
- [Ask the model to adopt a persona](https://platform.openai.com/docs/guides/gpt-best-practices/tactic-ask-the-model-to-adopt-a-persona)
- [Use delimiters to clearly indicate distinct parts of the input](https://platform.openai.com/docs/guides/gpt-best-practices/tactic-use-delimiters-to-clearly-indicate-distinct-parts-of-the-input)
- [Specify the steps required to complete a task](https://platform.openai.com/docs/guides/gpt-best-practices/tactic-specify-the-steps-required-to-complete-a-task)
- [Provide examples](https://platform.openai.com/docs/guides/gpt-best-practices/tactic-provide-examples)
- [Specify the desired length of the output](https://platform.openai.com/docs/guides/gpt-best-practices/tactic-specify-the-desired-length-of-the-output)



## Strategy: Write clear instructions

### Tactic: Include details in your query to get more relevant answers

In order to get a highly relevant response, make sure that requests provide any important details or context. Otherwise you are leaving it up to the model to guess what you mean.

|                                                 |                                                              |
| :---------------------------------------------- | :----------------------------------------------------------- |
| **Worse**                                       | **Better**                                                   |
| How do I add numbers in Excel?                  | How do I add up a row of dollar amounts in Excel? I want to do this automatically for a whole sheet of rows with all the totals ending up on the right in a column called "Total". |
| Who’s president?                                | Who was the president of Mexico in 2021, and how frequently are elections held? |
| Write code to calculate the Fibonacci sequence. | Write a TypeScript function to efficiently calculate the Fibonacci sequence. Comment the code liberally to explain what each piece does and why it's written that way. |
| Summarize the meeting notes.                    | Summarize the meeting notes in a single paragraph. Then write a markdown list of the speakers and each of their key points. Finally, list the next steps or action items suggested by the speakers, if any. |

### Tactic: Ask the model to adopt a persona

The system message can be used to specify the persona used by the model in its replies.

SYSTEM

When I ask for help to write something, you will reply with a document that contains at least one joke or playful comment in every paragraph.

USER

Write a thank you note to my steel bolt vendor for getting the delivery in on time and in short notice. This made it possible for us to deliver an important order.

[Open in Playground](https://platform.openai.com/playground/p/default-playful-thank-you-note)

### Tactic: Use delimiters to clearly indicate distinct parts of the input

Delimiters like triple quotation marks, XML tags, section titles, etc. can help demarcate sections of text to be treated differently.

USER

Summarize the text delimited by triple quotes with a haiku. """insert text here"""

[Open in Playground](https://platform.openai.com/playground/p/default-delimiters-1)

SYSTEM

You will be provided with a pair of articles (delimited with XML tags) about the same topic. First summarize the arguments of each article. Then indicate which of them makes a better argument and explain why.

USER

<article> insert first article here </article> <article> insert second article here </article>

[Open in Playground](https://platform.openai.com/playground/p/default-delimiters-2)

SYSTEM

You will be provided with a thesis abstract and a suggested title for it. The thesis title should give the reader a good idea of the topic of the thesis but should also be eye-catching. If the title does not meet these criteria, suggest 5 alternatives.

USER

Abstract: insert abstract here Title: insert title here

[Open in Playground](https://platform.openai.com/playground/p/default-delimiters-3)

For straightforward tasks such as these, using delimiters might not make a difference in the output quality. However, the more complex a task is the more important it is to disambiguate task details. Don’t make GPTs work to understand exactly what you are asking of them.

### Tactic: Specify the steps required to complete a task

Some tasks are best specified as a sequence of steps. Writing the steps out explicitly can make it easier for the model to follow them.

SYSTEM

Use the following step-by-step instructions to respond to user inputs. Step 1 - The user will provide you with text in triple quotes. Summarize this text in one sentence with a prefix that says "Summary: ". Step 2 - Translate the summary from Step 1 into Spanish, with a prefix that says "Translation: ".

USER

"""insert text here"""

[Open in Playground](https://platform.openai.com/playground/p/default-step-by-step-summarize-and-translate)

### Tactic: Provide examples

Providing general instructions that apply to all examples is generally more efficient than demonstrating all permutations of a task by example, but in some cases providing examples may be easier. For example, if you intend for the model to copy a particular style of responding to user queries which is difficult to describe explicitly. This is known as "few-shot" prompting.

SYSTEM

Answer in a consistent style.

USER

Teach me about patience.

ASSISTANT

The river that carves the deepest valley flows from a modest spring; the grandest symphony originates from a single note; the most intricate tapestry begins with a solitary thread.

USER

Teach me about the ocean.

[Open in Playground](https://platform.openai.com/playground/p/default-chat-few-shot)

### Tactic: Specify the desired length of the output

You can ask the model to produce outputs that are of a given target length. The targeted output length can be specified in terms of the count of words, sentences, paragraphs, bullet points, etc. Note however that instructing the model to generate a specific number of words does not work with high precision. The model can more reliably generate outputs with a specific number of paragraphs or bullet points.

USER

Summarize the text delimited by triple quotes in about 50 words. """insert text here"""

[Open in Playground](https://platform.openai.com/playground/p/default-summarize-text-50-words)

USER

Summarize the text delimited by triple quotes in 2 paragraphs. """insert text here"""

[Open in Playground](https://platform.openai.com/playground/p/default-summarize-text-2-paragraphs)

USER

Summarize the text delimited by triple quotes in 3 bullet points. """insert text here"""

[Open in Playground](https://platform.openai.com/playground/p/default-summarize-text-3-bullet-points)

## 总结

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，可以看到所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://platform.openai.com/docs/guides/gpt-best-practices