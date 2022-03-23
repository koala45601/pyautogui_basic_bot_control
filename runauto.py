import pyautogui
import time
import schedule
import datetime

#check Position
global c
global d
c = 0
d = 1
print("Bot is working, Please don't Control mouse!!!.")
time.sleep(2)
for x1 in range(1,10):
    print('Start in',x1)
    time.sleep(1)
date = datetime.datetime.now()
print(date)
def cl():
    global c
    #while True:
    for x in range(0,5):
        pos = pyautogui.position()
        #pos = pyautogui.displayMousePosition()
        print(f'{c} : PX=',pos.x, 'PY=',pos.y)
        time.sleep(1.5)
        c+=1

    #working bot
        if c == 5:
            print('Moniter 1: Task 1 Working to bomb')
            pos_mov= pyautogui.moveTo(x=289, y=379, duration=0.5)
            time.sleep(2)
            p1=pyautogui.click(x=289, y=379)
            time.sleep(5)
            p2=pyautogui.doubleClick(x=289, y=379)
            time.sleep(15)
           # p22=pyautogui.doubleClick(x=283, y=394)
           # time.sleep(10)
            #work
            #hero 1
            #p3=pyautogui.moveTo(x=246, y=200,duration=0.25)
            #time.sleep(2)
            p3=pyautogui.click(x=247, y=170)
            time.sleep(10)
            print('Hero Working Moniter1 : ON')
           
            #exit work hero
            p8=pyautogui.click(x=319, y=144)
            time.sleep(4)
            p8=pyautogui.click(x=319, y=144)
            time.sleep(4)
            p8=pyautogui.click(x=319, y=144)
            time.sleep(4)
            p9=pyautogui.doubleClick(x=319, y=144)
            time.sleep(2)
            p9=pyautogui.doubleClick(x=503, y=172)
            time.sleep(2)
            print('Exit to mode select hero.')
            c = 0
            time.sleep(10)
            print('Moniter 1 Task 1 : Run Suscess ')

            #Moniter 2---------------------------------------------------------------------
            print('Moniter 2: Task 1 Working to bomb')
            pos_mov= pyautogui.moveTo(x=848, y=398, duration=0.5)
            time.sleep(2)
            p1=pyautogui.click(x=848, y=398)
            time.sleep(5)
            p2=pyautogui.doubleClick(x=848, y=398)
            time.sleep(7)
           # p22=pyautogui.doubleClick(x=283, y=394)
           # time.sleep(10)
            #work
            #hero 1
            p3=pyautogui.moveTo(x=811, y=190,duration=0.25)
            time.sleep(2)
            p3=pyautogui.click(x=811, y=190)
            time.sleep(10)
            print('Hero Working Moniter2 : ON')
            
            #exit work hero
            p8=pyautogui.click(x=880, y=162)
            time.sleep(4)
            p8=pyautogui.click(x=880, y=162)
            time.sleep(4)
            p8=pyautogui.click(x=880, y=162)
            time.sleep(4)
            p9=pyautogui.doubleClick(x=1052, y=201)
            time.sleep(2)
            print('Exit to mode select hero.')
            c = 0
            time.sleep(10)
            print('Moniter 2 Task 1 : Run Suscess ')

             #Moniter 3 ------------------------------------------------------------
            print('Moniter 1: Task 1 Working to bomb')
            pos_mov= pyautogui.moveTo(x=292, y=853, duration=0.5)
            time.sleep(2)
            p1=pyautogui.click(x=292, y=853)
            time.sleep(5)
            p2=pyautogui.doubleClick(x=292, y=853)
            time.sleep(7)
           # p22=pyautogui.doubleClick(x=283, y=394)
           # time.sleep(10)
            #work
            #hero 1
            #p3=pyautogui.moveTo(x=243, y=192,duration=0.25)
            #time.sleep(2)
            p3=pyautogui.click(x=249, y=647)
            time.sleep(10)
            print('Hero Morniter 3 : ON')
            #exit work hero
            p8=pyautogui.click(x=322, y=624)
            time.sleep(4)
            p8=pyautogui.click(x=322, y=624)
            time.sleep(4)
            p8=pyautogui.click(x=322, y=624)
            time.sleep(4)
            p9=pyautogui.doubleClick(x=503, y=640)
            time.sleep(2)
           # p9=pyautogui.doubleClick(x=503, y=640)
            # time.sleep(2)
            print('Exit to mode select hero.')
            c = 0
            time.sleep(10)
            print('Moniter 3 Task 1 : Run Suscess ')

   

