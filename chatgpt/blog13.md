# OpenAI发布新的embedding模型和API更新

## 背景

OpenAI在2024年1月25日发布了重要更新，主要更新内容如下：

* 更新了GPT-4 Turbo模型
* 更新了GPT-3.5 Turbo模型
* 更新了文本审查模型(moderation model)
* GPT-3.5 Turbo降价
* 引入了新的API使用管理工具
* 引入2个新的embedding模型

默认地，发送给OpenAI API的数据不会被OpenAI用于模型训练和优化。

### GPT-3.5模型升级和降价

从2024年1月29日开始，OpenAI引入了一个新的GTP-3.5 Turbo模型，叫`gpt-3.5-turbo-0125`。与此同时，OpenAI会对GPT-3.5 Turbo模型进行降价。

新的GPT-3.5 Turbo模型对于输入token的费用下降50%，降为0.0005美金/1K token，输出token的费用下降25%到0.0015美金/1K token。

这个新的GPT-3.5 Turbo模型做了很多改进提升，包括提升了问题回答的准确性以及修复了非英语场景下function call的bug。

新模型发布2周后，开发者如果在API调用时指定GPT-3.5-turbo，会自动从之前的gpt-3.5-turbo-0613升级到gpt-3.5-turbo-0125。

如果想迫不及待马上使用最新模型的话，就直接在API调用的时候指定模型为gpt-3.5-turbo-0125即可。

### GPT-4 Turbo模型升级

GPT-4 API调用里，超过70%的请求使用的都是GPT-4 Turbo模型，主要是以下原因：

* 使用的训练数据更新。GPT-4 Turbo模型使用的训练数据截止到2023年4月，GPT-4模型使用的训练数据截止到2021年9月。
* 更大的上下文窗口。GPT-4 Turbo模型支持128k上下文窗口，GPT-4模型支持8k上下文窗口。
* 价格更便宜。

此次发布的GPT-4 Turbo新模型叫gpt-4-0125-priview。

这个模型比之前的GPT-4 Turbo模型在任务完成度上更好，优化了之前模型的偷懒行为。

同时，这个新模型还修复了对于非英语语言的UTF-8内容生成的bug。

开发者在调用API时，指定模型为gpt-4-turbo-preview就可以自动使用到最新的gpt-4-0125-preview新模型。

此外，OpenAI计划在接下来的几个月里发布更为强大的GPT-4 Turbo with vision模型。

### 审查模型升级

OpenAI目前免费的审查API可以帮助开发者检测出有害内容。

这次发布的新审查模型叫text-moderation-007，是OpenAI目前最稳定的审查模型。

如果你在开发的时候指定模型为text-moderation-latest或者text-moderation-stable，都会自动只想这个text-moderation-007新模型。

如果你想构建安全的AI系统，可以参考 [safety best practices guide](https://platform.openai.com/docs/guides/safety-best-practices)。

## API Key管理升级

API管理进行了两个功能升级，可以帮助开发者更好地管理和分析API key的使用。

第一，开发者可以对创建的API key做权限控制，比如可以指定API key只有特定API的使用权限。具体权限设置地址：https://platform.openai.com/api-keys。

第二，支持对API key开启tracking跟踪功能，开启后，在API key的Usage面板里可以看到每个API key的使用情况，做更精细化的API key使用分析。

OpenAI在接下来的几个月里，会进一步优化API key的管理和使用分析。

## 升级embedding模型和降价

OpenAI发布了2个新的embedding模型：一个小巧但是高效的text-embedding-3-small模型和一个规模更大效果更好地text-embedding-3-large模型。

在此之前，OpenAI的embedding模型是2022年12月发布的text-embedding-ada-002模型。

| Model                  | Usage                |
| ---------------------- | -------------------- |
| text-embedding-3-small | $0.00002 / 1K tokens |
| text-embedding-3-large | $0.00013 / 1K tokens |
| ada v2                 | $0.00010 / 1K tokens |

## 总结

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，可以看到所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://openai.com/blog/new-embedding-models-and-api-updates

* https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo

* https://openai.com/pricing#language-models
