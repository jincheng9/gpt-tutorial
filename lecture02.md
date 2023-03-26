# GPT常见概念

## Prompt和Completion

## Model

OpenAI支持包括GPT-4, GPT-3.5, DALL-E, Whisper等众多Model，每个Model有各自的适用场景。

比如GPT-4是基于GPT-3.5衍生出来的，比GPT-3.5更强大，未来还会支持根据文本输入生成图片。

DALL-E可以根据文本生成或者编辑图片。

Whisper可以根据录音生成文本。

* [OpenAI的Model列表和具体说明](https://platform.openai.com/docs/models)

注意：

* 上面提到的GPT-4，GPT-3.5等，其实每一个都可以理解为一个Model Family，每个Model Family包含有更细分的版本，比如GPT-3.5这个Model Family有gpt-3.5-turbo，text-davinci-003等多个Model。

* 以上模型的Training Data数据截止到2021年9月，未来可能会引入更新的Training Data。

* ChatGPT不能联网获取最新知识，但是ChatGPT推出了[ChatGPT plugin](https://openai.com/blog/chatgpt-plugins)，可以通过插件的方式获取最新知识。

  ![](/Users/zhangjincheng/Desktop/zhangjincheng/github/gpt-tutorial/lecture02_1.png)

## Token

* [Token个数统计和可视化：https://platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)

## API

官方支持Python和NodeJS，其它语言目前是社区提供。

* [Python](https://github.com/openai/openai-python)

* [NodeJS](https://github.com/openai/openai-node)

* [其它语言的API](https://platform.openai.com/docs/libraries)