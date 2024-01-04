import threading

import time


def thread_function():
    print("thread 1")
    time.sleep(5)
    print("thred 1 after sleep")

def thread_function2():
    print("thread 2")



t1 = threading.Thread(target=thread_function)
t2 = threading.Thread(target=thread_function2)
t1.start()
t2.start()


# PRINT
# thread 1
# thread 2
# thred 1 after sleep