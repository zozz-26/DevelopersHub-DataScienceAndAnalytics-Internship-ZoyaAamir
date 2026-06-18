## Task 2: Credit Risk Prediction

Predicted whether a loan applicant is likely to default on a loan using the Loan Prediction Dataset from Kaggle.

### Approach
- Handled missing values using mode (categorical) and median (numerical)
- Visualized Loan Amount, Education, and Applicant Income
- Applied Label Encoding to convert categorical columns to numbers
- Split data 80/20 for training and testing
- Trained Logistic Regression model
- Evaluated using accuracy score and confusion matrix

### Results & Insights
- Model achieved 78.86% accuracy
- Credit History is the most important factor (coefficient: 3.28)
- Model predicts approvals well but struggles with rejections