#def check new map
def nw_mp():
    global d
    #check new map every 13 min
    print('Task 3 check new map every 13 min : ',d)
    d+=1
    for v1 in range(0,5):
        p1 = pyautogui.click(250, 347)
        time.sleep(2)
    print('Moniter 1 : Task 3 : Run Suscess')
    
    for v2 in range(0,5):
        p2 = pyautogui.click(849, 342)
        time.sleep(2)
    print('Moniter 2 : Task 3 : Run Suscess')

    
    for v3 in range(0,5):
        p3 = pyautogui.click(256, 797)
        time.sleep(2)
    print('Moniter 3 : Task 3 : Run Suscess')
    
    #if pyautogui.pixel(324, 347)[142] == 142:
    #    p1 = pyautogui.click(324, 247)

# select hero 6
def h_SR():

    print('Task 2 Working to Hero SR')
    #pos_mov= pyautogui.moveTo(x=1362, y=178, duration=0.5)
    time.sleep(1)
    p1=pyautogui.click(x=288, y=394)
    time.sleep(10)
    p2=pyautogui.click(x=288, y=394)
    time.sleep(8)
    p11 = pyautogui.moveTo(251, 358)
    time.sleep(2)        
    #scroll down to select hero
    for y in range(0,8):
        sc = pyautogui.scroll(-10)
        time.sleep(2)
        
    #exit work hero
    p11 = pyautogui.click(243, 310)
    time.sleep(3)

    p8=pyautogui.click(x=318, y=158)
    time.sleep(4)
    p9=pyautogui.doubleClick(x=505, y=167)
    time.sleep(2)
    p9=pyautogui.doubleClick(x=505, y=167)
    time.sleep(5)
    print('Compelete hero 6 to working')
#remap
def remap():
    #return to home
    print('Moniter 1 Task 3 : Remap every 15 min.')
    p1=pyautogui.moveTo(72, 105, duration=0.25)
    time.sleep(2)
    p2=pyautogui.doubleClick(72, 105)
    time.sleep(7)

    #gotomap
    p1=pyautogui.moveTo(296, 249, duration=0.25)
    time.sleep(2)
    p2=pyautogui.doubleClick(296, 249)
    time.sleep(4)
    print('Moniter 1 : Go to Map Suscess')

        #return to home
    print('Moniter 2 Task 3 : Remap every 15 min.')
    p1=pyautogui.moveTo(624, 118, duration=0.25)
    time.sleep(2)
    p2=pyautogui.doubleClick(624, 118)
    time.sleep(3)

    #gotomap
    p1=pyautogui.moveTo(847, 266, duration=0.25)
    time.sleep(2)
    p2=pyautogui.doubleClick(847, 266)
    time.sleep(4)
    print('Moniter 2 : Go to Map Suscess')

        #return to home
    print('Moniter 3 Task 3 : Remap every 15 min.')
    p1=pyautogui.moveTo(71, 577, duration=0.25)
    time.sleep(2)
    p2=pyautogui.doubleClick(71, 577)
    time.sleep(3)

    #gotomap
    p1=pyautogui.moveTo(293, 761, duration=0.25)
    time.sleep(2)
    p2=pyautogui.doubleClick(293, 761)
    time.sleep(4)
    print('Moniter 3 : Go to Map Suscess')

def reconf():
    print('Task 4 Reconnect every 20 min')
    p1=pyautogui.click(97, 57)
    print('Refrest Screen')
    time.sleep(5)
    p2=pyautogui.doubleClick(284, 301)
    print('Clear Button and wait 10sec.')
    time.sleep(15)
    p3=pyautogui.click(289, 333)
    print("Connected Bomb!!")
    time.sleep(25)
    p2=pyautogui.doubleClick(284, 301)
    time.sleep(2)
    p4=pyautogui.click(444, 553)
    print('Sign Meta')
    time.sleep(40)
    p5=pyautogui.click(292, 241)
    print('Go to Map')
    time.sleep(2)
    print('Task4 : Run Suscess')

def check1():
    #global c
    while True:
    #for x in range(0,5):
        pos = pyautogui.position()
        pos = pyautogui.displayMousePosition()
        #print(f'{c} : PX=',pos.x, 'PY=',pos.y)
        time.sleep(1.5)
        #c+=1
    
#set schedule
schedule.every(80).minutes.do(cl)
#schedule.every(2).minutes.do(nw_mp)
#schedule.every(240).minutes.do(h_SR)
schedule.every(5).minutes.do(remap)
#schedule.every(25).minutes.do(reconf)
#-------------------------------------------------------
#schedule.every(5).seconds.do(nw_mp)
schedule.every(4).seconds.do(cl)
#schedule.every(4).seconds.do(check1)
#schedule.every(5).seconds.do(h_SR)
schedule.every(5).seconds.do(remap)
#schedule.every(5).seconds.do(reconf)
schedule.every().hour.do(cl)
#schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)
