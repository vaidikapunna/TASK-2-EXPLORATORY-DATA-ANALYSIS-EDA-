import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Setting up the look of our plots
sns.set(style="whitegrid")

# Step 1: Load the dataset
print(" Loading the Titanic dataset...")
df = pd.read_csv("train.csv")
print(" Dataset loaded successfully!\n")

# Step 2: Peek into the dataset
print(" Let's take a look at the first few rows:")
print(df.head())

print("\n Summary statistics (the story of numbers):")
print(df.describe())

print("\n Checking for missing values:")
print(df.isnull().sum())

# Step 3: Handle missing data thoughtfully
print("\n🛠 Filling missing 'Embarked' values with the mode...")
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

print("🧹 Dropping 'Cabin' column since it's mostly empty...")
df.drop(columns=['Cabin'], inplace=True)

print(" Missing data handled!\n")

# Step 4: Let's get visual 📸

# Histogram - distribution of numeric features
print(" Plotting histograms...")
df.hist(bins=30, figsize=(10, 8), color='skyblue')
plt.suptitle("Histograms of Numeric Features", fontsize=16)
plt.tight_layout()
plt.savefig("histograms.png")
plt.show()

# Boxplot for Age
print(" Creating a boxplot for Age...")
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Age"], color='orchid')
plt.title("Boxplot of Age")
plt.savefig("boxplot_age.png")
plt.show()

# Boxplot of Age by Survival
print(" Age distribution by survival status...")
plt.figure(figsize=(6, 4))
sns.boxplot(x='Survived', y='Age', data=df, palette="Set2")
plt.title("Age vs Survival")
plt.savefig("boxplot_age_survived.png")
plt.show()

# Step 5: Correlation matrix — how features relate to one another
print(" Exploring relationships through correlation matrix...")
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=['number'])
numeric_df = df.select_dtypes(include=['number']).drop('PassengerId', axis=1)
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Heatmap")
plt.savefig("correlation_matrix.png")
plt.show()

# Step 6: Pairplot — mini stories between pairs of features
print(" Creating pairplot for selected features...")
sns.pairplot(df[['Survived', 'Pclass', 'Age', 'Fare']], hue='Survived')
plt.savefig("pairplot.png")
plt.show()

# Step 7: Interactive plot using Plotly
print(" Generating interactive age histogram with Plotly...")
fig = px.histogram(df, x='Age', color='Survived', nbins=30,
                   title="Interactive Age Distribution by Survival",
                   labels={'Survived': 'Survived (0 = No, 1 = Yes)'})
fig.write_html("interactive_age_plot.html")
fig.show()

print("\n Task Completed! Visuals saved.")


