# ChatGPT Tutorial

* [Lecutre 1: ChatGPT账号注册](./lecture01.md)
* [Lecture 2: 基本概念和常用工具](./lecture02.md)
* [Lecture 3: 收费说明](./lecture03.md)
* [Lecture 4: ChatGPT API帮助手册](./lecture04.md)
* [FAQ: 常见问题](./chatgpt_faq.md)
* [ChatGPT API重大升级](./chatgpt/blog01.md)
* [GPT-4 API全面开放使用](./chatgpt/blog02.md)
* [ChatGPT最佳实践系列-第1篇](./chatgpt/blog03.md)
* [ChatGPT最佳实践系列-第2篇](./chatgpt/blog04.md)
* [ChatGPT最佳实践系列-第3篇](./chatgpt/blog05.md)
* [ChatGPT最佳实践系列-第4篇](./chatgpt/blog06.md)
* [ChatGPT最佳实践系列-第5篇](./chatgpt/blog07.md)
* [ChatGPT最佳实践系列-第6篇](./chatgpt/blog08.md)
* [ChatGPT最佳实践系列-第7篇](./chatgpt/blog09.md)
* [OpenAI在寻找数据合作伙伴啦](./chatgpt/blog10.md)
* [一文读懂GPT Store](./chatgpt/blog11.md)
* [OpenAI发布ChatGPT Team](./chatgpt/blog12.md)
* [OpenAI发布新的embedding模型和API更新](./chatgpt/blog13.md)
* [OpenAI发布史上最强大的文生视频模型Sora](./chatgpt/blog14.md)



# 文心一言

* [Lecture1: 文心一言网站使用和API使用申请](./baidu/lecture01.md)



# 模型多模态能力

| 模型               | 能力                                           | 备注                                                         |
| ------------------ | ---------------------------------------------- | ------------------------------------------------------------ |
| GPT-4o             | 输入：文、图、音频、视频<br>输出：文、图、音频 | API目前(2024.05.18)只能使用GPT-4o的文->文和图->文能力<br>https://openai.com/index/hello-gpt-4o/ |
| GPT-4 Turbo、GPT-4 | 文->文、图->文                                 | chat completions API支持图片作为input                        |
| GPT-3.5            | 文->文                                         | 不支持 图->文                                                |
| DALL.E 3           | 文->图                                         | 暂时不支持图生图                                             |
| DALL.E 2           | 文->图、图->图                                 | DALL.E 2有图片编辑或者生成已有图片变种的功能                 |
| TTS                | 文 -> 音频                                     |                                                              |
| Whisper            | 音频->文                                       |                                                              |

OpenAI每个API支持哪些模型可以参考如下官方说明：

https://platform.openai.com/docs/models/model-endpoint-compatibility

比如文生图的API `/v1/images/generations`只支持DALL.E 3和DALL.E 2这2个模型，图片编辑API `v1/images/edits`和图片变种API `v1/images/variations`只支持DALL.E 2模型。



# 主要玩家

海外大模型主要玩家：

* OpenAI: GPT
* Google: Gemini 
* Meta: LLAMA
* Anthropic: Claude

在比较模型能力的时候，海外主要对标这几家公司的大模型



## 开源模型

