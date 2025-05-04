# 🏠 Loan Prediction Problem

A machine learning project focused on binary classification, designed to automate the loan eligibility process for a housing finance company. This solution involves structured steps including data analysis, pre-processing, feature engineering, and model building.
# 📌 Problem Statement

Dream Housing Finance is a company that offers home loans across urban, semi-urban, and rural areas. Currently, customers apply for loans via an online form. The company aims to automate the real-time prediction of loan eligibility based on customer details. These customer details include:

| Feature                    | Description                                      |
|----------------------------|--------------------------------------------------|
| Gender                     | Applicant's gender                              |
| Marital Status             | Whether the applicant is married or single      |
| Education                  | Education level of the applicant                |
| Number of Dependents       | Total number of dependents                      |
| Applicant & Co-applicant Income | Combined income of applicant and co-applicant |
| Loan Amount                | Amount of loan requested                        |
| Loan Term                  | Duration of the loan in months or years         |
| Credit History             | Record of previous credit performance           |
| Property Area              | Location category: Urban, Semi-urban, or Rural  |
| Others                     | Additional relevant attributes                  |


# 🔍 Objetive

The objective is to identify customer segments eligible for loans, enabling targeted services and faster decision-making.

## Hypothesis
The initial hypothesis is that a higher income coming from the applicant and co-applicant would correlate with an increased probability of approval.

# 📊 Project Overview

## 1. Introduction

This project addresses a binary classification problem, where the goal is to predict whether a customer is eligible for a loan (```Yes``` or ```No```), based on historical data.

## 2. Exploratory Data Analysis (EDA) & Pre-processing

- Thorough data inspection and visualisation.
- Handling of missing values and outliers.
- Transformation of categorical variables.
- Data scaling and preparation for modelling.

## 3. Feature Engineering & Model Building

- Creation of new relevant features to enhance predictive performance.
- Comparison of various classification algorithms.
- Evaluation using accuracy, precision, recall, and ROC-AUC score.
- Final model selection based on performance metrics

## 4. Variable description

