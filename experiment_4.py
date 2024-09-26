import pandas as pd

# Import
data = pd.read_csv('dataset/student-dataset.csv')

# Details of the dataset
print("Number of Rows and Columns:", data.shape)
print("First Five Rows:")
print(data.head())
print("Dataset Size (Total Elements):", data.size)
print("Number of Missing Values:")
print(data.isnull().sum())

# Sum, Average, Min, and Max from numerical columns
print("Sum of Numerical Columns:")
print(data.sum(numeric_only=True))

print("Average of Numerical Columns:")
print(data.mean(numeric_only=True))

print("Minimum Values in Numerical Columns:")
print(data.min(numeric_only=True))

print("Maximum Values in Numerical Columns:")
print(data.max(numeric_only=True))

# Export the data (saving to CSV file)
data.to_csv('exported_data.csv', index=False)
