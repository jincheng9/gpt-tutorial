# OpenAI发布重磅新模型再次遥遥领先

## 背景

OpenAI在2024年2月16日发布了史上最强大的文生视频模型Sora。

这是继文生文模型(ChatGPT)、文生图模型(DALL·E 3)后，OpenAI在一个更有挑战性的文生视频(text-to-video)领域再次遥遥领先。

![](../img/sora_vs.png) 

诸如Pika、Runway等文生视频领域的创业公司很可能要面临生存危机了。

## Sora强大之处

Sora能够生成长达一分钟的视频，在生成视频的时长上秒杀同类模型，同时保证高质量的视觉效果，以及严格遵循用户的提示词(Prompt)。

Sora能够生成包含多个角色、特定类型的动作、以及主题和背景的准确细节的复杂场景。Sora模型不仅理解用户在提示词中要求的内容，还理解这些事物在物理世界中的存在方式。

Sora模型对语言有着深刻的理解，使其能够准确解释提示词，并生成表达丰富情感的引人入胜的角色。Sora还可以在单个生成的视频中创建多个镜头，准确地保持角色和视觉风格的连贯性。

下面就让我们来见识下Sora的威力吧：

### 提示词1：

Prompt:  一位时尚的女士穿着黑色皮夹克、一条长红裙和黑色靴子，在充满温暖发光霓虹和动态城市标识的东京街道上行走。

<video controls>
  <source src="https://cdn.openai.com/sora/videos/tokyo-walk.mp4" type="video/mp4">
  您的浏览器不支持视频标签。
</video>

### 提示词2：

Prompt: 几只巨大的长毛猛犸象踏过雪地草原接近，它们长长的毛皮在风中轻轻飘扬，远处覆盖着雪的树木和壮观的雪顶山峰，午后的阳光透过稀疏的云层，远处的太阳高悬，营造出温暖的光芒，低角度的摄影视角令人惊叹，以美丽的摄影技术捕捉到这种大型毛茸茸的哺乳动物，效果出众。

<video controls>
  <source src="https://cdn.openai.com/sora/videos/wooly-mammoth.mp4" type="video/mp4">
  您的浏览器不支持视频标签。
</video>

### 提示词3：

Prompt: 电影预告片展示了一位30岁的太空人的冒险，他戴着一顶红色羊毛编织的摩托车头盔，在蓝天和盐漠之下，采用电影风格，使用35mm胶片拍摄，色彩鲜艳。

<video controls>
  <source src="https://cdn.openai.com/sora/videos/mitten-astronaut.mp4" type="video/mp4">
  您的浏览器不支持视频标签。
</video>

看到这里，有没有感觉到非常震撼，简单几句提示词就可以生成画面质量如此高的AI视频，很多产业和创业公司都要被颠覆了。



## Sora的局限性

当然，官方承认Sora模型目前有一些缺陷。

* 局限一：Sora在精确模拟复杂画面和理解画面的前因后果上还存在缺陷。

  例如，有可能当前你看到的画面里有一个人咬了一口饼干，但是在接下来的花面里这个饼干却没有被咬的痕迹了。

* 局限二：Sora可能还会混淆提示词(Prompt)的空间细节，例如把左右搞反，而且在处理随时间发生的事件的精确描述上可能会遇到困难，比如遵循特定的相机轨迹。

下面的视频就能看出局限性：

Prompt: 五只灰色的狼崽在一条偏远的碎石路上嬉戏追逐，周围是草地。小狼们奔跑和跳跃，相互追逐，咬着对方，玩耍着。

<video controls>
  <source src="https://cdn.openai.com/sora/videos/puppy-cloning.mp4" type="video/mp4">
  您的浏览器不支持视频标签。
</video>

## Sora如何使用

Sora目前只开放了内测给少数群体，比如视觉艺术家、设计师和电影从业人员等。

期待Sora正式开放以及支持API接入的那一天的到来。

## 技术细节

OpenAI也公布了Sora大致实现的技术细节：Sora在视频数据上进行大规模生成模型训练，使用了Transformer架构。

Sora将视频和图像表示为被称为补丁(patches)的较小数据单元的集合，每个patch类似于ChatGPT里的Token。Sora对不同时长、不同分辨率和不同宽高比的视频和图像数据进行了联合训练，使用了文本条件扩散模型。

Sora能够生成高保真度的一分钟视频。测试的结果表明，扩大视频生成模型的规模是朝着构建物理世界通用模拟器迈进的一个有希望的技术实现路径。

详细技术报告可以参考：https://openai.com/research/video-generation-models-as-world-simulators

## 总结

文章和示例代码开源在GitHub: [GPT实战教程](https://github.com/jincheng9/gpt-tutorial)，可以看到所有主流的开源LLM。

公众号：coding进阶。关注公众号可以获取最新GPT实战内容。

个人网站：[Jincheng's Blog](https://jincheng9.github.io/)。

知乎：[无忌](https://www.zhihu.com/people/thucuhkwuji)。



## References

* https://openai.com/sora

* https://openai.com/research/video-generation-models-as-world-simulators
