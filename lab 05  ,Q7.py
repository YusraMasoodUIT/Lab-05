print("Yusra Masood, 18B-093-CS , Section A")
print("Lab 05")
print("Q7")

import math
def horizontal():
    time = eval(input("Enter the total time taken by the object,Please enter your answer in digits "))
    initialx = eval(input("Enter the initial velocity along x-axis, Please enter your answer in digits "))
    angx = eval(input("Enter the angle with which it's thrown , Please enter your answer in degrees "))
    ax = math.sin(math.radians(2*angx))
    g = 9.81
    rang = ((initialx**2) *(ax))/g
    velocity = initialx
    dist = velocity * time
    print("\n")
    print("The horizontal velocity  is "+str(velocity)+"m/s")
    print("The horizontal velocity would be same  as initial velocity")
    print("The horizontal distance covered is "+str(dist)+"m")
    print("The horizontal range is " +str(rang)+"m")


def vertical():
    time = eval(input("Enter the total time taken by the object,Please enter your answer in digits "))
    initialy = eval(input("Enter the initial velocity accross y-axis, Please enter your answer in digits "))
    ang = eval(input("Enter the angle with which it's thrown , Please enter your answer in degrees "))
    g = -9.81
    dist = (initialy*time)-(0.5*g*(time**2))
    velocity = initialy -(g*time)
    a = math.sin(math.radians(ang))
    maxH = ((initialy**2)*(a**2))/(2*g)
    print("\n")
    print("The vertical velocity  is "+str(velocity)+"m/s")
    print("The vertical distance covered is "+str(dist)+"m")
    print("The max Height covered is " +str(maxH)+"m")



def time():
    print("Calculates the time of flight i.e. The total time the object is in the air")
    print("\n")
    initial = eval(input("Enter the initial velocity , Please enter your answer in digits "))
    ang = eval(input("Enter the angle with which it's thrown , Please enter your answer in degrees "))
    g =9.81
    a = math.sin(math.radians(ang))
    time = (2*initial*a)/g
    print("\n")
    print("The time of flight is "+str(time)+"s")


decision = input("What do you want to calculate for Projectile motion , Horizontal trajectory , Vertical trajectory or time of flight , Please enter your answe in the form of H or V or T ")
print("\n")
if decision == "H":
    horizontal()
elif decision == "V":
    vertical()
elif decision == "T":
    time()
else:
    print("Sorry your choice wasn't correct , Please try again later ")


input()














    
