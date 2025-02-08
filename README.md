<div align="center">
<h1>Phi-GetSession-python</h1>
使用python实现的phigros获取sessionToken操作喵<br>
注意本项目已经猫化了喵，带有大量喵元素喵，介意者勿用喵！<br><br>

[![Github仓库喵](https://img.shields.io/badge/github-Phi--GS--py-red?style=for-the-badge&logo=Github)](https://github.com/wms26/Phi-GetSession-python)

<img src="https://counter.seku.su/cmoe?name=phi-gs-py&theme=r34" title="喵喵喵~"/><br>

[![Phi-LocalAction-python](https://img.shields.io/badge/Github-LocalAction(本地数据操作)-red?style=for-the-badge&logo=Github)](https://github.com/wms26/Phi-LocalAction-python)
[![Phi-CloudAction-python](https://img.shields.io/badge/Github-CloudAction(云端数据操作)-red?style=for-the-badge&logo=Github)](https://github.com/wms26/Phi-LocalAction-python)

[![PhigrosLibrary](https://img.shields.io/badge/yt6983138-PhigrosLibraryCSharp-blue?style=for-the-badge&logo=Github)](https://github.com/yt6983138/PhigrosLibraryCSharp/)

</div>

# 近期繁忙，本项目将会保持极低频率的更新喵（

## 声明喵：

**本项目仅作为学习参考用，请勿用作违法用途喵！(虽然我也想不到能做什么违法的事情就是了喵)**

**编写本项目所需的资料和资源均源于互联网收集喵(所以本人就是一个废物，什么都要依靠互联网喵(bushi))**

**本项目的初衷仅仅是为了供学习参考使用，本人从未想过要破坏音游圈的游戏平衡喵！**

**请勿尝试滥用本项目！已加检测，请不要试图做出任何商业行为！否则统一纳入黑名单！(此条声明可能与GPLv3许可证存在冲突，请以README.md中本声明为准！)**

**对于本项目本喵拥有最终解释权！请不要做出让任何一个音游玩家都会十分反感的事情！**

**如果你认为本项目不应该存在或者有其他问题，可以提交Issues或者发送邮件到qianqi26@616.sb，我时不时会去查看邮箱喵~**

**Emmm...对于本项目有建议或者问题的请提交Issue谢谢喵~(提Issue方便往后其他有相同问题的人不会再问一遍喵)**

## 环境准备喵！

1. 编写本项目时使用的是 **python3.11.8** 的喵，不能完全保证其他版本会不会出现问题喵，建议使用 **python>=3.9** 来运行喵~(后面换成3.11.8滴喵！)

2. 注意在使用本项目前要先安装`requirement.txt`中的模块喵

## 使用喵！

### 安装requests、colorlog库喵：

直接在命令行运行喵：

```
pip install requests colorlog
```

或者如果想要一点仪式感也可以运行喵：

```
pip install -r requirement.txt
```

### 各函数功能使用方法喵：

看`example.py`吧喵，里面写了一个示例，用上了主要功能，看注释也许都能理解怎么用了罢喵~

`getSave.py`是获取云存档并解析写出到`PhigrosSave.json`的示例喵

`uploadNickname.py`是修改昵称的示例，但Phigros仅在登录Taptap时会同步一次昵称好像，不如自己去手机上改`.userdata`喵

## 未来计划功能喵！

- [x] **本地提取userdata[ADB/]**(注释较为完整喵)
  - [x] ~~少量防呆设计喵~~
  - [x] ~~提取userdata喵~~

- [x] **Taptap扫描二维码获得userdata[QRCode]**(注释较为完整喵)
  - [x] ~~控制台输出二维码喵~~
  - [x] ~~获得userdata喵~~

## 喵喵喵~

此项目QRCode的思路源于[yt6983138](https://github.com/yt6983138/)的项目[PhigrosLibraryCSharp](https://github.com/yt6983138/PhigrosLibraryCSharp/)喵(本文档前面也留了链接喵)(快说“谢谢yt6983138！”)

介于本喵懒惰的性格和本项目的特殊性喵，本项目也许应该可能大概会在未来也可能在现在某个时间突然停更或者消失喵(bushi)

## 更新日志喵：

### 2025/02/08：
1. 将GetSession从Phi-CloudAction分离至本仓库
2. 修改部分代码，优化部分注释
