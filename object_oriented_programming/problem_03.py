# Define a class called employee
class employee:

    # Class variables: base salary and percentage increase
    salary = int(200)
    increase = int(20)

    # Define a property to calculate salary after the increase
    @property
    def salaryafterincrease(self):
        return (self.salary + self.salary * (self.increase / 100))
    
    # Define a setter to adjust the 'increase' percentage when a new salary is set
    @salaryafterincrease.setter
    def salaryafterincrease(self, newsalary):
        self.increase = ((newsalary / self.salary) - 1) * 100

# Create an instance of employee
ram = employee()

# Access the salary after applying the increase
new_salaray = ram.salaryafterincrease

# Print the current increase percentage
print(ram.increase)
