# Regression Models for Dataset Prediction

This project involves preprocessing a dataset and applying several regression models to predict outcomes. The notebook demonstrates the use of various regression techniques to evaluate their performance and compare their effectiveness.

## Overview

The notebook follows these steps:

1. **Data Preprocessing**: 
   - Load the dataset.
   - Handle missing values and duplicates.
   - Feature engineering and transformation.

2. **Model Training**:
   - **Linear Regression**: Trains a linear regression model and evaluates its performance. Accuracy: 0.7215985462656012
   - **Decision Tree Regressor**: Trains a decision tree regressor and evaluates its performance.Accuracy: 0.9793106551145742
   - **Random Forest Regressor**: Trains a random forest regressor and evaluates its performance. Accuracy: 0.9786961383626938
   - **Support Vector Regressor (SVR)**: Trains an SVR model and evaluates its performance. Accuracy: 0.7656820765977232
   - **Extra Trees Regressor**: Trains an extra trees regressor and evaluates its performance. Accuracy: 0.9788756023512171

## Data

- The dataset used is assumed to be in a CSV file format. The file is named `data.csv`.

## Installation

To run this notebook, ensure you have the following Python packages installed:

- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`

You can install these packages using pip:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn
