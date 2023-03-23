

maxOne=-1001
maxTwo=-1002
number = int(input())
while number != 0:
    if maxOne<number:
       maxTwo=maxOne
       maxOne=number
    elif maxTwo<number:
       maxTwo=number
    number = int(input())
print(maxTwo)