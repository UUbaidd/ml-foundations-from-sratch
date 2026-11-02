
# 📈 Linear Regression — From Scratch & Scikit-learn

Implementation of Linear Regression using Python and NumPy, followed by an implementation using Scikit-learn.

The objective is to understand the mathematical foundations, optimisation process, and practical implementation of Linear Regression.

## 1. Overview

Linear Regression is a supervised learning algorithm used to predict continuous numerical values by modelling a linear relationship between input features and a target variable.

This project explores:

- Linear Regression with multiple input features
- Prediction using matrix multiplication
- Mean Squared Error (MSE)
- Gradient calculation using partial derivatives
- Training and convergence
- Implementation using Scikit-learn
- Comparison between implementations

## 2. NumPy Implementation — From Scratch

**File:** `scratch-linear-regression.py`

The implementation includes:

1. Weight and bias initialisation
2. Prediction function
3. Mean Squared Error loss function
4. Analytical gradient calculation
5. Gradient Descent parameter updates
6. Training loop with configurable learning rate and epochs
7. Loss history tracking and visualisation

## 3. Scikit-learn Implementation

**File:** `sklearn_implementation.py`

Linear Regression was implemented using Scikit-learn.

Main operations:

- `LinearRegression()` — Create the model
- `model.fit(X, y)` — Fit the model
- `model.coef_` — Retrieve learned weights
- `model.intercept_` — Retrieve learned bias
- `model.predict(X)` — Generate predictions
- `mean_squared_error(y, y_pred)` — Evaluate predictions

Scikit-learn's LinearRegression uses a least-squares solver rather than the manually implemented Gradient Descent training loop.


## 7. Key Learnings

- Understanding Linear Regression mathematically and computationally
- Deriving and applying gradients
- Understanding the influence of learning rate and epochs
- Working with multiple features and NumPy array shapes
- Understanding model convergence
- Comparing Gradient Descent with least-squares solvers
- Using Scikit-learn for fitting, prediction, and evaluation

## 9. Technologies

- Python
- NumPy
- Matplotlib
- Scikit-learn

---

This project is part of my ongoing [Machine Learning Foundations — From Scratch](https://github.com/UUbaidd/ml-foundations-from-sratch) repository.
