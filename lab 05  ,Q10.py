print("Yusra Masood , 18B-093-CS , Section A ")
print("lab 5")
print("Q10")

import math
fnum= eval(input("Enter the first number "))
lnum= eval(input("Enter the last number "))
print("number       sin()           cos()              tan()")
def angle(fnum , lnum):
    for num in range(fnum , lnum+1):
        s = math.sin(math.radians(num))
        c = math.cos(math.radians(num))
        t = math.tan(math.radians(num))
        print(str(num)+"  "+str(s)+"  "+str(c)+"  "+str(t))

angle(fnum , lnum)

input()
