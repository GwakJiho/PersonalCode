from time import sleep
from threading import Thread, Event

event = Event()

def infinite_loop():
    while True:
        sleep(1)
        if event.is_set():
            print("infinite Loop Stop")
            return
        print("infinite Loop Thread")

t = Thread(target=infinite_loop, daemon=True)
t.start()

print("Script start")

s = input()
if s == "stop":
    event.set()

print("Script End!")