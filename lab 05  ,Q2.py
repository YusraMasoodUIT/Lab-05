print("Yusra Masood, 18B-093-CS , Section A")
print("Lab 05")
print("Q2")

length = eval(input("Enter a value for the length of the rectangle "))
width = eval(input("Enter a value for the width of the rectangle "))
print("\n")
def Area(length , width):
    totarea = length * width
    print("The total area of the rectangle with length "+str(length)+
          " and width "+str(width)+" is "+str(totarea))

def Perimeter(length , width):
    perimeter = (2*length)+(2*width)
    print("The total perimeter is "+str(perimeter))

Area(length , width)
Perimeter(length , width)
input()
