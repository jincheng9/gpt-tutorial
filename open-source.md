## 开源大语言模型

| Model      | 作者                                        | 参数量                                          | 训练数据量 | 训练成本                                                     | 推理成本                                                     |
| :--------- | ------------------------------------------- | ----------------------------------------------- | ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| LLaMA      | Meta                                        | 包括 70 亿、130 亿、330 亿、650 亿 4 种参数规模 |            |                                                              |                                                              |
| Alpaca     | Stanford                                    | 70亿                                            |            |                                                              |                                                              |
| Vicuna     | UC Berkeley, CMU, Stanford, UCSD and MBZUAI | 130亿                                           |            |                                                              |                                                              |
| Koala      | UC Berkeley                                 | 130亿                                           |            | 一台 Nvidia DGX 服务器与8个A100 GPU，需要6个小时训练完成2个epochs。在公共云计算平台上，预期训练成本不超过100美元。 |                                                              |
| Dolly 2.0  | Databricks                                  | 120亿                                           |            |                                                              |                                                              |
| ChatGLM    | 清华大学KEG 实验室和智谱AI                  | 1300亿                                          |            |                                                              | 支持在一台 **A100（40G \* 8）** 或 **V100（32G \* 8）服务器**上对千亿规模参数的模型进行推理 |
| 鹏程·盘古α | 鹏程实验室、华为、北大                      | 2000亿                                          |            |                                                              |                                                              |

Alpaca, Vicuna, Koala都是基于LLaMA衍生而来的，LLaMA目前仅用于学术、社会公益项目，不能用于商业化项目。



## 术语

RLHF: Reinforcement Learning from Human Feedback

LLM: Large Language Model

## References

* https://medium.com/geekculture/list-of-open-sourced-fine-tuned-large-language-models-llm-8d95a2e0dc76
* https://arxiv.org/pdf/2303.18223.pdf
* https://mp.weixin.qq.com/s/_9JevS70pRqEmPRbVVM9Vw