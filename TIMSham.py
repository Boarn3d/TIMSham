import pyautogui,time,pyperclip,win32clipboard,random,os
from io import BytesIO
from PIL import Image

pic_dir = '.\\pic\\'
dic_path = '.\\dic.txt'
game_path = '.\\games.txt'
config_path = '.\\config.txt'
steam_path = ''

dic = []
game_list = []

dic_count = 0
game_count = 0
sleep_min_min = 0
sleep_min_max = 12
say_chance = 100
window = None
window_name = None
mode = 0


def Mysetup(var, content):
    if var == 'STEAM_PATH':
        global steam_path
        steam_path = content.replace("\\", "\\\\")
    elif var == 'SLEEP_MIN':
        global sleep_min_min
        sleep_min_min = int(content)
    elif var == 'SLEEP_MAX':
        global sleep_min_max
        sleep_min_max = int(content)
    elif var == 'TARGET_WINDOW':
        global window
        global window_name
        window_name = str(content)
        window = pyautogui.getWindowsWithTitle(window_name)
    elif var == 'MODE':
        global mode
        mode = int(content)
    elif var == 'WORD_CHANCE':
        global say_chance
        say_chance = int(content)


with open(game_path, 'r',encoding='utf8') as fo:
    for lines in fo:
        lines = lines.replace("\n","")
        game = lines.split(",")
        game_list.append(game)
    game_count = len(game_list)

with open(dic_path, 'r',encoding='utf8') as fo:
    for lines in fo:
        dic.append(lines.replace("\n",""))
    dic_count = len(dic)

with open(config_path, 'r',encoding='utf8') as fo:
    for lines in fo:
        lines = lines.replace("\n", "")
        while lines.find("  ") != -1:
            lines = lines.replace("  ", " ")
        line = lines.split(" ")
        Mysetup(line[0][1:len(line[0]) - 1], line[1])

def Sham():
    global mode
    if mode == 1: # only game
        startgame()
    elif mode == 2: #pic and word
        if setwindow():
            jpgpaste()
            wordpaste()
            window[0].minimize()
    elif mode == 0: # game and pic
        if setwindow():
            jpgpaste()
            window[0].minimize()
        startgame()
    elif mode == -1: # only pic
        if setwindow():
            jpgpaste()
            window[0].minimize()
    elif mode == 3: # all
        if setwindow():
            jpgpaste()
            wordpaste()
            window[0].minimize()
        startgame()

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
    pic_list = os.listdir(pic_dir)
    pic_num = random.randint(0,len(pic_list)-1)
    Img = Image.open(pic_dir+pic_list[pic_num])
    Myprint("Pic: "+str(pic_list[pic_num]))
    output = BytesIO()
    Img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()
    send_to_clipboard(win32clipboard.CF_DIB, data)
    Mypaste()


def random_time(min,max):
    return random.randint(min,max)*60+random.randint(0,59)

def startgame():
    random_game = random.randint(0,game_count-1)
    Myprint("Launch Game: "+game_list[random_game][1])
    os.system(steam_path+" steam://rungameid/"+str(game_list[random_game][0]))
    game_time = random_time(int(game_list[random_game][2]),int(game_list[random_game][3]))
    t = time.time()+game_time
    Myprint("Close when: "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t)))
    time.sleep(game_time)
    os.system("taskkill /F /IM \""+str(game_list[random_game][1])+"\"")

def wordpaste():
    say = dic[random.randint(0,dic_count-1)]
    if random.randint(0,100)<say_chance :
        Myprint("Say: "+str(say))
        pyperclip.copy(say)
        Mypaste()
    else:
        Myprint("No word this time.")

def test(): 
    Myprint("Test:")
    Sham()
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
    window = pyautogui.getWindowsWithTitle(window_name)
    if window == []:
        Myprint("Couldn't find target window:"+window_name)
        return False
    window[0].restore()
    window[0].activate()
    return True


breakline("long")
Myprint("Go!\nBegin Time:"+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+"\nMode:"+str(mode))

time.sleep(3)
test()

while True:
    sleep_min = random.randint(sleep_min_min,sleep_min_max)
    sleep_sec = random.randint(0,59)
    sleep_time = sleep_min*60+sleep_sec
    Myprint("Sleep: %d min %d sec"%(sleep_min,sleep_sec))
    t = time.time()+sleep_time
    Myprint("Wake: "+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t)))
    breakline("short")
    time.sleep(sleep_time)
    Sham()