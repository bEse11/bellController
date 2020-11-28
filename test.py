from gpiozero import LED
from time import sleep
from threading import Timer
import time

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)
led4 = LED(23)

h = [1,3,4,1,1]
ht = [120,120,780,1780,2780]
noteStarters = {}
noteStoppers = {}

def startNote(x):
    #print("startingu")
    noteSelector(x).off()
    return 1

def stopNote(x):
    #print("stopperino")
    noteSelector(x).on()
    return 1

def noteSelector(x):
    switcher = {
        1: led1,
        2: led2,
        3: led3,
        4: led4
        }
    return switcher.get(x,"Note exist NO")

i = 0
for x in h:
    timerOnName = "t" + str(i) + "On"
    timerOffName = "t" + str(i) + "Off"
    noteStarters[timerOnName] = Timer(ht[i]/1000, startNote, [x])
    noteStoppers[timerOffName] = Timer(ht[i]/1000 + 0.1, stopNote, [x])
    noteStarters[timerOnName].start()
    noteStoppers[timerOffName].start()
    i = i + 1
    
