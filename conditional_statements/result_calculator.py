# STUDENT RESULT CALCULATOR BASED ON AVERAGE MARKS

# Input marks for three subjects
physics = int(input("Enter Physics marks [Out of 100]: "))
chemistry = int(input("Enter Chemistry marks [Out of 100]: "))
maths = int(input("Enter Maths marks [Out of 100]: "))

# Calculate average percentage
average = (physics + chemistry + maths) / 3

# Display result based on average
if average >= 33:
    print(f"✅ Passed! Your average is: {average:.2f}%")
else:
    print(f"❌ Failed. Your average is: {average:.2f}%")
