# BLOOMChat: 开源可商用支持多语言的重磅模型

## 背景

SambaNova和Together这2家公司于2023.05.19开源了可商用的支持多语言的微调模型BLOOMChat。

SambaNova这家公司专注于为企业和政府提供生成式AI平台，Together专注于用开源的方式打造一站式的foundation model，赋能各个行业。

OpenAI的GPT-4和Google的PaLM2对多语言的支持已经做得很不错了，但这两者都是闭源的，而开源的大语言模型主要有以下痛点无法解决：

* 第一，大多数不能商用。比如Meta开源的LLAMA，以及基于LLAMA衍生的Vicuna等无法商用，只能用于学术研究。清华和智谱AI开源的ChatGLM的模型权重也不能商用。
* 第二，对非英语支持一般。大部分开源模型的训练语料以英文为主，非英文的对话效果一般。然而，世界上有超过80%左右的人是不讲英语的，如何解决这部分人的使用痛点也很关键。

国内很多企业和公司也在调研如何基于开源模型进行微调，打造一个支持中文的大语言模型，应用到自己的业务场景里。

由BigScience开源的Bloom基座模型是很多互联网公司的首选，因为这个模型可商用，支持包包括中文在内的46种语言，而且模型参数够多，有1760亿参数。

有些公司就是直接拿基于Bloom做过微调后的Bloomz模型，来进一步微调，打造一个垂直领域的LLM。

SambaNova和Together联合开源的BLOOMChat，其目的就是打造一个开源的、支持多语言、可商用的LLM，实验表明BLOOMChat对多语言的支持明显优于其它开源模型。

## BLOOMChat

BLOOMChat是在SambaNova提供的AI计算平台RDUs(Reconfigurable Dataflow Units)上进行训练的。

在人类偏好研究中，对于6种语言的测评，相比于GPT-4的54.75%胜率，BLOOMChat获得了45.25%的胜率，弱于GPT-4。

但是，与其它主流的开源聊天LLM相比，它有66%的时间表现更优。

在WMT翻译任务中同样表现出色，领先于其它基于BLOOM的微调模型和其它主流开源聊天模型的结果。

受到先前工作的启发，即在一个语言中进行指令微调可以提升多语言模型在另一种语言中的效果表现，BLOOMChat使用了包括OpenChatKit的OIG、Dolly 2.0和OASST1数据集在内的以英语为主的对话数据集来进行BLOOM（176B）的模型微调。

尽管只在英语上进行了微调，我们观察到BLOOMChat在非英语语言上的聊天质量也得到了显著提高。

## 数据收集



## 训练



## 实验效果



## 总结

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。

## References

* https://sambanova.ai/blog/introducing-bloomchat-176b-the-multilingual-chat-based-llm/
* https://huggingface.co/spaces/sambanovasystems/BLOOMChat
* https://github.com/sambanova/bloomchat
