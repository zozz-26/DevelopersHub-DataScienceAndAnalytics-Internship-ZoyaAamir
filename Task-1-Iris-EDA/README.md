# DevelopersHub Data Science & Analytics Internship
**Intern:** Zoya Aamir

---

## Task 1: Iris Dataset - Exploratory Data Analysis

### Objective
Understand how to read, summarize, and visualize a dataset.

### Approach
- Loaded Iris dataset using Seaborn's built-in load_dataset() function into a Pandas DataFrame
- Inspected dataset structure using .shape (150 rows, 5 columns), .columns (sepal length, sepal width, petal length, petal width, species) and .head() (first 5 rows)
- Analyzed summary statistics using .describe() — mean, std, min, max, and percentiles
- Scatter plot: analyzed relationship between sepal length and petal length across 3 species
- Histogram: examined distribution of sepal length across all 150 flowers
- Box plot: detected outliers and spread of petal length by species
  
### Results & Insights
- Setosa has the smallest petal size with least variation
- Virginica has the largest petal size with most variation
- Positive correlation exists between sepal length and petal length
- Outliers detected in Setosa and Versicolor species
