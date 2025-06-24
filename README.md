
# titanic - Exploratory Data Analysis (EDA)
I'm Vaidika, and this is my submission for Task 2 of my AI/ML Internship. In this task, I performed Exploratory Data Analysis (EDA) on the famous Titanic dataset to discover patterns and insights about the passengers and their chances of survival.

This project includes the following files:
├── titanic_eda.py # Python script that performs the EDA
├── README.md # This file (project explanation)
└── train.csv # Titanic dataset used for analysis

---

##  What I Did (Step by Step)

1. **Loaded the dataset** using `pandas`.
2. **Cleaned the data**:
   - Filled missing values in the `Embarked` column using the most common value.
   - Dropped the `Cabin` column since most of its data was missing.
3. **Explored the data** through:
   - Summary statistics (mean, median, etc.)
   - Histograms for numeric columns
   - Boxplots to show age distribution by survival
4. **Used Seaborn and Matplotlib** to create visualizations that explain the relationships in the data.
5. **Created an interactive age distribution chart** using Plotly for better understanding.

---

##  What I Observed

- Most passengers who survived were **women** and **children**.
- Passengers in **1st class** had a higher survival rate compared to those in 3rd class.
- **Younger passengers** (below 15) had better chances of survival.
- There’s a strong relationship between **Fare**, **Pclass**, and **Survival**.

---

## Tools & Libraries Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly

 How to Run This Project

1. Make sure you have Python installed.
2. Download the files into a folder.
3. Open a terminal or command prompt in that folder.
4. Run the following command:

```bash
python titanic_eda.py

# TASK-2-EXPLORATORY-DATA-ANALYSIS-EDA-
de8a5ca57a36cbb6b7baaa07360aeb1e089fd62c
