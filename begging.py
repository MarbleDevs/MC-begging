import time
import keyboard
import random
import chardet
from datetime import datetime

#change these to your Minecraft settings

rank = 'rank'
color = 'rank color'
name = 'username'
delay_start = 7
delay_stop = 20

#dont change these options

loop = True
lastbegtest = ""
stop = False

def pause():
    global stop
    stop = not stop
    print(datetime.now().strftime('%H:%M:%S:%f'), f": Pause is now {stop}")


with open('begs.txt', 'rb') as file:
    file_raw = chardet.detect(file.read())

with open('begs.txt', 'r', encoding=file_raw['encoding']) as file:
    beg_lines = file.readlines()

print(datetime.now().strftime('%H:%M:%S:%f'),": Waiting for K")
keyboard.wait("k")
keyboard.add_hotkey('b', pause)

while True:
    while not stop:
        print(datetime.now().strftime('%H:%M:%S:%f'),": Random choice ahead!")
        begtext = random.choice(beg_lines)

        begtext = begtext.replace('{rank}', rank)
        begtext = begtext.replace('{color}', color)
        begtext = begtext.replace('{name}', name)

        print(begtext)

        if lastbegtest == begtext:
            nottwice = True
            print(datetime.now().strftime('%H:%M:%S:%f'),": It has been twice")
        else:
            nottwice = False
            print(datetime.now().strftime('%H:%M:%S:%f'),": It has not been twice")

        lastbegtest = begtext

        wait = random.randint(delay_start, delay_stop)
        wait = int(wait)

        time.sleep(wait)
        if stop:
            break

        if not nottwice:
            print(datetime.now().strftime('%H:%M:%S:%f'),": Writing")
            print("")
            keyboard.press_and_release("t")
            time.sleep(0.1)
            keyboard.write(begtext)
            time.sleep(2)
            keyboard.press_and_release("enter")