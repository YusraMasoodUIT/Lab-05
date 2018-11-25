print("Yusra Masood , 18B-093-CS , Section A ")
print("lab 5")
print("Q5")
print("\n")
print("Marksheet")
print("\n")
name = input("Enter your name ")
fname = input("Enter your father name ")
rollnum = eval(input("Enter your roll number "))
subj = []
x = 1
avg = 0

numofsubj = eval(input("Enter your total number of subjects "))
while x != numofsubj+1:
    subname1 = input("Enter your "+str(x) + " subject name " )
    marks = eval(input("Enter your subject marks "))
    subj.append(subname1)
    avg = avg + marks
    x = x + 1
    if x == numofsubj+1:
        break


totmarks = numofsubj *100   
perc= ((avg/totmarks)*100)
if perc >= 90:
    grade = 'A*'
elif perc >= 80:
    grade  = 'A'
elif perc >= 70:
    grade  = 'B'
elif perc >= 60:
    grade  = 'C'
elif perc >= 50:
    grade  = 'D'
else:
    grade = 'F'

  


print("\n\n\n\n")


print("Name :- " +name)
print("Father's Name :- " +fname)
print("Roll # :- " +str(rollnum))
print("Subject Names :- " +str(subj))
print("Total marks:- " +str(totmarks))
print("Obtained marks:- " +str(avg))
print("Your Percentage is :- " +str(perc))
print("Your overall Grade is :- " + grade)

input()
