# Task 4: Predicting Insurance Claim Amounts

## Objective
Predicted medical insurance charges based on personal data using Linear Regression.

### Approach
- Checked for missing values (none found)
- Encoded categorical columns (sex, smoker, region) using Label Encoding
- Visualized impact of BMI, Age, and Smoking status on charges using scatter plots and box plot
- Split data 80/20 for training and testing
- Trained Linear Regression model
- Evaluated using MAE and RMSE

### Results & Insights
- MAE: 4186.51, RMSE: 5799.59
- Smoking status is the most influential factor (coefficient: 23647) — smokers pay significantly higher charges
- Age and BMI have moderate positive impact on charges
- Children, sex, and region have minimal impact
