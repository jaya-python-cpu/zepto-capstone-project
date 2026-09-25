Analytics & Machine Learning:
Overview-

This module implements an end-to-end data analytics and machine learning pipeline using the Titanic dataset.

Workflow:

Data Loading → Data Cleaning → EDA → Visualization → Preprocessing → ML Models → Evaluation → Tuning

Key Tasks:

Loaded and profiled the Titanic dataset using Pandas and Seaborn.
Analyzed missing values and applied appropriate cleaning strategies.
Performed univariate and bivariate analysis.
Identified outliers using the IQR method.
Analyzed survival patterns based on gender and passenger class.
Created correlation heatmaps and multiple visualizations.
Built and evaluated:
Logistic Regression
Decision Tree
Random Forest
Compared model performance using Accuracy, Precision, Recall, F1 Score and AUC.
Compared class-imbalance strategies including class_weight='balanced' and SMOTE.
Performed Random Forest hyperparameter tuning using GridSearchCV.
Built a Linear Regression model to predict passenger fare.
Evaluated regression using MAE, RMSE, R² and Adjusted R².
Saved the complete best-performing ML pipeline using Joblib.
Preprocessing

The machine learning pipeline uses:

Missing-value imputation
One-hot encoding for categorical features
StandardScaler for numerical features
Stratified train/test split
Scikit-learn Pipeline and ColumnTransformer

All preprocessing steps are fitted only on the training data to prevent data leakage.

Files:

01_eda.ipynb – Data loading, cleaning and exploratory analysis
02_modeling.ipynb – Machine learning, evaluation and tuning
titanic.csv – Offline dataset
charts/ – Generated visualizations
models/ – Saved ML pipeline
