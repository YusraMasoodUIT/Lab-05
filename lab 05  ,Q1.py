print("Yusra Masood, 18B-093-CS , Section A")
print("Lab 05")
print("Q1")

import math
rad = eval(input("Enter a value for the radius of the cylinder "))
height = eval(input("Enter a value for the height of the cylinder "))

def area(rad , height):
    x = math.pi
    a1 = 2*x*rad*height
    a2 = 2*x*(rad**2)
    total = a1 + a2
    print("the area of the cylinder is " + str(total)) 

def volume(rad , height):
    y = math.pi
    vol = y*(rad**2)*height
    print("The volume of the cylinder is "+str(vol))

volume(rad , height)
area(rad , height)

input()
