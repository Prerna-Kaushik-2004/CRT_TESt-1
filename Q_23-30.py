import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Creating the dataset
data = {
    'Student Name': ['John', 'Sarah', 'David', 'Emily'],
    'Math': [80, 95, 70, 85],
    'Science': [75, 85, 65, 90],
    'English': [90, 80, 75, 88],
    'History': [70, 85, 80, 92]
}

df = pd.DataFrame(data)

# 1. Calculate the mean score of each subject using NumPy
mean_scores = df.iloc[:, 1:].mean()
print("\nMean Score of Each Subject:\n", mean_scores)

# 2. Calculate the average score of each student
df['Average Score'] = df.iloc[:, 1:].mean(axis=1)
print("\nAverage Score of Each Student:\n", df[['Student Name', 'Average Score']])

# 3. Find the student with the highest overall score
highest_scorer = df.loc[df['Average Score'].idxmax()]
print("\nStudent with the Highest Overall Score:\n", highest_scorer[['Student Name', 'Average Score']])

# 4. Scatter plot for Math vs Science scores
plt.figure(figsize=(6,4))
plt.scatter(df['Math'], df['Science'], color='blue', marker='o')
plt.xlabel("Math Scores")
plt.ylabel("Science Scores")
plt.title("Math vs Science Scores")
plt.grid(True)
plt.show()

# 5. Standardize the scores
standardized_scores = (df.iloc[:, 1:5] - df.iloc[:, 1:5].mean()) / df.iloc[:, 1:5].std()
print("\nStandardized Scores:\n", standardized_scores)

# 6. Visualize total scores using a bar plot
df['Total Score'] = df.iloc[:, 1:5].sum(axis=1)
plt.figure(figsize=(6,4))
plt.bar(df['Student Name'], df['Total Score'], color=['red', 'green', 'blue', 'purple'])
plt.xlabel("Student Name")
plt.ylabel("Total Score")
plt.title("Total Scores of Students")
plt.show()

# 7. Generate a pie chart for subject-wise average scores
plt.figure(figsize=(6,6))
plt.pie(mean_scores, labels=mean_scores.index, autopct='%1.1f%%', colors=['blue', 'green', 'red', 'purple'])
plt.title("Subject-wise Average Scores")
plt.show()

# 8. Display students whose History score is greater than the average History score
average_history = mean_scores['History']
high_history_students = df[df['History'] > average_history]
print("\nStudents with History Score Greater than Average:\n", high_history_students[['Student Name', 'History']])
