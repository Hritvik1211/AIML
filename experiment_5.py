import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('dataset/student-dataset.csv')

# Step 1: Select only numerical columns
numerical_data = data.select_dtypes(include=['float64', 'int64'])

# Step 2: Calculate correlation matrix on the numerical data
correlation_matrix = numerical_data.corr()

# Step 3: Visualize the correlation matrix
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix Heatmap")
plt.show()

# Print the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)
