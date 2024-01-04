import threading
import time


def asd(name):
    for i in range(10):
        print(name)
        time.sleep(0.01)
L=["asd","y"]
for i in range(2):
    x=threading.Thread(target=asd,args=(L[i],))
    x.start()

print("done")