![Image](https://github.com/user-attachments/assets/c1030713-c554-4eca-8eae-54a9d98567cc)

## 5. Evaluation Metrics

The process of model development is incomplete without a thorough evaluation of its performance. In the context of a classification task, performance can be assessed using various evaluation metrics. One commonly used approach involves the confusion matrix, which provides a tabular summary comparing actual and predicted classifications. This allows for a clearer understanding of the model’s effectiveness across different outcome categories.
    
![Image](https://github.com/user-attachments/assets/4ec525c9-d02c-45b3-b711-17ea741132f6)

- True Positive – Targets which are actually true(Y) and we have predicted them as true(Y)
- True Negative – Targets that are actually false(N) and we have predicted them as false(N)
- False Positive – Targets that are actually false(N) but we have predicted them as true(T)
- False Negative – Targets that are actually true(T) but we have predicted them as false(N)

## Definitions:

- **Accuracy**: To assess the performance of the model, it is important to determine the number of instances where the predictions align with the actual classes, both positive and negative. The accuracy metric, which quantifies the proportion of correctly predicted instances, should be maximised. By utilising these values, the overall accuracy of the model can be calculated.

- **Precision:** It is a measure of accuracy in true predictions, indicating the proportion of observations labelled as true that are indeed correctly identified as true.

- **Recall (Sensitivity):** It represents the proportion of actual observations that are correctly predicted, specifically indicating how many instances of the true class are accurately labelled. This metric is also referred to as ```Sensitivity```.

- **Specificity:** It is a measure of how many observations of false class are labeled correctly.

**_NOTE: Specificity and sensitivity are fundamental in the derivation of the ROC curve. These metrics can be calculated as demonstrated below:_**

![Image](https://github.com/user-attachments/assets/17c197cc-e147-41e5-a92e-561b997b8029)

- **Receiver Operating Characteristic(ROC):** The model’s performance is assessed by evaluating the trade-offs between the true positive rate (sensitivity) and the false positive rate (1 - specificity). This analysis provides insight into the model’s ability to correctly identify positive cases while minimising the occurrence of false positives. The balance between these metrics is crucial for understanding the model’s effectiveness in different scenarios, and allows for the optimisation of its predictive accuracy based on the specific requirements of the task at hand.

- **The area under the curve (AUC):** The metric, often termed the accuracy index (A) or concordance index, is widely recognised as an optimal performance measure for the ROC curve. A larger area under the curve (AUC) signifies enhanced predictive performance of the model. The following provides an illustration of a typical ROC curve:

![Image](https://github.com/user-attachments/assets/fcc92da2-071a-47b0-9a14-386524c6de84)

- The area under the curve (AUC) quantifies the model's ability to correctly classify both true positives and true negatives. Ideally, the model should predict true classes as true and false classes as false.

- It is essential to consider both the true positive rate and the false positive rate. While a true positive rate of 1 is desirable, it is equally important to ensure that false classes are accurately predicted as false, maintaining a low false positive rate.

- Maximising the area under the curve is a key objective, with the optimal performance observed for classes 2, 3, 4, and 5 in the example provided.

- For class 1, when the false positive rate is 0.2, the true positive rate is approximately 0.6. In contrast, for class 2, the true positive rate reaches 1 at the same false positive rate, resulting in a higher AUC for class 2. Therefore, the model for class 2 demonstrates superior performance.

- The models for classes 2, 3, 4, and 5 are expected to deliver more accurate predictions compared to those for classes 0 and 1, as reflected by the higher AUC for these classes.


# 🗂️ File Structure (pending on the final modification)

```bash
├── data/
│   └── dataset.csv
├── notebooks/
│   └── analysis_and_modelling.ipynb
├── outputs/
│   ├── predictions/
│   └── plots/
├── README.md
└── requirements.txt
```
# 🚀 How to Run (pending to correct)

- Clone this repository.
- Install dependencies: `pip install -r requirements.txt` or `conda install --file requirements.yml`

## 👌 Explanation

```pip```: For standard Python virtual environments (requirements.txt)

```conda```: If you're using Anaconda/Miniconda and prefer to work with .yml environment files (requirements.yml)
# 📈 Output Plot (Pending on modification)

As can be observed, there is a strong linear relationship between the independent variable (X) and the dependent variable (Y). This indicates that the linear regression model performs well on the test data, demonstrating good generalisation, low error, and a strong linear fit.

### Training set (PENDINENTES DE AGREGAR IMAGENES)
![Alt Text](/Users/alberto/Documents/Coding/7_DataScience_ML_projects/Linear_Regression/1_Simple_Linear_regression/Images/training_results.png)

### Testing set
![Alt Text](/Users/alberto/Documents/Coding/7_DataScience_ML_projects/Linear_Regression/1_Simple_Linear_regression/Images/testing_results.png)

## 🧪 Model and Evaluation Metrics:

The metrics used in this projects were ```accuracy``` and ```F1 score``` to have a point of comparison. 

### 🔹 Accuracy
The percentage of correct predictions out of all predictions.

    ✅ Use when classes are balanced (roughly equal positive/negative cases).
    ⚠️ Not reliable when data is imbalanced (e.g., 90% no-loan, 10% loan).

### 🔹 F1 Score

The balance between precision and recall.

    ✅ Best for imbalanced datasets, as it considers both false positives and false negatives.
    ✅ A higher F1 score means better performance in correctly identifying the positive class while minimising both types of errors.

# 📈 Results and conclusions

| **Model**               | **Accuracy** | **F1 Score** |
|-------------------------|--------------|--------------|
| **Logistic Regression**  | 78.38%       | 85.51%       |
| **Random Forest**        | 77.30%       | 84.21%       |
| **XGBoost Classifier**   | 75.14%       | 82.58%       |

- Logistic Regression performed best overall, with the highest ```accuracy``` and ```F1 score```.
- All models showed similar performance, but ```Logistic Regression``` had a slight edge.
- Since ```F1 score``` is prioritised for imbalanced classification, ```Logistic Regression``` is the most reliable choice in this scenario.
## 📦 Libraries

- ```Pandas```
- ```Numpy```
- ```Matplotlib```
- ```Scikit-learn```
- ```Seaborn```
- ```Jupyter Notebook```
- ```XGBoost```
- ```OrderedDict```
- ```sys``` & ```os``` - For handling system-specific parameters and file paths.


## Additional Libraries
XGBoost – A powerful gradient boosting algorithm for classification and regression.

OrderedDict – A dictionary that remembers the order of key insertion.

sys & os – For handling system-specific parameters and file paths.

## 👨‍💻 Author

Made with ❤️ by Alberto AJ - AI/ML Engineer.

## 📢 Bonus: GitHub Badges

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/ML-ScikitLearn-orange?logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
