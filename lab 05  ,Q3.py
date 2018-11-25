print("Yusra Masood , 18B-093-CS , Section A ")
print("lab 5")
print("Q3")

print("Program to calculate the arithmetic sequence ")
a1 = eval(input("Enter the first term  "))
diff= eval(input("Enter the common difference  "))
num= eval(input("Enter the number of terms  "))
an = (a1 + ((num - 1)*diff))
print("the nth term of sequence is  " + str(an))
x= input("Do you want to continue ")
while x == "yes" :
    num = eval(input("Enter the number of terms  "))
    an = (a1 + ((num - 1)*diff))
    print("the nth term of sequence is  " + str(an))
    x= input("Do you want to continue ")
    if x == "no":
        break 
print("\n\n\n")
input()
