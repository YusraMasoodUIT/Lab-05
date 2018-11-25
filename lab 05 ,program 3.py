print("Yusra Masood, 18B-093-CS , Section A")
print("Lab 05")
print("Program 3")

num = eval(input("Enter a number to execute while loop "))
# using while loop
sum1 = 0
count = 1
while count <= num :
    sum1 = sum1 + count
    count = count + 1

print("The total sum is " +str(sum1))
input()


number = eval(input("Enter a number for FOR loop " ))
# same program using for loop
sum3 = 0

for count in range(1 , num+1):
    sum3 = sum3 + count
    
print("The total sum is " +str(sum3))
input()
