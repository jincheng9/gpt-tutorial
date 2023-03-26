# **注册ChatGPT详细指南**

最近ChatGPT真受欢迎，但是有些人注册时会经常面临不服务它们的地区问题，现在我们给你详细问题解决。

作者 [twitter](https://twitter.com/BoxMrChen)

## **准备**

1. 代理。要求是韩国，日本，印度，新加坡，美国这些国家的地址都合适。对其他的我们还不太清楚，反正香港或中国的代理肯定不行。
2. 找一个国外手机号码，如果你没有用过接码平台也行，有些接码平台是无法接的，所以我们推荐一个就是 [sms-activate.org](https://sms-activate.org/?ref=2068197)
3. 准备一个浏览器

## **开始一步一步注册**

### **第一步是接验证码**

打开接码平台 [sms-activate.org](https://sms-activate.org/?ref=2068197)，注册一个账号



![img](https://lh6.googleusercontent.com/cMeZQKgY35Bnn9cqLhmZuNP4wYfgawEmklF8HfGU6vAXCsIN8WnpmZ4zwEq3lhi116Gw9epgJOGyDjVLET0skBytiuT41ZGa08crSpt1yh6gnpCni-JJjSmPYiFTj9csfrgDStp3iANCPsbHcToModOOSUvhQzQFQtdziT6A6QzMjXez82OcaIQu5h1iCA)

 

然后要充值余额



![充值，这里单位是卢布](https://lh5.googleusercontent.com/yVgQqWlnP3Rk0thUlNUP7SAtU66CTD1L4HRHm5KhC_ZSfy0PdY1ANoLJRE_NRRttSCyGdBuR2WprtzCfbbyrXJ4oY99QCg4fg8lH2GbPAYc9GcZ33hPSRirWq1nFhPytxkeJ4VQgvpQlMFNDnw3RAdWcgwK-QXXPh-JqcdRE-ofSl5CM_UZDOm1o2GvWuA)

一次接码OpenAi的验证码费用是大概11卢布，人民币来看差不多是1块钱，不过只能充美金，就先充直个1美金钱。可以选择对你任何方便方式。支付宝也有

![img](https://lh3.googleusercontent.com/g7fMxTmyZN6gl2uY0ZYdWebtbwrOZz7mEtdM3h1WwNGJxMcOVEeASgWk_qHmUYh68nRZ8mTuS5Wm7ZPvm8iAlDP8ChF6fDQZtLJYurScOr0SU8thZP9BKYwMPoRoMdg3OSksBQo_Z01Cxaun2knKymAItvkI51Uz8I9fZoRvDocoDD8jph-E0iJuZtLK3Q)

充值完成可能需要等一会，就先放着，直接进行下一步。

## **第二部是注册一个OpenAI账号**

首先打开[ChatGPT的账户注册页面](https://beta.openai.com/signup)。谷歌注册或者邮箱注册都可以，无所谓，我们这里用邮箱注册作为例子。

![img](https://lh4.googleusercontent.com/5FAoNOuw0v992RG1BreZuHjLJv1TpWYSs8Vk8nfTI4YnuKKgO-54rRHromwVnwjXGvHhdoDj0Lu_yjH2E4G4lOV2pvlgC1G-5g6SpvrVGnoxz6yQWtBiryWutOymCtW2UuHzEooXF1O-ilKMdBknLtEskP3MeaI1RZavvrDCXweIUnhdJ8t6eN1vjFoP3Q)

用邮箱注册后你要验证邮件。进去邮箱，查看email里的链接。

 

![img](https://lh6.googleusercontent.com/8bcYtPuGvpYcfLzGqi4uF1cHeuiYRW0zYwTUc5EX--LVenBC0iDtpp00UWxbvk7aJAyW08RIhpArfDORzd8N8Eko6fK7prIZxBGEcZmYZ6NlAInYo9mls9S85R-rdsos4joQfLS0-l15GIvblEyXLc3jzoht24aecm-m9CeZIui76iZX3FOWapRuigyYYQ)

这里你需要输入需要的信息。

当然，有一些人会在这里遇到一个问题，会出现说不能在当前国家服务的提示。

 

![不用怕，我写这文章就是为了解决这个问题](https://lh5.googleusercontent.com/7R1aY59o0MNxWmlONV5KktskGbifyEAP9cn2zYxxvIMkKO5bpaLtAo-76iHN0yPcL413dUxHytKI2hOgFzDi2SShQ60NrEdhhjNTUcjKUtf3xYFNBaiDe3yDdWH90gBmDoQRuVuz3fsNuQaVxUiPqlVWYULR3dAyOB35C2MmT3kOVfWk5fMOty0MUSZ48A)

不用怕，这个这文章就帮助你解决这个问题。

这方面那，给你一招。一般你出现这种问题，就是因为你的代理没有全局，或者位置不对。香港或中国的的代理是100%无法通过的。

这个问题是非常神奇的，只要你出现了这个提示，那么你接下来怎么切换代理，都是没用的。现在提供给你你一招解决。

## **解决地区问题**

先，你要把你的代理切换到任何合适的地区，我们这里选择了韩国。

然后，先复制下面这段代码

window.localStorage.removeItem(Object.keys(window.localStorage).find(i=>i.startsWith('@@auth0spajs')))

接着在地址栏里输入

javascript:



请注意，这里一定要输入，因为你复制的话是粘贴不了的。

然后再粘贴我们第一段复制的内容：

![img](https://lh6.googleusercontent.com/nZPZ-jlp6ZW_4DH6YpIPFJJGsL6Dz6g2_P3JcGlg8C18mvcmLSLC3FKI7cVeSLe-A0yq_8IdlocOGcmPmF0f7K-IHlQZSWekYbyi6kZXAbMC_mSovCG58f5EQuhDLydd9PWCf3eM47A2YNY790U11ka0Qw1PYUuhL3LyTnegsRRuMc9aTzX8FifLl2WOZg)

然后按下回车键，刷新页面。如果你的代理没问题，就可以看到正常工作的注册页面了。

## **输入手机号码**

 

![img](https://lh5.googleusercontent.com/-P8__DqW8L2ALL1R-prXR67miAndgWSKd1nyRVX6GIOLqqBM-pIYr9-ItBB4Y-dvbK4IsVomBl7ZLrHr60rkJIPh6ra1293C7CNKIgNGo0nRChZQSH4BnAtJ1IZfjJRZDhGnfNp_aGlo_O46QOChyz5REw0Xu3nOP2yqJSQmKRXbIP1xaWhiVmlAHtXE3g)

这里选的是韩国，这是因为我们使用韩国的代理，但是我们最好选择印度。然后到我们的接码网站上去。在左侧搜索OpenAi，然后点击印度。

![img](https://lh6.googleusercontent.com/CF_2ilYYa3bJndavHZkG2CRuKOIBnI_pRd7ljOik61P42vHUdfGN-yOautzgUI9Jty04jdoqf9tOQdsAfSlqKDO-SQwyrzS9JvriuPwO3UD7MlMJgbZi_E4M76FhzcL8X5zz8HewvTtwOCHziihUKESUovjR2f8pVg5QYF5gVWxCIOpJJ5NhKP2uruGrJA)

 

点击”小黄车”。

 

![img](https://lh5.googleusercontent.com/DSqE8eZhRe_v_jftZH4nf7KN74jL5ll3WqWeVQHd3EznubDpdsb2Tp9iI5R8dRtF9ZTlG5hZw2vaP3ihm-Ottk-1Yf6NSku7jdYAEM6APR8HwuLZbF_6dVe6uvtN0Ay9NlqhWiPyhnpeFkXnlsBXWPBA006_Li5SeuIzLLrceyTVw_ja71xCLaqK3v3HDw)

然后我们复制这个号码，粘贴过去。然后我们点击发送验证码就完成了。

等一会网站会提示验证码，我们复制粘贴。

![img](https://lh6.googleusercontent.com/8kNrQqyAtxmiDIo6YQaTLCoBDDFxW03ItyirJ__fbjTTplvE_9ZCfs3B83Q2jenNPp2be8WgBiimx8RUMQOGjS0lcOEM_xj0Yn6Ghslx223QALm-hnTKU399CzkVk55Fq6jASaoVuUXXiQIp_BW8sKXerdtaipDKuoO-QzPPBxMsgk9EZXhINlGSnHe7wg)

这里你要选择你打算如何使用OpenAI。随便选择吧。

## **使用ChatGPT**

注册完后，打开[ChatGPT网站](https://chat.openai.com/auth/login)去登陆。

![img](https://lh3.googleusercontent.com/6ZdsiN3icfui0AdbF5_D5gRsK6BGlNBbNYusO4jrPHzZOJYov0zE9qukPwlA1jmGET4og0s9oYlZ0cHtaM1Ty8nW9BpnHxf14SZ9Jkq7NrgTfYC7qwx8fl4IpRykNdcRic4dAiQ3c_VRrLe8E7MNdZEAf9prceEdOAd6btO5FiWDOXt8VTu0PJz8Iq69Cg)

在下面这个地方就可以开始写你的任何巧妙的句子了。取乐吧！



## References

* **注册ChatGPT详细指南**

最近ChatGPT真受欢迎，但是有些人注册时会经常面临不服务它们的地区问题，现在我们给你详细问题解决。

作者 [twitter](https://twitter.com/BoxMrChen)

## **准备**

1. 代理。要求是韩国，日本，印度，新加坡，美国这些国家的地址都合适。对其他的我们还不太清楚，反正香港或中国的代理肯定不行。
2. 找一个国外手机号码，如果你没有用过接码平台也行，有些接码平台是无法接的，所以我们推荐一个就是 [sms-activate.org](https://sms-activate.org/?ref=2068197)
3. 准备一个浏览器

## **开始一步一步注册**

### **第一步是接验证码**

打开接码平台 [sms-activate.org](https://sms-activate.org/?ref=2068197)，注册一个账号



![img](https://lh6.googleusercontent.com/cMeZQKgY35Bnn9cqLhmZuNP4wYfgawEmklF8HfGU6vAXCsIN8WnpmZ4zwEq3lhi116Gw9epgJOGyDjVLET0skBytiuT41ZGa08crSpt1yh6gnpCni-JJjSmPYiFTj9csfrgDStp3iANCPsbHcToModOOSUvhQzQFQtdziT6A6QzMjXez82OcaIQu5h1iCA)

 

然后要充值余额



![充值，这里单位是卢布](https://lh5.googleusercontent.com/yVgQqWlnP3Rk0thUlNUP7SAtU66CTD1L4HRHm5KhC_ZSfy0PdY1ANoLJRE_NRRttSCyGdBuR2WprtzCfbbyrXJ4oY99QCg4fg8lH2GbPAYc9GcZ33hPSRirWq1nFhPytxkeJ4VQgvpQlMFNDnw3RAdWcgwK-QXXPh-JqcdRE-ofSl5CM_UZDOm1o2GvWuA)

一次接码OpenAi的验证码费用是大概11卢布，人民币来看差不多是1块钱，不过只能充美金，就先充直个1美金钱。可以选择对你任何方便方式。支付宝也有

![img](https://lh3.googleusercontent.com/g7fMxTmyZN6gl2uY0ZYdWebtbwrOZz7mEtdM3h1WwNGJxMcOVEeASgWk_qHmUYh68nRZ8mTuS5Wm7ZPvm8iAlDP8ChF6fDQZtLJYurScOr0SU8thZP9BKYwMPoRoMdg3OSksBQo_Z01Cxaun2knKymAItvkI51Uz8I9fZoRvDocoDD8jph-E0iJuZtLK3Q)

充值完成可能需要等一会，就先放着，直接进行下一步。

## **第二部是注册一个OpenAI账号**

首先打开[ChatGPT的账户注册页面](https://beta.openai.com/signup)。谷歌注册或者邮箱注册都可以，无所谓，我们这里用邮箱注册作为例子。

![img](https://lh4.googleusercontent.com/5FAoNOuw0v992RG1BreZuHjLJv1TpWYSs8Vk8nfTI4YnuKKgO-54rRHromwVnwjXGvHhdoDj0Lu_yjH2E4G4lOV2pvlgC1G-5g6SpvrVGnoxz6yQWtBiryWutOymCtW2UuHzEooXF1O-ilKMdBknLtEskP3MeaI1RZavvrDCXweIUnhdJ8t6eN1vjFoP3Q)

用邮箱注册后你要验证邮件。进去邮箱，查看email里的链接。

 

![img](https://lh6.googleusercontent.com/8bcYtPuGvpYcfLzGqi4uF1cHeuiYRW0zYwTUc5EX--LVenBC0iDtpp00UWxbvk7aJAyW08RIhpArfDORzd8N8Eko6fK7prIZxBGEcZmYZ6NlAInYo9mls9S85R-rdsos4joQfLS0-l15GIvblEyXLc3jzoht24aecm-m9CeZIui76iZX3FOWapRuigyYYQ)

这里你需要输入需要的信息。

当然，有一些人会在这里遇到一个问题，会出现说不能在当前国家服务的提示。

 

![不用怕，我写这文章就是为了解决这个问题](https://lh5.googleusercontent.com/7R1aY59o0MNxWmlONV5KktskGbifyEAP9cn2zYxxvIMkKO5bpaLtAo-76iHN0yPcL413dUxHytKI2hOgFzDi2SShQ60NrEdhhjNTUcjKUtf3xYFNBaiDe3yDdWH90gBmDoQRuVuz3fsNuQaVxUiPqlVWYULR3dAyOB35C2MmT3kOVfWk5fMOty0MUSZ48A)

不用怕，这个这文章就帮助你解决这个问题。

这方面那，给你一招。一般你出现这种问题，就是因为你的代理没有全局，或者位置不对。香港或中国的的代理是100%无法通过的。

这个问题是非常神奇的，只要你出现了这个提示，那么你接下来怎么切换代理，都是没用的。现在提供给你你一招解决。

## **解决地区问题**

先，你要把你的代理切换到任何合适的地区，我们这里选择了韩国。

然后，先复制下面这段代码

window.localStorage.removeItem(Object.keys(window.localStorage).find(i=>i.startsWith('@@auth0spajs')))

接着在地址栏里输入

javascript:



请注意，这里一定要输入，因为你复制的话是粘贴不了的。

然后再粘贴我们第一段复制的内容：

![img](https://lh6.googleusercontent.com/nZPZ-jlp6ZW_4DH6YpIPFJJGsL6Dz6g2_P3JcGlg8C18mvcmLSLC3FKI7cVeSLe-A0yq_8IdlocOGcmPmF0f7K-IHlQZSWekYbyi6kZXAbMC_mSovCG58f5EQuhDLydd9PWCf3eM47A2YNY790U11ka0Qw1PYUuhL3LyTnegsRRuMc9aTzX8FifLl2WOZg)

然后按下回车键，刷新页面。如果你的代理没问题，就可以看到正常工作的注册页面了。

## **输入手机号码**

 

![img](https://lh5.googleusercontent.com/-P8__DqW8L2ALL1R-prXR67miAndgWSKd1nyRVX6GIOLqqBM-pIYr9-ItBB4Y-dvbK4IsVomBl7ZLrHr60rkJIPh6ra1293C7CNKIgNGo0nRChZQSH4BnAtJ1IZfjJRZDhGnfNp_aGlo_O46QOChyz5REw0Xu3nOP2yqJSQmKRXbIP1xaWhiVmlAHtXE3g)

这里选的是韩国，这是因为我们使用韩国的代理，但是我们最好选择印度。然后到我们的接码网站上去。在左侧搜索OpenAi，然后点击印度。

![img](https://lh6.googleusercontent.com/CF_2ilYYa3bJndavHZkG2CRuKOIBnI_pRd7ljOik61P42vHUdfGN-yOautzgUI9Jty04jdoqf9tOQdsAfSlqKDO-SQwyrzS9JvriuPwO3UD7MlMJgbZi_E4M76FhzcL8X5zz8HewvTtwOCHziihUKESUovjR2f8pVg5QYF5gVWxCIOpJJ5NhKP2uruGrJA)

 

点击”小黄车”。

 

![img](https://lh5.googleusercontent.com/DSqE8eZhRe_v_jftZH4nf7KN74jL5ll3WqWeVQHd3EznubDpdsb2Tp9iI5R8dRtF9ZTlG5hZw2vaP3ihm-Ottk-1Yf6NSku7jdYAEM6APR8HwuLZbF_6dVe6uvtN0Ay9NlqhWiPyhnpeFkXnlsBXWPBA006_Li5SeuIzLLrceyTVw_ja71xCLaqK3v3HDw)

然后我们复制这个号码，粘贴过去。然后我们点击发送验证码就完成了。

等一会网站会提示验证码，我们复制粘贴。

![img](https://lh6.googleusercontent.com/8kNrQqyAtxmiDIo6YQaTLCoBDDFxW03ItyirJ__fbjTTplvE_9ZCfs3B83Q2jenNPp2be8WgBiimx8RUMQOGjS0lcOEM_xj0Yn6Ghslx223QALm-hnTKU399CzkVk55Fq6jASaoVuUXXiQIp_BW8sKXerdtaipDKuoO-QzPPBxMsgk9EZXhINlGSnHe7wg)

这里你要选择你打算如何使用OpenAI。随便选择吧。

## **使用ChatGPT**

注册完后，打开[ChatGPT网站](https://chat.openai.com/auth/login)去登陆。

![img](https://lh3.googleusercontent.com/6ZdsiN3icfui0AdbF5_D5gRsK6BGlNBbNYusO4jrPHzZOJYov0zE9qukPwlA1jmGET4og0s9oYlZ0cHtaM1Ty8nW9BpnHxf14SZ9Jkq7NrgTfYC7qwx8fl4IpRykNdcRic4dAiQ3c_VRrLe8E7MNdZEAf9prceEdOAd6btO5FiWDOXt8VTu0PJz8Iq69Cg)

在下面这个地方就可以开始写你的任何巧妙的句子了。取乐吧！

## References

* https://sms-activate.org/cn/info/ChatGPT