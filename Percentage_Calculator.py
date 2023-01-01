print("Enter the marks of all six subjects, one by one ::")

num1= int(input("Enter the marks out of 100 obtained in subject-1: "))
num2= int(input("Enter the marks obtained out of 100 in subject-2: "))
num3= int(input("Enter the marks obtained out of 100 in subject-3: "))
num4= int(input("Enter the marks obtained out of 100 in subject-4: "))
num5= int(input("Enter the marks obtained in out of 100 subject-5: "))
num6= int(input("Enter the marks obtained in out of 100 subject-6: "))

total_marks= (num1+num2+num3+num4+num5+num6)

average_marks= (total_marks)/6

percentage_marks= ((total_marks/600)*100)

print("Total marks obtained: ",total_marks)
print("Average marks obtained: ",average_marks)
print("Percentage obtained: ",percentage_marks)