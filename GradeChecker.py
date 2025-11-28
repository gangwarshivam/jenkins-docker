# 
# 1. Grade Checker
# Take a score as input and print the grade based on the following:
# 90+ : "A"
# 80-89 : "B"
# 70-79 : "C"
# 60-69 : "D"
# Below 60 : "F"
# here we used a basic if else statement to carry out marks and all.


def grade_checker(score):
    score=int(score)
    if score>=90:
        print("A")
    elif score >=80 and score<=89:
        print("B")
    elif score >=70 and score<=79:
        print("C")
    elif score >=60 and score<=69:
        print("D")
    else:
        print("F")
    
    
marks=int(input("Enter your score:"))
grade_checker(marks)