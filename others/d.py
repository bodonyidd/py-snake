import keyboard
import time

counter = 0
incrementing = True

class ASD:
    def __init__(self) -> None:
        self.up=0
        self.down=0
        self.left=0
        self.right=0
        self.last_movement="right"
        # self.directions: dict={"left":self.left,"right":self.right,"up":self.up,"down":self.down}

    def get_key_value(self,key_name):
        if key_name=="left":
            return self.left
        elif key_name=="right":
            return self.right
        elif key_name=="up":
            return self.up
        elif key_name=="down":
            return self.down
    
    def set_value(self,direction,value):
        if direction=="left":
            self.left=self.left+value
        elif direction=="right":
            self.right=self.right+value
        elif direction=="up":
            self.up=self.up+value
        elif direction=="down":
            self.down=self.down+value
        # time.sleep(0.5)
        
        


a=ASD()
base=["left","right","up","down"]
t={"left":a.left,"right":a.right,"up":a.up,"down":a.down}
a.last_movement="right"
while True:
    # print(counter)

    if keyboard.is_pressed("right"):
        print("Key 'right' pressed. Toggling direction.")
        a.last_movement="right"

    elif keyboard.is_pressed("left"):
        print("Key 'left' pressed. Toggling direction.")
        a.last_movement="left"


    elif keyboard.is_pressed("up"):
        print("Key 'up' pressed. Toggling direction.")
        a.last_movement="up"


    elif keyboard.is_pressed("down"):
        print("Key 'down' pressed. Toggling direction.")
        a.last_movement="down"

    # key_name,value=a.which_key_to_increment()
    # value=value+1
    a.set_value(a.last_movement,1)
    value=a.get_key_value(a.last_movement)
    print(value)
    

    # Add a delay to make the output more readable
    # Adjust the sleep duration based on your preference

    # time.sleep(0.5)
# n=input()