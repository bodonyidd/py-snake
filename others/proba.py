import threading
import time
import msvcrt

def task():
    while True:
        print("Working...")
        time.sleep(1)

def check_key():
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'w':
                print("Key 'w' pressed. Stopping the task.")
                break

if __name__ == "__main__":
    worker_thread = threading.Thread(target=task)
    key_check_thread = threading.Thread(target=check_key)

    worker_thread.start()
    key_check_thread.start()

    worker_thread.join()
    key_check_thread.join()

    print("Task and key check threads are done.")
