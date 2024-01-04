import threading
import time

class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            # Your thread logic here
            print("Working...")
            time.sleep(1)

    def stop(self):
        self._stop_event.set()

if __name__ == "__main__":
    my_thread = MyThread()
    my_thread.start()

    # Allow the thread to run for some time
    # time.sleep(5)

    # Stop the thread using the flag
    my_thread.stop()
