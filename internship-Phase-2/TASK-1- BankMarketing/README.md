## Task 1: Term Deposit Subscription Prediction (Bank Marketing)

Predicted whether a bank customer will subscribe to a term deposit using the UCI Bank Marketing Dataset (41,188 records).

### Approach
- Cleaned dataset by replacing 'unknown' values with mode
- Performed EDA on subscription count, job types, and age distribution
- Encoded categorical features using Label Encoding
- Trained two models: Logistic Regression and Random Forest
- Evaluated using Accuracy, F1-Score, Confusion Matrix, and ROC Curve
- Used SHAP to explain model predictions (Explainable AI)

### Results & Insights
- Random Forest outperformed Logistic Regression (91.7% accuracy, 0.59 F1, 0.94 AUC)
- Dataset was highly imbalanced (~11% subscriptions), making F1-Score the key metric
- SHAP identified call duration as the strongest predictor, followed by economic indicators
- Explained 5 individual predictions using SHAP force plots
