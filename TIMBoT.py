import pyautogui,time,pyperclip,win32clipboard,random,os
from io import BytesIO
from PIL import Image

pic_dir = '.\\pic\\'
dic_path = '.\\dic.txt'
config_path = '.\\config.txt'

dic = []
sleep_min_min = 0
sleep_min_max = 12
count = 0
target_window_name = ""

with open(dic_path, 'r',encoding='utf8') as fo:
    for lines in fo:
        count += 1
        dic.append(lines.replace("\n",""))

with open(config_path, 'r',encoding='utf8') as fo:
        temp = fo.readline()
        temp = temp.replace("\n","")
        temptime = temp.split(",")
        sleep_min_min = int(temptime[0])
        sleep_min_max = int(temptime[1])
        temp = fo.readline()
        target_window_name = temp.replace("\n","")

window = pyautogui.getWindowsWithTitle(target_window_name)

def Myprint(text):
    print(text)
    with open(".\\log", "a", encoding='utf8') as fo:
        fo.write(text+"\n")

def minibreak():
    ms = float(str(random.random())[0:4])
    time.sleep(ms)

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def Mypaste():
    minibreak()
    pyautogui.hotkey('ctrl','v')
    minibreak()
    pyautogui.press("enter")
    minibreak()

def jpgpaste():
    num = len(os.listdir(pic_dir))
    pic_num = random.randint(1,num)
    Img = Image.open(pic_dir+str(pic_num)+'.jpg')
    Myprint("Pic: "+str(pic_num))
    output = BytesIO()
    Img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)
    Mypaste()

def wordpaste():
    say = dic[random.randint(0,count-1)]
    Myprint("Say: "+str(say))
    pyperclip.copy(say)
    Mypaste()

def Pastetest(): 
    Myprint("Test:")
    setwindow()
    jpgpaste()
    wordpaste()
    window[0].minimize()
    Myprint("Test End.\n")

def breakline(type):
    char = "-"
    length = 31
    if type == "long":
        length = 63
        char = "#"
    brkline = ""
    for i in range(0,length):
        brkline+=char
    Myprint(brkline+"\n")

def setwindow():
    window = pyautogui.getWindowsWithTitle(target_window_name)
    window[0].restore()
    window[0].activate()


breakline("long")
Myprint("Go!\nBegin Time:"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+"\n")

time.sleep(3)
Pastetest()

while True:
    sleep_min = random.randint(sleep_min_min,sleep_min_max)
    sleep_sec = random.randint(0,59)
    sleep_time = sleep_min*60+sleep_sec
    Myprint("Sleep: %d min %d sec"%(sleep_min,sleep_sec))
    t = time.time()+sleep_time
    Myprint("Wake: "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t)))
    breakline("short")
    time.sleep(sleep_time)
    setwindow()
    jpgpaste()
    wordpaste()
    window[0].minimize()