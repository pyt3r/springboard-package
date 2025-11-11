# Customer Churn Prediction Project

## Goal

This project implements an end-to-end churn prediction model for an online tea retail store to identify customers at risk of churning (discontinuing service). The goal is to enable proactive retention measures by predicting which customers are likely to leave.

## Project Structure

This project demonstrates two approaches to building and deploying a churn prediction model:

1. **Standalone Implementation** ([`standalone.ipynb`](standalone.ipynb))
   - Complete machine learning pipeline using scikit-learn
   - Feature engineering, model training, and evaluation
   - Random Forest with hyperparameter tuning

2. **AWS SageMaker Implementation** ([`AWS/`](AWS/) subdirectory)
   - Production-ready pipeline using SageMaker Canvas and Feature Store
   - Visual workflow design with Canvas ([`AWS/churn.flow`](AWS/churn.flow))
   - Feature Store pipeline ([`AWS/churn.ipynb`](AWS/churn.ipynb))
   - For detailed setup and execution instructions, see [AWS/instructions.md](AWS/instructions.md)

## Getting Started

### Standalone Implementation

The standalone implementation is available in [`standalone.ipynb`](standalone.ipynb). It includes:
- Feature engineering (5 high-impact features)
- Random Forest and Logistic Regression models
- Hyperparameter tuning with GridSearchCV
- Model evaluation with AUC ROC

### AWS SageMaker Implementation

For detailed instructions on setting up and running the SageMaker implementation, see [AWS/instructions.md](AWS/instructions.md).

The AWS implementation includes:
- SageMaker Canvas workflow ([`AWS/churn.flow`](AWS/churn.flow))
- Feature Store pipeline ([`AWS/churn.ipynb`](AWS/churn.ipynb))
- Production-ready deployment capabilities
