from random import randint

nb=[]
def generate():
    return randint(1,90)
def asd():
    numbers=[]
    for _ in range(5):
        n=generate()
        while n in numbers:
            n=generate()
        numbers.append(n)
    # print(numberss)
    nb.append(numbers)



for _ in range(10000):
    asd()

numbers={}
for i in nb:
    for j in i:
        if j in numbers:
            numbers[j]=numbers[j]+1
        else:
            numbers[j]=0
    
most_frequent_number=0
freq=0
for id,value in numbers.items():
    # print(id,value)
    if freq<value:
        freq=value
        most_frequent_number=id
        
        

print(most_frequent_number,freq )




    