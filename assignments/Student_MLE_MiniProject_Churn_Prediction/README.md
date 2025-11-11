# Customer Churn Prediction Project

## Goal

This project implements an end-to-end churn prediction model for an online tea retail store to identify customers at risk of churning (discontinuing service). The goal is to enable proactive retention measures by predicting which customers are likely to leave.

## Project Structure & Getting Started

This project demonstrates two approaches to building and deploying a churn prediction model:

1. **Standalone Implementation** ([`standalone.ipynb`](standalone.ipynb))
   - Complete scikit-learn pipeline with feature engineering, model training, and evaluation
   - Random Forest with GridSearchCV hyperparameter tuning
   - Model evaluation using AUC ROC

2. **AWS SageMaker Implementation** ([`AWS/`](AWS/) subdirectory)
   - Production-ready pipeline using SageMaker Canvas ([`AWS/churn.flow`](AWS/churn.flow)) and Feature Store
   - Pipeline conversion and deployment notebook ([`AWS/churn.ipynb`](AWS/churn.ipynb))
   - For detailed setup instructions, see [AWS/instructions.md](AWS/instructions.md)
