# PROGRAM TO STORE MARKS OF 7 STUDENTS ENTERED BY THE USER

# Initialize an empty list to store marks
marks = []

# Loop to collect marks of 7 students
for i in range(7):
    a = int(input(f"Enter marks of student {i + 1}: "))
    marks.append(a)

# Display the collected marks
print("Marks of students:", marks)
