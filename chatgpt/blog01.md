# ChatGPT API重大升级

## 背景

OpenAI官方在2023.06.13发布了API层面的重磅升级，主要变化如下：

* 在Chat Completions这个API里支持了开发者自定义的函数调用。
* 更新了`gpt-4`和`gpt-3.5-turbo`模型。
* `gpt-3.5-turbo`支持的上下文长度扩容到16K，之前只支持4K个token。
* embedding model的使用成本降低75%。
* `gpt-3.5-turbo`模型的input token的成本降低25%，从原来的0.002美金 / 1K token降低为0.0015美金 / 1K token。
* 2023.09.13会下线`gpt-3.5-turbo-0301`、`gpt-4-0314`和`gpt-4-32k-0314` 模型，过了这个时间点调用这些模型会请求失败。

上面提到的这些模型都严格遵循2023.03.01发布的隐私和安全规定，用户通过API发送的数据和API返回的数据不会用于OpenAI大模型的训练。

## Function calling

Developers can now describe functions to `gpt-4-0613` and `gpt-3.5-turbo-0613`, and have the model intelligently choose to output a JSON object containing arguments to call those functions. This is a new way to more reliably connect GPT's capabilities with external tools and APIs.

These models have been fine-tuned to both detect when a function needs to be called (depending on the user’s input) and to respond with JSON that adheres to the function signature. Function calling allows developers to more reliably get structured data back from the model. For example, developers can:

- Create chatbots that answer questions by calling external tools (e.g., like ChatGPT Plugins)

Convert queries such as “Email Anya to see if she wants to get coffee next Friday” to a function call like `send_email(to: string, body: string)`, or “What’s the weather like in Boston?” to `get_current_weather(location: string, unit: 'celsius' | 'fahrenheit')`.

- Convert natural language into API calls or database queries

Convert “Who are my top ten customers this month?” to an internal API call such as `get_customers_by_revenue(start_date: string, end_date: string, limit: int)`, or “How many orders did Acme, Inc. place last month?” to a SQL query using `sql_query(query: string)`.

- Extract structured data from text

Define a function called `extract_people_data(people: [{name: string, birthday: string, location: string}])`, to extract all people mentioned in a Wikipedia article.

These use cases are enabled by new API parameters in our `/v1/chat/completions` endpoint, `functions` and `function_call`, that allow developers to describe functions to the model via JSON Schema, and optionally ask it to call a specific function. Get started with our [developer documentation](https://platform.openai.com/docs/guides/gpt/function-calling) and [add evals](https://github.com/openai/evals) if you find cases where function calling could be improved

# Function calling例子

What’s the weather like in Boston right now?

Step 1·OpenAI API

Call the model with functions and the user’s input

- [Request](https://openai.com/blog/function-calling-and-other-api-updates#)
- [Response](https://openai.com/blog/function-calling-and-other-api-updates#)

```bash
curl https://api.openai.com/v1/chat/completions -u :$OPENAI_API_KEY -H 'Content-Type: application/json' -d '{
  "model": "gpt-3.5-turbo-0613",
  "messages": [
    {"role": "user", "content": "What is the weather like in Boston?"}
  ],
  "functions": [
    {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"]
          }
        },
        "required": ["location"]
      }
    }
  ]
}'
```

Step 2·Third party API

Use the model response to call your API



- [Request](https://openai.com/blog/function-calling-and-other-api-updates#)
- [Response](https://openai.com/blog/function-calling-and-other-api-updates#)

```plaintext
curl https://weatherapi.com/...
```

Step 3·OpenAI API

Send the response back to the model to summarize



- [Request](https://openai.com/blog/function-calling-and-other-api-updates#)
- [Response](https://openai.com/blog/function-calling-and-other-api-updates#)

```bash
curl https://api.openai.com/v1/chat/completions -u :$OPENAI_API_KEY -H 'Content-Type: application/json' -d '{
  "model": "gpt-3.5-turbo-0613",
  "messages": [
    {"role": "user", "content": "What is the weather like in Boston?"},
    {"role": "assistant", "content": null, "function_call": {"name": "get_current_weather", "arguments": "{ \"location\": \"Boston, MA\"}"}},
    {"role": "function", "name": "get_current_weather", "content": "{\"temperature\": "22", \"unit\": \"celsius\", \"description\": \"Sunny\"}"}
  ],
  "functions": [
    {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": ["celsius", "fahrenheit"]
          }
        },
        "required": ["location"]
      }
    }
  ]
}'
```





The weather in Boston is currently sunny with a temperature of 22 degrees Celsius.

Since the alpha release of ChatGPT plugins, we have learned much about making tools and language models work together safely. However, there are still open research questions. For example, a proof-of-concept exploit illustrates how untrusted data from a tool’s output can instruct the model to perform unintended actions. We are working to mitigate these and other risks. Developers can protect their applications by only consuming information from trusted tools and by including user confirmation steps before performing actions with real-world impact, such as sending an email, posting online, or making a purchase.

## 新模型

### GPT-4模型

`gpt-4-0613` 相对于`gpt-4`，新增了函数调用的支持。

`gpt-4-32k-0613` 相对于`gpt-4-32k`，同样是新增了函数调用的支持。

在接下来的几周里，OpenAI会把GPT-4 API waiting list上的申请都尽量审批通过，让开发者可以享用到GPT-4的强大能力。还没申请的赶紧去申请吧。

### GPT-3.5 Turbo模型

`gpt-3.5-turbo-0613` 相对于`gpt-3.5-turbo`，新增了函数调用的支持。

`gpt-3.5-turbo-16k` 支持的上下文长度扩容到了16K，是`gpt-3.5-turbo`的4倍，费用是`gpt-3.5-turbo`的2倍。具体费用是每1K input token需要0.003美金， 每1K output token需要0.004美金。

### 旧模型下线时间

从2023.06.13开始，OpenAI会开始升级生产环境的`gpt-4`、`gpt-4-32k`和`gpt-3.5-turbo`模型到最新版本，预计2023.06.27开始就可以使用到升级后的模型了。

如果开发者不想升级，可以继续使用旧版本的模型，不过需要在model参数里指定用
 `gpt-3.5-turbo-0301`，`gpt-4-0314` 或 `gpt-4-32k-0314` 。

这些旧版本的模型在2023.09.13会下线，后续继续调用会请求失败。

## 更低价格

### Embedding模型

`text-embedding-ada-002`目前是OpenAI所有embedding模型里最受欢迎的。

现在使用这个embedding模型的成本降低为0.0001美金/1K token，成本下降75%。

### GPT-3.5 Turbo模型

`gpt-3.5-turbo` 模型在收费的时候，既对用户发送的问题(input token)收费，也对API返回的结果(output token)收费。

现在该模型的input token成本降低25%，每1K input token的费用为0.0015美金。

output token的费用保持不变，还是0.002美金/1K token。

`gpt-3.5-turbo-16k` 模型的input token收费是0.003美金/1K token，output token收费是0.004美金/1K token。



## 总结

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，可以看到所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://openai.com/blog/function-calling-and-other-api-updates
