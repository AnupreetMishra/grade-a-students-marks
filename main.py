# A school has following rules for grading system:
# a. Below 25 - F
# b. 25 to 45 - E
# c. 45 to 50 - D
# d. 50 to 60 - C
# e. 60 to 80 - B
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.


total_marks=int(input("Enter student's marks:"))
maximum_marks=100

if total_marks<25:
  print("Grade-F,You need to do study hard")
  
elif total_marks>25 and total_marks<45:
  print("Grade-E,Poor performance try to be better study hard")

elif total_marks>45 and total_marks<50:
  print("Grade-D,Average performance study well and grow your ability")

elif total_marks>50 and total_marks<60:
  print("Grade-C,Average performance try to be do better")

elif total_marks>60 and total_marks<80:
  print("Grade-B,Good performance study well")

else:
  print("Grade-A,Wonderfull performance keep it up")