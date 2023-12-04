# TIMSham

### **config.txt** 

配置说明

> **[STEAM_PATH]** PATH\TO\steam.exe **#指向你的steam可执行文件，用intwindows的目录符号\\**
>
> **[SLEEP_MIN]** 0 **#最短静默时间，单位为分钟**，int
>
> **[SLEEP_MAX]** 12 **#最长静默时间，单位为分钟**，int
>
> **[TARGET_WINDOW]** Sample **#目标发言窗口标题**
>
> **[MODE]** 1 **#模式1：仅打开游戏；模式2：仅说话和发图片；模式3：说话、发图、开游戏**
>
> **[WORD_CHANCE]** 67 **#在说话时有多少概率说话**，int(0-100)

### **dic.txt**

存储发言词汇，一行一个，可以空格，如

> Hello
>
> here
>
> is
>
> a
>
> sample
>
> #每次发言会随机选取其中一行发言

### **pic**目录

里面存储图片，命名为 **数字+.jpg** 格式，必须从小到大，如

> 1.jpg

### **games.txt** 

存储要打开的游戏，一行一个，格式如下

> 570,dota2.exe,79,135
>
> #游戏代号,进程名称,最小打开分钟,最大打开分钟

## 使用

1. 打开目标TIM会话窗口挂在后台**（必需）**。
3. 编译执行 **TIMSham.py** 或者执行 **TIMSham.bat**

会生成一个log保存记录