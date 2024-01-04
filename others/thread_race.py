import threading
import time

shared_resource = 0
lock = threading.Lock()

def increment_shared_resource():
    global shared_resource
    with lock:
        current_value = shared_resource
        time.sleep(1)  # Simulating some processing time
        shared_resource = current_value + 1

def main():
    threads = []

    for _ in range(5):
        thread = threading.Thread(target=increment_shared_resource)
        print(thread.name)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print("Final value of shared resource:", shared_resource)

if __name__ == "__main__":
    main()
