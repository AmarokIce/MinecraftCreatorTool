![](icon.png) 

## **Minecraft模组开发者小工具**
$状态： 正在更新$

%更新计划%：
- [x] 错误报告过滤消息 [Done]
- [ ] OCR [Doing]
- [x] GIF拆分 [Done]
- [ ] GIF合并 [Doing]
- [ ] 自动更新 [Beta/Doing]
- [ ] Connect With... [MissingNo]
- [ ] Ping Server [MissingNo]


### MinecraftTool
1.[关于](#About)  
2.[外部库](#lib)  

### Other
3.[OCR](#ocr)

### 许可证
4.[许可证](#license)
***

## <span id="About">**关于**</span>
这套Python小工具由Someoneice制作，使用Main时将会以整合形式启动，也可在MinecraftTool文件夹中每个模块单独启动使用。  
这套工具主要效力于ManaMetalMod官方讨论组，以及维护[ManaMetalMod Wiki](https://mana-metal-mod.fandom.com/zh)与[MC百科 ManaMetalMod](https://mcmod.cn/class/1111)页面。欢迎访问我的[个狼博客页](https://ut.snowlyicewolf.club)。  
这套工具提供了以下功能：

* Tick转换
* Model文件夹下Item Json自动输出
* 中文转换Unicode
* 错误报告要点过滤
* 将16x 的动态图片分割帧
* ~~将16x 的帧粘合为gif~~ （正在实现）

***
## <span id=lib>**外部库**</span>
图像处理需要使用到部分库。请放心，我使用的是一些热门且优秀的库，安装这些库也会提高你的工作效率。
若你还没有这些库，可以在lib文件夹中运行GitPIPLib.py文件获取。  
列表如下：  
Numpy : Python数据运算常用库。  
Pillow : Python图像处理常用库。  
MatplotLib : Python数据绘图库。  
OpenCV : Python优质视觉图像处理库。

***
## <span id=ocr>OCR</span>
这是一个为识别ManaMetalMod的更新日志而开发的简单识别。
由于更新日志都为繁体，而现有的各种OCR遇到繁体不是不识别就是错字连天。
因此我决定自己训练一份OCR模型来解决问题。



***
## <span id=license> **开源许可**</span>
这个项目拥有两种许可证，以凤梨许可证为主许可证。
若您无法接受一份自创的，没有法律效应的许可证，您可以选择使用AFL - 3.0许可证。
当然，若您正在使用AFL - 3.0进行衍生开发或别的用途，您可能需要标明您正在使用AFL - 3.0而不是Pineapple。

参见：
[PineappleLICENSE](license.md)
[With AFL - 3.0](LICENSE-AFL)