| Model            | 作者                                        | 参数量                                          | 训练数据量(tokens)                                           | 训练成本                                                     | 对中英文的支持 |
| :--------------- | ------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | -------------- |
| Llama-1          | Meta                                        | 包括 70 亿、130 亿、330 亿、650 亿 4 种参数规模 | 1.4万亿                                                      | 2048个A100 GPU                                               | 中英文         |
| Alpaca           | Stanford                                    | 70亿                                            | 52k条问答指令数据，指令数据来源于OpenAI的API返回结果         | 500美元数据成本+100美元训练成本                              | 中英文         |
| Vicuna           | UC Berkeley, CMU, Stanford, UCSD and MBZUAI | 130亿                                           | 70k条问答指令数据，指令数据来源于用户分享出来的对话记录      | 300美元                                                      | 中英文         |
| Koala            | UC Berkeley                                 | 130亿                                           | 500k条问答直录功能数据，指令数据来源于网上公开数据集         | 在公共云计算平台上，预期训练成本不超过100美元。一台 Nvidia DGX 服务器与8个A100 GPU，需要6个小时训练完成2个epochs。 | 中英文         |
| Llama-2          | Meta                                        | 70亿、130亿和700亿参数规模                      | 2万亿                                                        | A100集群                                                     | 中英文         |
| Bloom            | BigScience                                  | 1760亿                                          | 3660亿                                                       | 384 80GB A100 GPUs 训练3.5个月[数据来源](https://huggingface.co/blog/bloom-megatron-deepspeed) |                |
| Bloomz           |                                             | 1760亿                                          |                                                              |                                                              |                |
| BLOOMChat        | SambaNova and Together                      | 1760亿                                          | [OIG](https://huggingface.co/datasets/laion/OIG) from [OpenChatKit](https://www.together.xyz/blog/openchatkit) , [Dolly 2.0](https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm), and [OASST1](https://huggingface.co/datasets/OpenAssistant/oasst1) datasets | 基于Bloom在指定数据集上做fine tune                           | 中英文         |
| StableLM         | Stability AI                                | 30亿、70亿、150亿和300亿                        | 1.5万亿                                                      | 未公布                                                       | 英文           |
| Dolly 2.0        | Databricks                                  | 120亿                                           | 15k条问答指令数据，指令数据来源于Databricks员工              | 不到30美元                                                   |                |
| ChatGLM/ChatGLM2 | 清华大学KEG 实验室和智谱AI                  | 60亿和1300亿共2种参数规模                       | 4000亿左右，中文和英文token各2000亿                          | 数百万人民币                                                 | 中英文         |
| 鹏程·盘古α       | 鹏程实验室、华为                            | 26亿、130亿和2000亿共3种参数规模                | 2500亿                                                       | 2048 块昇腾处理器                                            | 中英文         |
| MOSS             | 复旦                                        | 160亿参数                                       | 约7000亿中英文                                               | 未公布。整体技术偏弱一些，暂时无法和ChatGLM相比。            | 中英文         |
| MPT              | Mosaic ML                                   | 70亿参数                                        | 1万亿                                                        | 20万美金，训练9.5天，[详细介绍](https://www.mosaicml.com/blog/mpt-7b) |                |
| baichuan-7B      | Baichuan-Inc                                | 70亿参数                                        | 1.2万亿                                                      | 千卡A800集群，成本未知                                       | 中英文         |
| baichuan-13B     | Baichuan-Inc                                | 130亿参数                                       | 1.4万亿                                                      | 千卡A800集群，成本未知                                       | 中英文         |

* Alpaca, Vicuna, Koala都是基于Llama-1衍生而来的，Llama-1目前仅用于学术、社会公益项目，不能用于商业化项目。
* Llama-2不仅可以用于学术研究，还可以用于商业化。
* Dolly 2.0是基于15k指令数据做fine-tune，其依赖的base model是 [EleutherAI’s](https://www.eleuther.ai/) [Pythia-12b](https://huggingface.co/EleutherAI/pythia-12b)。
* MPT-7B可商用。
* baichuan-7B和baichuan-13B可商用，支持中英文。
* ChatGLM和ChatGLM2可以商用。



# 开源大语言模型

* [BLOOMChat: a New Open Multilingual Chat LLM](./open-source-llm-article/llm0-bloomchat.md)
* [轩辕：首个千亿级中文金融对话模型](./open-source-llm-article/llm1-xuanyuan.md)
* [baichuan-7B: 开源可商用支持中英文的最佳大模型](./open-source-llm-article/llm2-baichuan7b.md)



## AI知识

* [Nvidia GPU显卡有哪些型号](./gpu/gpu0-nvidia.md)



## References

* https://medium.com/geekculture/list-of-open-sourced-fine-tuned-large-language-models-llm-8d95a2e0dc76
* https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard
