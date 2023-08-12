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

| **Worse**                                       | **Better**                                                   |
| :---------------------------------------------- | :----------------------------------------------------------- |
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

例如，你希望GPT帮你做内容创作，然后在每段内容里包含至少一个笑话或俏皮的评论。

那system可以这么如下示例：

| SYSTEM | When I ask for help to write something, you will reply with a document that contains at least one joke or playful comment in every paragraph. |
| ------ | ------------------------------------------------------------ |
| USER   | Write a thank you note to my steel bolt vendor for getting the delivery in on time and in short notice. This made it possible for us to deliver an important order. |

可以在这个链接里看效果：[Open in Playground](https://platform.openai.com/playground/p/default-playful-thank-you-note)



## 策略3：用分隔符来明确prompt的不同组成部分

分隔符可以方便大模型更精确识别prompt里的不同组成部分，回答效果更好。

参考示例：

| USER | Summarize the text delimited by triple quotes with a haiku. <br>"""insert text here""" |
| ---- | ------------------------------------------------------------ |



| SYSTEM | You will be provided with a pair of articles (delimited with XML tags) about the same topic. First summarize the arguments of each article. Then indicate which of them makes a better argument and explain why. |
| ------ | ------------------------------------------------------------ |
| USER   | <article> insert first article here </article> <br><article> insert second article here </article> |



| SYSTEM | You will be provided with a thesis abstract and a suggested title for it. The thesis title should give the reader a good idea of the topic of the thesis but should also be eye-catching. If the title does not meet these criteria, suggest 5 alternatives. |
| ------ | ------------------------------------------------------------ |
| USER   | Abstract: insert abstract here Title: insert title here      |



对于一些很简单的任务，加分隔符前后效果可能不明显。

但是对于一些复杂的任务，比如很长的的prompt，加分隔符可以让GPT精确识别到每部分的结构，回答效果会更好。

## 策略4：指定完成本项任务需要的步骤

有些任务是可以分步拆解的，明确告诉GPT要执行的每个步骤可以让回答效果更好。

| SYSTEM | Use the following step-by-step instructions to respond to user inputs. <br><br/>Step 1 - The user will provide you with text in triple quotes. Summarize this text in one sentence with a prefix that says "Summary: ". <br><br/>Step 2 - Translate the summary from Step 1 into Spanish, with a prefix that says "Translation: ". |
| ------ | ------------------------------------------------------------ |
| USER   | """insert text here"""                                       |

比如上面的例子，GPT的回答就会根据你的要求，第一步先输出summary，第二步再把summary翻译为西班牙语。

可以在这个链接里看效果：[Open in Playground](https://platform.openai.com/playground/p/default-step-by-step-summarize-and-translate)

## 策略5：提供示例

有时候你希望GPT按照你想要的风格回答问题，但是这个风格又很难用明确的语言表述出来，就可以通过提供样例的方式给GPT，这种就叫 few-shot learning/prompting。

参考示例如下，你提供了一组<user, assistant>样例，system里指定了模型要扮演的角色。

后续user的问题，模型就会按照你提供的样例的风格进行回答。

| SYSTEM    | Answer in a consistent style.                                |
| --------- | ------------------------------------------------------------ |
| USER      | Teach me about patience.                                     |
| ASSISTANT | The river that carves the deepest valley flows from a modest spring; the grandest symphony originates from a single note; the most intricate tapestry begins with a solitary thread. |
| USER      | Teach me about the ocean.                                    |

可以在这个链接里看效果：[Open in Playground](https://platform.openai.com/playground/p/default-chat-few-shot)

## 策略6：明确你想要的输出结果的长度

你可以告诉模型回答内容的长度，这个长度可以是字数，可以是句子数量，也可以是段落数量等。对于字数，模型不会特别精准。

参考示例如下：

| USER | Summarize the text delimited by triple quotes in about 50 words. """insert text here""" |
| ---- | ------------------------------------------------------------ |



| USER | Summarize the text delimited by triple quotes in 2 paragraphs. """insert text here""" |
| ---- | ------------------------------------------------------------ |



| USER | Summarize the text delimited by triple quotes in 3 bullet points. """insert text here""" |
| ---- | ------------------------------------------------------------ |



## 总结

本文是ChatGPT使用最佳实践系列第1篇 - 提供清晰且明确的指令(write clear instructions)。

详细讲述了6个策略，以上策略不仅适用于GPT模型，还适用于其它大语言模型。



文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，可以看到所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://platform.openai.com/docs/guides/gpt-best-practices