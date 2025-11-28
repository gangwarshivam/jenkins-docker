# 2 Student Grades
# Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
# Add a new student and grade.
# Update an existing student’s grade.
# Print all student grades.


# dictionary with keys as student name and values are their grades
grade={'Shivam': 'A', 'Ravi': 'B', 'Shivansh': 'C', 'Rishav': 'D'}

print("Initial dictionary", grade)
# empty dictionary to take student and grade as input from user

emp={}

# user will chose the number of new records to be added

n=int(input("Enter number of student records you want to add: "))

i=0
for i in range(n):
    print(f"Enter the student name #{i+1}:")
    key=input()
    print(f"Enter grade for student {key}:")
    value=input()
    emp[key]=value

# Combining the emp dictionary with original grade dictionary
grade.update(emp)

print("Final dictionary is :", grade)

# Update an existing student grade
# Changing Student Ravi grades to F from B 

print("Changing Ravi grades to F")
grade['Ravi']="F"

# Printing all student grades
print("All student grades", grade)

