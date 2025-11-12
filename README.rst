=============================================================
Springboard - Machine Learning for Engineers
=============================================================

Course Overview
---------------

This repository contains the complete coursework and projects from a **4-month intensive Springboard course titled "Machine Learning for Engineers"**. The curriculum covers fundamental machine learning concepts, from data exploration and feature engineering to deep learning, computer vision, NLP, and model deployment.

Course Curriculum
-----------------

The course curriculum is organized into 12 modules:

1. **Program Overview**
     * Required Sign-ups

2. **Intro to Machine Learning**
     * Fundamentals
     * Types of ML Problems
     * Stats vs ML
     * Deep Learning vs Machine Learning
     * Accuracy-Explainability Tradeoff
     * Visual Intro to ML

3. **Data Wrangling and Exploration**
     * EDA and Feature Engineering
     * Messy Data

4. **Machine Learning With Sklearn**
     * Decision Trees
     * Bagging and Ensembling
     * Random Forest
     * Gradient Boosting
     * Mini Project - Trees & Forests

5. **Model Evaluation**
     * Metrics for Model Performance
     * Evaluation Metrics
     * ROC-AUC
     * Building a Baseline
     * AutoML
     * Data Splitting
     * Model Generalization
     * Hyperparameter Tuning

6. **Deep Learning & Optimization**
     * Neural Networks
     * Gradient Descent

7. **Computer Vision**
     * Convolutional Neural Networks (CNNs)
     * Fine-Tuning CNNs
     * Image Segmentation and Object Detection
     * Vision Language Models

8. **Natural Language Processing**
     * NLP Introduction
     * Large Language Models

9. **Model Deployment**
     * ML Project Lifecycle

10. **Amazon Web Services**
      * Sagemaker

11. **Monitoring and Maintenance**

12. **Ethics and Bias**
      * Ethical Challenges
      * The Legal and Regulatory Landscape
      * Case Studies
      * AI Future Ethical Trends

Coursework
----------------

The course consisted of **6 mini projects** and **1 capstone project**, each designed to build practical machine learning skills through hands-on implementation:

Mini Projects
~~~~~~~~~~~~~~

1. **Exploratory Data Analysis** (`assignments/Student_MLE_MiniProject_EDA.ipynb <assignments/Student_MLE_MiniProject_EDA.ipynb>`_)
     * Performs comprehensive EDA on the NYC Taxi Dataset
     * Analyzes data structure, distributions, and relationships between variables
     * Applies statistical and visual techniques to uncover patterns and insights

2. **Logistic Regression** (`assignments/Student_MLE_MiniProject_Logistic_Regression.ipynb <assignments/Student_MLE_MiniProject_Logistic_Regression.ipynb>`_)
     * Implements logistic regression for binary classification on the Wisconsin Breast Cancer Detection dataset
     * Covers model training, evaluation, and interpretation of coefficients
     * Focuses on model evaluation and interpretation rather than implementation details

3. **Machine Learning Pipeline** (`assignments/Student_MLE_MiniProject_ML.ipynb <assignments/Student_MLE_MiniProject_ML.ipynb>`_)
     * Predicts total fare on the NYC Taxi Dataset
     * Builds baseline models, full ML models, and performs hyperparameter tuning
     * Uses Scikit-Learn pipelines for rapid experimentation

4. **Trees and Forests** (`assignments/Student_MLE_MiniProject_Trees_and_Forests.ipynb <assignments/Student_MLE_MiniProject_Trees_and_Forests.ipynb>`_)
     * Introduces Decision Trees, Random Forests, Bagging, and Boosting
     * Demonstrates ensemble methods for improved model performance

5. **Deep Learning with Keras** (`assignments/Student_MLE_MiniProject_Deep_Learning.ipynb <assignments/Student_MLE_MiniProject_Deep_Learning.ipynb>`_)
     * Builds a deep learning classifier using Keras to predict income from the Adult Income dataset
     * Covers data preprocessing, model architecture design, training, and evaluation

6. **Churn Prediction with AWS** (`assignments/Student_MLE_MiniProject_Churn_Prediction/ <assignments/Student_MLE_MiniProject_Churn_Prediction/>`_)
     * Implements an end-to-end churn prediction model for an online tea retail store
     * Demonstrates both standalone scikit-learn implementation and AWS SageMaker deployment
     * Includes production-ready pipeline using SageMaker Canvas and Feature Store

Capstone Project
~~~~~~~~~~~~~~~~

**Bitcoin Price Direction Prediction** (`capstone/ <capstone/>`_)
   * Predicts next-day Bitcoin price direction using momentum indicators and technical analysis
   * Implements comprehensive feature engineering (volatility, volume, momentum indicators)
   * Compares baseline models (Logistic Regression, Random Forest, ARIMA) with deep learning models (Feedforward NN, LSTM)
   * Uses proper time series validation to prevent data leakage
   * Achieves meaningful predictive performance with a defensive bias useful for risk management

   See `capstone/README.rst <capstone/README.rst>`_ for detailed project documentation.

Repository Structure
--------------------

::

    springboard-package/
    ├── assignments/          # 6 mini projects
    │   ├── Student_MLE_MiniProject_EDA.ipynb
    │   ├── Student_MLE_MiniProject_Logistic_Regression.ipynb
    │   ├── Student_MLE_MiniProject_ML.ipynb
    │   ├── Student_MLE_MiniProject_Trees_and_Forests.ipynb
    │   ├── Student_MLE_MiniProject_Deep_Learning.ipynb
    │   └── Student_MLE_MiniProject_Churn_Prediction/
    ├── capstone/              # Capstone project
    │   ├── 0_EDA.ipynb
    │   ├── 1_Features_and_Target.ipynb
    │   ├── 2_Baseline.ipynb
    │   ├── 3_Model.ipynb
    │   └── README.rst
    └── README.rst             # This file

