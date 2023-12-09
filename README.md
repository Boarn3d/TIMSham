# TIMSham

## Dependencies

- pyautogui
- pyperclip
- win32clipboard (pywin32)

## 配置文件详解

#### **config.txt** 

配置说明

> **[STEAM_PATH]** PATH\TO\steam.exe **#指向你的steam可执行文件，用windows的目录符号\\**
>
> **[SLEEP_MIN]** 0 **#最短静默时间，单位为分钟**，int
>
> **[SLEEP_MAX]** 12 **#最长静默时间，单位为分钟**，int
>
> **[TARGET_WINDOW]** Sample **#目标发言窗口标题**
>
> **[MODE]** 0,1,0 **#依次代表启动游戏，发图片，说话的设置，0为关闭，1为开启**
>
> **[WORD_CHANCE]** 100 **#在说话时有多少概率说话**，int(0-100)

#### **dic.txt**

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

#### **pic**目录

存储要发的图片， **jpg** 格式，命名随意，但不要有特殊字符。如

> 1.jpg

#### **games.txt** 

存储要打开的游戏，一行一个，逗号分隔，格式如下

> 570,dota2.exe,79,135
>
> #游戏steam商店代码,游戏进程名称,最小打开分钟,最大打开分钟

## 使用

1. 打开目标TIM会话窗口挂在后台。 **(模式2和3必需)**
3. 编译执行 **TIMSham.py** 或者执行 **TIMSham.bat**

会生成一个log保存记录