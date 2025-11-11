Customer Churn Prediction Project
=================================

Goal
----

This project implements an end-to-end churn prediction model for an online tea retail store.

Project Structure & Getting Started
-----------------------------------

This project demonstrates two approaches to building a churn prediction model:

1. **Standalone Implementation** (`standalone.ipynb <standalone.ipynb>`_)
   - Complete scikit-learn pipeline with feature engineering and model training
   - Random Forest with GridSearchCV hyperparameter tuning
   - Model evaluation using AUC ROC
   - Inference using unseen data

2. **AWS SageMaker Implementation** (`AWS/ <AWS/>`_ subdirectory)
   - Production-ready pipeline using SageMaker Canvas (`AWS/churn.flow <AWS/churn.flow>`_) and Feature Store
   - Pipeline conversion and deployment notebook (`AWS/churn.ipynb <AWS/churn.ipynb>`_)
   - For detailed setup instructions, see `AWS/instructions.md <AWS/instructions.md>`_

