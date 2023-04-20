# GPT Tutorial

* [Lecutre 1: ChatGPT账号注册](./lecture01.md)
* [Lecture 2: 基本概念和常用工具](./lecture02.md)
* [Lecture 3: 收费说明](./lecture03.md)
* [Lecture 4: ChatGPT API帮助手册](./lecture04.md)
* [FAQ: 常见问题](./chatgpt_faq.md)



# 文心一言

* [Lecture1: 文心一言网站使用和API使用申请](./baidu/lecture01.md)



## 开源模型

| Model      | 作者                                        | 参数量                                          | 训练数据量(tokens)                                      | 训练成本                                                     |
| :--------- | ------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------ |
| LLaMA      | Meta                                        | 包括 70 亿、130 亿、330 亿、650 亿 4 种参数规模 | 1.4万亿                                                 | 2048个A100 GPU                                               |
| Alpaca     | Stanford                                    | 70亿                                            | 52k条问答指令数据，指令数据来源于OpenAI的API返回结果    | 500美元数据成本+100美元训练成本                              |
| Vicuna     | UC Berkeley, CMU, Stanford, UCSD and MBZUAI | 130亿                                           | 70k条问答指令数据，指令数据来源于用户分享出来的对话记录 | 300美元                                                      |
| Koala      | UC Berkeley                                 | 130亿                                           | 500k条问答直录功能数据，指令数据来源于网上公开数据集    | 在公共云计算平台上，预期训练成本不超过100美元。一台 Nvidia DGX 服务器与8个A100 GPU，需要6个小时训练完成2个epochs。 |
| Bloom      | BigScience                                  | 1760亿                                          | 3660亿                                                  | 384 80GB A100 GPUs 训练3.5个月[数据来源](https://huggingface.co/blog/bloom-megatron-deepspeed) |
| Dolly 2.0  | Databricks                                  | 120亿                                           | 15k条问答指令数据，指令数据来源于Databricks员工         | 不到30美元                                                   |
| ChatGLM    | 清华大学KEG 实验室和智谱AI                  | 60亿和1300亿共2种参数规模                       | 4000亿左右，中文和英文token各2000亿                     | 数百万人民币                                                 |
| 鹏程·盘古α | 鹏程实验室、华为                            | 26亿、130亿和2000亿共3种参数规模                | 2500亿                                                  | 2048 块昇腾处理器                                            |

Alpaca, Vicuna, Koala都是基于LLaMA衍生而来的，LLaMA目前仅用于学术、社会公益项目，不能用于商业化项目。

* [开源模型汇总](./open-source.md)
