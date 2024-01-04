import __future__
import copy
import keyboard
import random
import os


HEIGHT=20
WIDTH=50

# PLACE=HEIGHT*WIDTH
def create_row(row_value=" "):
    one_row=[row_value for _ in range(WIDTH)] # WIDTH
    return one_row

one_row=create_row()
one_row[0]="|"
one_row[-1]="|"

def create_rows():
  rows=[copy.deepcopy(one_row) for _ in range(HEIGHT)] # HEIGHT
  rows[0]=create_row("-")
  rows[-1]=create_row("-")
  return rows
rows=create_rows()




start_point_x=int((WIDTH-2)/2) # "-2"  are the first and the last string: '|'
start_point_y=int((HEIGHT-2)/2) # "-2"  are the first and the last row: '-'
rows[start_point_y][start_point_x]="O"
start_snake_length=1
snake_pos=[[start_point_y,start_point_x]]


class Snake:
    HEIGHT=20
    WIDTH=50

    start_point_x=int((WIDTH-2)/2) # "-2"  are the first and the last string: '|'
    start_point_y=int((HEIGHT-2)/2) # "-2"  are the first and the last row: '-'
    rows[start_point_y][start_point_x]="O"
    start_snake_length=1
    snake_pos=[[start_point_y,start_point_x]]


    rows[9][26]="x"




    def __init__(self) -> None:
        self.snake_length=1
        self.x=start_point_x
        self.y=start_point_y
        self.snake_coord=[[self.y,self.x]]
        self.rows=rows
        self.is_game=True
        self.last_snake_coords=[]
        self.last_movement=None
        self.points=0
    
    def clear_console(self,is_moved=False):
        if is_moved:
            # Clear the console screen based on the OS
            if os.name == 'posix':
                os.system('clear')  # For UNIX-like systems (Linux, macOS)
            elif os.name == 'nt':
                os.system('cls')    # For Windows

    def create_row(row_value=" "):
        one_row=[row_value for _ in range(WIDTH)] # WIDTH
        return one_row

    one_row=create_row()
    one_row[0]="|"
    one_row[-1]="|"

    def create_rows():
        rows=[copy.deepcopy(one_row) for _ in range(HEIGHT)] # HEIGHT
        rows[0]=create_row("-")
        rows[-1]=create_row("-")
        return rows
    rows=create_rows()


    def draw_table(self,tabla):
        # point
        first_row_length=len(tabla[0]) #width
        point_row=[" " for _ in range(first_row_length)]
        text=list(f"point: {self.points}")
        for i in range(len(text)):
            point_row[i]=text[i]
        print("".join(point_row))
        
        # tabla
        for i in range(len(tabla)):
            print("".join(tabla[i]))

    def moving(func):
        def wrapper(self,*args, **kwargs):
            func(self,*args, **kwargs)
            self.clear_console(True)
            self.draw_table(self.rows)
            # print(self.snake_coord)
            return rows
        return wrapper

    def is_next_border_or_snake(self,new_y,new_x):
        if self.rows[new_y][new_x]=="-" or rows[new_y][new_x]=="|" or self.rows[new_y][new_x]=="O":
            return True
        return False

    def check_apple(self,new_y,new_x):
        if self.rows[new_y][new_x]=="x":
            return True
        return False

    def create_snake(self):
        z=self.snake_coord[0]
        self.snake_coord.remove(z)
        for i in self.snake_coord:
            self.rows[i[0]][i[1]] = "O"
        self.rows[z[0]][z[1]] = " "
    
    def generate_random_apple_point(self)->tuple[int,int]:
        apple_x=random.randint(1,WIDTH-2)
        apple_y=random.randint(1,HEIGHT-2)
        if self.rows[apple_y][apple_x]=="x" or self.rows[apple_y][apple_x]=="-" or rows[apple_y][apple_x]=="|" or self.rows[apple_y][apple_x]=="O":
            self.generate_random_apple_point()
            # NOTE: mikor már telített a tábla,az utolsó kis terület is filled akkor ez lehet hibát dob
        else:
            return apple_y,apple_x
        
    def draw_new_apple(self,apple_y,apple_x):
        self.rows[apple_y][apple_x] = "x"



    @moving
    def move_right(self):
        if self.last_movement=="LEFT":
            raise ValueError
        new_y=copy.deepcopy(self.y) #start 9 
        new_x=copy.deepcopy(self.x+1) # start 24
        self.movement(new_y=new_y,new_x=new_x)
        self.last_movement="RIGHT"

    def movement(self,new_y,new_x):
        if self.is_next_border_or_snake(new_y,new_x):
            raise ValueError
        self.last_snake_coords=copy.deepcopy(self.snake_coord)
        if self.check_apple(new_y,new_x):
            self.snake_length=self.snake_length+1
            self.snake_coord.insert(0,[self.snake_coord[0][0]-1,self.snake_coord[0][1]-1])
            self.points=self.points+1
            apple_y,apple_x=self.generate_random_apple_point()
            self.draw_new_apple(apple_y,apple_x)
        self.snake_coord.append([new_y,new_x])
        self.create_snake()
        self.y=copy.deepcopy(new_y)
        self.x=copy.deepcopy(new_x)
        


    @moving
    def move_up(self):
        if self.last_movement=="DOWN":
            raise ValueError
        new_y=copy.deepcopy(self.y-1) #start 9 
        new_x=copy.deepcopy(self.x) # start 24
        self.movement(new_y=new_y,new_x=new_x)
        self.last_movement="UP"
    
    @moving
    def move_down(self):
        if self.last_movement=="UP":
            raise ValueError
        new_y=copy.deepcopy(self.y+1) #start 9 
        new_x=copy.deepcopy(self.x) # start 24
        self.movement(new_y=new_y,new_x=new_x)
        self.last_movement="DOWN"
    
    @moving
    def move_left(self):
        if self.last_movement=="RIGHT":
            raise ValueError
        new_y=copy.deepcopy(self.y) #start 9 
        new_x=copy.deepcopy(self.x-1) # start 24
        self.movement(new_y=new_y,new_x=new_x)
        self.last_movement="LEFT"
        
    

global game
game=True

        
new_y=start_point_y
new_y=start_point_y
x=start_point_x
y=start_point_y

s=Snake()

try:
    while game:
        s.clear_console(True)
        s.draw_table(rows)
        key_event = keyboard.read_event(suppress=True)

        if key_event.event_type == keyboard.KEY_DOWN and key_event.name=="right":
            s.move_right()
            
            
        elif key_event.event_type == keyboard.KEY_DOWN and key_event.name=="left":
            s.move_left()

        elif key_event.event_type == keyboard.KEY_DOWN and key_event.name=="up":
            s.move_up()

        elif key_event.event_type == keyboard.KEY_DOWN and key_event.name=="down":
            s.move_down()
except ValueError:
    game=False
    s.clear_console(True)
    print("Game over! Earned points: {}".format(s.points))


# TODO:
    # - automattikusan kéne a cuccnak elindulnia jobbra és ha felszed egy hamit akkor mindig egyre gyorsabban mennie
    # - egy irányba induljon el és akkor mindig arra felé tendáljon folyamotsan 


# ----------------------------------------------------


def reset_last_apple_point(rows,apple_y,apple_x):
   rows[apple_y][apple_x]=" "
   return rows










  




