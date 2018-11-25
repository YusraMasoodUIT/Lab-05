print("Yusra Masood , 18B-093-CS , Section A ")
print("lab 5")
print("Q6")


print("Program to calculate three laws of motions")

def law1():
    print("Newton's first law of motion states that an object in motion remains in motion with the same velocity unless acted upon by what we call an unbalanced force")
    print("\n")
    force = input("Is the resultant force acting on the object equal to 0, Yes/No ")
    x = force.lower()
    if x == "yes":
        rest = input("Is the object at rest, Yes/No ")
        y = rest.lower()
        if y == "yes":
            print("Then the object will remain at rest untill a resultant force acts on it")
        else:
            velo = input("Is the object moving with constant velocity, Yes/No ")
            z = velo.lower()
            if z == "yes":
                velonum = eval(input("Please enter the velocity with which it is moving "))
                print("The object will continue to move at "+str(velonum)+"m/s since the velocity is constant and there is no resultant force ")
            else:
                print("Sorry... that's not a possible condition since there could only be a change in velocity if there is a resultant force acting on the object")
    else:
        forcenum = eval(input("Please enter a value for resultant force "))
        mass = eval(input("Please enter a value for the mass of the object "))
        time = eval(input("Please enter a value of the time it takes for the object to accelerate "))
        acc = forcenum / mass
        initialvelo = input("Is the object initially at rest , Yes/No ")
        w = initialvelo.lower()
        if w == "yes":
            velocity = acc * time
            displacement = 0.5*acc*(time**2)
            print("\n")
            print("The object of mass "+str(mass)+"kg and initial velocity of 0m/s will accelerate with an acceleration of "+str(acc)+"m/s^2 when a force of "+str(forcenum)+"N is applied on it")
            print("The final velocity of the object would be "+str(velocity)+"m/s and it will cover a total distance of "+str(displacement)+"m in a total time of "+str(time)+"s")
        else:
            iniu = eval(input("Enter a value for the initial velocity of the object "))
            velocity = iniu + (acc * time)
            displacement = (time*iniu)+(0.5*acc*(time**2))
            print("\n")
            print("The object of mass "+str(mass)+"kg and initial velocity of "+str(iniu)+"m/s will accelerate with an acceleration of "+str(acc)+"m/s^2 when a force of "+str(forcenum)+"N is applied on it")
            print("The final velocity of the object would be "+str(velocity)+"m/s and it will cover a total distance of "+str(displacement)+"m in a total time of "+str(time)+"s")

def law2():
    print("Newton's second law states that the acceleration of an object is directly proportional to the net force acting on it, and inversely proportional to its mass and can be written as F=ma")
    print("\n")
    option = input("What do uou want to calculate? ,force , mass or acceleration ")
    o = option.lower()
    if o == "force":
        mass = eval(input("Enter the mass of the object "))
        acc = eval(input("Enter the acceleration of the object "))
        force = mass *acc
        print("The force acting on the object of mass "+str(mass)+"kg and an acceleration of "+str(acc)+"m/s^2 is "+str(force)+"N")
    elif o == "mass":
        force = eval(input("Enter the force applied on the object "))
        acc = eval(input("Enter the acceleration of the object "))
        mass = force/acc
        print("The total mass of the object is "+str(mass)+"kg")
    else:
        force = eval(input("Enter the force applied on the object "))
        mass = eval(input("Enter the mass of the object "))
        acc = force/mass
        print("The acceleration of the object is "+str(acc)+"m/s^2")
input()



def law3():

    print("Calculates the reaction force exerted by second object on first object when the first object hits the second object ")
    print("\n")
    obj1 = input("Enter the name of the first object ")
    obj2 = input("Enter the name of the second object ")
    force1 = eval(input("Enter the force exerted by object1 on object2 "))
    print("\n")
    print("The force exerted by "+obj2+" on the "+obj1+" would be same as the force exerted by "+obj1+ " on "+obj2+" i.e."+str(force1)+ "N. This is because :-")
    print("Newton's third law states that if an object A exerts a force on object B, then object B must exert a force of equal magnitude and opposite direction back on object A.")




decision = input("Which Newton's law do you want to use? , First ,second or third ")
d = decision.lower()
if d == "first":
    law1()
elif d == "second":
    law2()
elif d == "third":
    law3()
else:
    print("Sorry.. you havent entered the correct choice , Please try again later ")


input()
















