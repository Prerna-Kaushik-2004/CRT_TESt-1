import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Name': ['John', 'Alice', 'Bob', 'Emma', 'Ryan'],
    'Age': [28, 24, 30, 26, 35],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
    'Salary': [50000, 60000, 55000, 62000, 72000],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Finance']
}

df = pd.DataFrame(data)

# 1. Calculate the average salary using NumPy
average_salary = np.mean(df['Salary'])
print("Average Salary:", average_salary)

# 2. Filter employees with salary greater than 60000
high_salary_employees = df[df['Salary'] > 60000]
print("\nEmployees with Salary greater than 60000:\n", high_salary_employees)

# 3. Plot department-wise average salary
avg_salary_by_dept = df.groupby('Department')['Salary'].mean()

plt.figure(figsize=(8,5))
plt.bar(avg_salary_by_dept.index, avg_salary_by_dept.values, color=['blue', 'green', 'red'])
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Department-wise Average Salary")
plt.show()
