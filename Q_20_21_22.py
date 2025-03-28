import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 40],
    'Department': ['HR', 'IT', 'Sales', 'HR', 'IT'],
    'Salary': [50000, 70000, 45000, 52000, 80000]
}

df = pd.DataFrame(data)

# 1. Plot a bar chart to visualize the number of employees in each department
employee_count = df['Department'].value_counts()
plt.figure(figsize=(8,5))
plt.bar(employee_count.index, employee_count.values, color=['blue', 'green', 'red'])
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Number of Employees in Each Department")
plt.show()

# 2. Filter employees with salary greater than 60,000
high_salary_employees = df[df['Salary'] > 60000]
print("\nEmployees with Salary greater than 60,000:\n", high_salary_employees)

# 3. Create a line graph for the salary trend by department
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()
plt.figure(figsize=(8,5))
plt.plot(avg_salary_by_dept.index, avg_salary_by_dept.values, marker='o', linestyle='-', color='purple')
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Salary Trend by Department")
plt.grid(True)
plt.show()