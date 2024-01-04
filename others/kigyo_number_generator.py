from random import randint

# def generate_random_apple_point(self)->tuple[int,int]:
#     apple_x=random.randint(1,WIDTH-2)
#     apple_y=random.randint(1,HEIGHT-2)
#     if self.rows[apple_y][apple_x]=="x" or self.rows[apple_y][apple_x]=="-" or rows[apple_y][apple_x]=="|" or self.rows[apple_y][apple_x]=="O":
#         print("apple random utkozesZUHJIOEERTZUIGHJKGHJKDFGHJKLERTZUIOPCVBNM")
#         self.generate_random_apple_point()
#         # NOTE: mikor már telített a tábla,az utolsó kis terület is filled akkor ez lehet hibát dob
#     else:
#         return apple_y,apple_x

class Numbers:
    def __init__(self) -> None:
        self.numbers=[]

    def generate_random_number(self):
        x=randint(1,5)
        # y=randint(1,5)
        return x
    
    def check_if_number_in_numbers(self):
        number=self.generate_random_number()
        if number in self.numbers:
            self.check_if_number_in_numbers()
        else:
            return number

n=Numbers()

for i in range(10):
    x=n.check_if_number_in_numbers()
    n.numbers.append(x)

print(n.numbers)
