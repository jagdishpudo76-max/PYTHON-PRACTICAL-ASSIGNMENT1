import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
df = pd.read_csv("C:/Users/JAGDEESH PUDO/Desktop/MCA1/JAGDISH PUDO/PYTHON/PRACTICAL 1/employee_data.csv")

# histogram for Salary
plt.hist(df["Salary"])
plt.title("Salary Distribution")
plt.show()

# box plot for Age
sns.boxplot(x=df["Age"])
plt.title("Age Box Plot")
plt.show()

# bar chart for department-wise employee count
df["Department"].value_counts().plot(kind="bar")
plt.title("Employees per Department")
plt.show()

# scatter plot between Experience and Salary
plt.scatter(df["Experience"], df["Salary"])
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")
plt.show()

# correlation heatmap
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()
