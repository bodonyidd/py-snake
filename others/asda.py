import threading
import keyboard
import time

class MyObject:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0
        # self.lock = threading.Lock()
        self.last_movement="right"
        self.cooldown = 0.7
        self.last_update_time=time.time()

    def update_position(self, direction):
        # with self.lock:
        current_time = time.time()
        if current_time - self.cooldown > self.last_update_time:
            if direction == "left":
                self.left += 1
            elif direction == "right":
                self.right += 1
            elif direction == "up":
                self.up += 1
            elif direction == "down":
                self.down += 1
            self.last_update_time = current_time

    def handle_key_press(self, key):
        if key.name == "left":
            self.last_movement="left"
            self.update_position("left")
        elif key.name == "right":
            self.last_movement="right"
            self.update_position("right")
        elif key.name == "up":
            self.last_movement="up"
            self.update_position("up")
        elif key.name == "down":
            self.last_movement="down"
            self.update_position("down")

# Create an instance of the object
my_object = MyObject()
my_object.stop_program = False
# Define a function to be run in a separate thread
def key_listener():
    keyboard.on_press(my_object.handle_key_press)
    keyboard.wait("esc")  # Wait for the "esc" key to exit the program
    my_object.stop_program = True

# Create a thread for the key listener
key_listener_thread = threading.Thread(target=key_listener)

# Start the thread
key_listener_thread.start()
# Main code can continue running independently
while not my_object.stop_program:
    # with my_object.lock:
        print(f"Left: {my_object.left}, Right: {my_object.right}, Up: {my_object.up}, Down: {my_object.down}")
        my_object.update_position(direction=my_object.last_movement)
        time.sleep(0.8)
