# ChatGPT最佳实践系列-第1篇

## 背景

OpenAI官方详细介绍了ChatGPT使用的最佳实践，不仅适用于使用ChatGPT网站进行直接对话的用户，还适用于通过OpenAI API接入的开发者。

掌握了这些最佳实践，就能更好地利用GPT大模型。

本文是ChatGPT使用最佳实践系列第1篇 - 提供清晰且明确的指令(write clear instructions)。

GPT大模型并不会读心术，需要你在提示词(prompt)里明确你的具体诉求，大模型才会提供最佳的回答。

* 如果大模型给的回答过长，你可以在prompt里告诉它你想要更简短的回答。
* 如果大模型给的回答过于简单，你可以在prompt里要求它提供专家水准一般的输出。
* 如果大模型给的回答格式你不喜欢，你可以在prompt里展示你想要的输出格式。

简而言之，GPT需要猜的东西越少，回答的效果也会越好。

接下来详细讲述下6个具体的操作指引。

## 策略1：在prompt里提供细节

如果要让GPT给出你想要的结果，需要确保你的prompt里包含重要的细节，否则GPT模型需要猜测你想要的答案，那给出的结果就未必好了。

以下是一些具体示例，第一列为bad prompt，第二列为good prompt。

|                                                 |                                                              |
| :---------------------------------------------- | :----------------------------------------------------------- |
| **Worse**                                       | **Better**                                                   |
| How do I add numbers in Excel?                  | How do I add up a row of dollar amounts in Excel? I want to do this automatically for a whole sheet of rows with all the totals ending up on the right in a column called "Total". |
| Who’s president?                                | Who was the president of Mexico in 2021, and how frequently are elections held? |
| Write code to calculate the Fibonacci sequence. | Write a TypeScript function to efficiently calculate the Fibonacci sequence. Comment the code liberally to explain what each piece does and why it's written that way. |
| Summarize the meeting notes.                    | Summarize the meeting notes in a single paragraph. Then write a markdown list of the speakers and each of their key points. Finally, list the next steps or action items suggested by the speakers, if any. |

## 策略2：指定模型需要扮演的角色

OpenAI的Chat Completions API里的messages参数可以通过指定role为system来告诉模型需要扮演的角色。

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "system",
        "content": "You are a math genius."
      },
      {
        "role": "user",
        "content": "Hello!"
      }
    ]
  }'
```





SYSTEM

When I ask for help to write something, you will reply with a document that contains at least one joke or playful comment in every paragraph.

USER

Write a thank you note to my steel bolt vendor for getting the delivery in on time and in short notice. This made it possible for us to deliver an important order.

[Open in Playground](https://platform.openai.com/playground/p/default-playful-thank-you-note)

## 策略3：用分隔符来明确prompt的不同组成部分



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

## 策略4：指定完成本项任务需要的步骤

Some tasks are best specified as a sequence of steps. Writing the steps out explicitly can make it easier for the model to follow them.

SYSTEM

Use the following step-by-step instructions to respond to user inputs. Step 1 - The user will provide you with text in triple quotes. Summarize this text in one sentence with a prefix that says "Summary: ". Step 2 - Translate the summary from Step 1 into Spanish, with a prefix that says "Translation: ".

USER

"""insert text here"""

[Open in Playground](https://platform.openai.com/playground/p/default-step-by-step-summarize-and-translate)

## 策略5：提供示例

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

## 策略6：明确你想要的输出结果的长度

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