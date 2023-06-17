# baichuan-7B: 开源可商用支持中英文的最好大模型

## 背景

baichuan-7B 是由百川智能开发的一个开源可商用的大规模预训练语言模型。

基于 Transformer 结构，在大约1.2万亿 tokens 上训练的70亿参数模型，支持中英双语，上下文窗口长度为4096。

在标准的中文和英文权威 benchmark（C-EVAL/MMLU）上均取得了同参数规模下的最好效果。

## baichuan-7B的优点

- 在同尺寸模型中baichuan-7B达到了目前SOTA的水平。
- baichuan-7B使用自有的中英文双语语料进行训练，在中文上进行优化，在C-Eval达到SOTA水平。
- 不同于LLaMA完全禁止商业使用，baichuan-7B使用更宽松的开源协议，允许用于商业目的。

## 数据收集

- 原始数据包括开源的中英文数据和自行抓取的中文互联网数据，以及部分高质量知识性数据。
- 参考相关数据工作，频率和质量是数据处理环节重点考虑的两个维度。 我们基于启发式规则和质量模型打分，对原始数据集进行篇章和句子粒度的过滤。在全量数据上，利用局部敏感哈希方法，对篇章和句子粒度做滤重。

![img](https://github.com/baichuan-inc/baichuan-7B/raw/main/media/data_process.png)

## 模型结构

整体模型基于标准的 Transformer 结构，采用了和 LLaMA 一样的模型设计。

- 位置编码：rotary-embedding

  是现阶段被大多模型采用的位置编码方案，具有更好的外延效果。虽然训练过程中最大长度为4096，但是实际测试中模型可以很好的扩展到 5000 tokens 上，如下图：

  
  [![img](https://github.com/baichuan-inc/baichuan-7B/raw/main/media/long-context-ppl.png)](https://github.com/baichuan-inc/baichuan-7B/blob/main/media/long-context-ppl.png)

- 激活层：SwiGLU, Feedforward 变化为(8/3)倍的隐含层大小，即11008。

- Layer-Normalization: 基于 [RMSNorm](https://arxiv.org/abs/1910.07467) 的 Pre-Normalization。

## 预训练

采用 DeepSpeed 框架进行训练，在原本的LLaMA框架上进行诸多修改以提升训练时的吞吐，具体包括：

1. 算子优化技术：采用更高效算子，如 Flash-attention，NVIDIA apex 的 RMSNorm 等。
2. 算子切分技术：将部分计算算子进行切分，减小内存峰值。
3. 混合精度技术：降低在不损失模型精度的情况下加速计算过程。
4. 训练容灾技术：训练平台和训练框架联合优化，IaaS + PaaS 实现分钟级的故障定位和任务恢复。
5. 通信优化技术，具体包括：
   1. 采用拓扑感知的集合通信算法，避免网络拥塞问题，提高通信效率。
   2. 根据卡数自适应设置 bucket size，提高带宽利用率。
   3. 根据模型和集群环境，调优通信原语的触发时机，从而将计算和通信重叠。

基于上述的几个优化技术，在千卡A800机器上达到了7B模型182Tflops的吞吐，GPU峰值算力利用率高达58.3% 。

最终的loss如下图：


[![img](https://github.com/baichuan-inc/baichuan-7B/raw/main/media/7b.loss.png)](https://github.com/baichuan-inc/baichuan-7B/blob/main/media/7b.loss.png)

## 实验效果

### C-Eval

[C-Eval 数据集](https://cevalbenchmark.com/index.html)是一个全面的中文基础模型评测数据集，涵盖了52个学科和四个难度的级别。

使用该数据集的dev集作为 few-shot 的来源，在 test 集上进行了 5-shot 测试。

先修改 `evaluate_zh.py` 中的 OPENMODEL_PATH 和 CEVAL_DATA_PATH 两个值，分别是模型（文件夹）存放的路径和 C-Eval 数据集的路径。再执行下面的脚本。

```
shot=5  # few-shot
gpu=0  # 显卡id
split=test  # 评估测试集
model_id=baichuan-7b   # 待评估的模型
task=ceval  # 任务名称：ceval
echo gpu_idx-${gpu}-${model_id}_${task}_${split}_${shot}-shot
nohup python  evaluate_zh.py --gpu_idx ${gpu} --model_id ${model_id} --task ${task} --shot ${shot} --split ${split} --show_detail  > ${model_id}_${task}_${split}_${shot}-shot_record.txt 2>&1 &
```

### 结果

| Model 5-shot                | Average | Avg(Hard) | STEM | Social Sciences | Humanities | Others |
| --------------------------- | ------- | --------- | ---- | --------------- | ---------- | ------ |
| GPT-4                       | 68.7    | 54.9      | 67.1 | 77.6            | 64.5       | 67.8   |
| ChatGPT                     | 54.4    | 41.4      | 52.9 | 61.8            | 50.9       | 53.6   |
| Claude-v1.3                 | 54.2    | 39.0      | 51.9 | 61.7            | 52.1       | 53.7   |
| Claude-instant-v1.0         | 45.9    | 35.5      | 43.1 | 53.8            | 44.2       | 45.4   |
| moss-moon-003-base (16B)    | 27.4    | 24.5      | 27.0 | 29.1            | 27.2       | 26.9   |
| Ziya-LLaMA-13B-pretrain     | 30.2    | 22.7      | 27.7 | 34.4            | 32.0       | 28.9   |
| LLaMA-7B-hf                 | 27.1    | 25.9      | 27.1 | 26.8            | 27.9       | 26.3   |
| ChatGLM-6B                  | 34.5    | 23.1      | 30.4 | 39.6            | 37.4       | 34.5   |
| Falcon-7B                   | 25.8    | 24.3      | 25.8 | 26.0            | 25.8       | 25.6   |
| Open-LLaMA-v2-pretrain (7B) | 24.0    | 22.5      | 23.1 | 25.3            | 25.2       | 23.2   |
| TigerBot-7B-base            | 25.7    | 27.0      | 27.3 | 24.7            | 23.4       | 26.1   |
| Aquila-7B*                  | 25.5    | 25.2      | 25.6 | 24.6            | 25.2       | 26.6   |
| BLOOM-7B                    | 22.8    | 20.2      | 21.8 | 23.3            | 23.9       | 23.3   |
| BLOOMZ-7B                   | 35.7    | 25.8      | 31.3 | 43.5            | 36.6       | 35.6   |
| **baichuan-7B**             | 42.8    | 31.5      | 38.2 | 52.0            | 46.2       | 39.3   |

### Gaokao

[Gaokao](https://github.com/ExpressAI/AI-Gaokao) 是一个以中国高考题作为评测大语言模型能力的数据集，用以评估模型的语言能力和逻辑推理能力。 

只保留了其中的单项选择题，随机划分后对所有模型进行统一 5-shot 测试。

### 结果

以下是测试的结果。

| Model                   | Average   |
| ----------------------- | --------- |
| Open-LLaMA-v2-pretrain  | 21.41     |
| Ziya-LLaMA-13B-pretrain | 23.17     |
| Falcon-7B               | 23.98     |
| TigerBot-7B-base        | 25.94     |
| LLaMA-7B                | 27.81     |
| ChatGLM-6B              | 21.41     |
| BLOOM-7B                | 26.96     |
| BLOOMZ-7B               | 28.72     |
| Aquila-7B*              | 24.39     |
| **baichuan-7B**         | **36.24** |

### AGIEval

[AGIEval](https://github.com/microsoft/AGIEval) 旨在评估模型的认知和解决问题相关的任务中的一般能力。

只保留了其中的四选一单项选择题，随机划分后对所有模型进行了统一5-shot测试。

### 结果

| Model                   | Average   |
| ----------------------- | --------- |
| Open-LLaMA-v2-pretrain  | 23.49     |
| Ziya-LLaMA-13B-pretrain | 27.64     |
| Falcon-7B               | 27.18     |
| TigerBot-7B-base        | 25.19     |
| LLaMA-7B                | 28.17     |
| ChatGLM-6B              | 23.49     |
| BLOOM-7B                | 26.55     |
| BLOOMZ-7B               | 30.27     |
| Aquila-7B*              | 25.58     |
| **baichuan-7B**         | **34.44** |

* 其中 Aquila 模型来源于智源官方网站(https://model.baai.ac.cn/model-detail/100098) 仅做参考

## 英文榜单

除了中文之外，也测试了模型在英文上的效果。

[MMLU](https://arxiv.org/abs/2009.03300) 是包含57个多选任务的英文评测数据集，涵盖了初等数学、美国历史、计算机科学、法律等，难度覆盖高中水平到专家水平，是目前主流的LLM评测数据集。

采用了[开源](https://github.com/hendrycks/test) 的评测方案，最终 5-shot 结果如下所示：

### 结果

| Model                     | Humanities | Social Sciences | STEM     | Other    | Average  |
| ------------------------- | ---------- | --------------- | -------- | -------- | -------- |
| LLaMA-7B2                 | 34.0       | 38.3            | 30.5     | 38.1     | 35.1     |
| Falcon-7B1                | -          | -               | -        | -        | 35.0     |
| mpt-7B1                   | -          | -               | -        | -        | 35.6     |
| ChatGLM-6B0               | 35.4       | 41.0            | 31.3     | 40.5     | 36.9     |
| BLOOM-7B0                 | 25.0       | 24.4            | 26.5     | 26.4     | 25.5     |
| BLOOMZ-7B0                | 31.3       | 42.1            | 34.4     | 39.0     | 36.1     |
| moss-moon-003-base (16B)0 | 24.2       | 22.8            | 22.4     | 24.4     | 23.6     |
| moss-moon-003-sft (16B)0  | 30.5       | 33.8            | 29.3     | 34.4     | 31.9     |
| **baichuan-7B0**          | **38.4**   | **48.9**        | **35.6** | **48.1** | **42.3** |



## 总结

baichuan-7B模型基于标准的 Transformer 结构，采用了和 LLaMA 一样的模型设计，核心优势如下：

- 在同尺寸模型中baichuan-7B达到了目前SOTA的水平。
- baichuan-7B使用自有的中英文双语语料进行训练，在中文上进行优化，在C-Eval达到SOTA水平。
- 不同于LLaMA完全禁止商业使用，baichuan-7B使用更宽松的开源协议，允许用于商业目的。

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，了解所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://github.com/baichuan-inc/baichuan-7B
* https://huggingface.co/baichuan-inc/baichuan-7B

