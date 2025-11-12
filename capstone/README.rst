Bitcoin Price Direction Prediction
===================================

Problem Statement
-----------------

Predicting short-term price movements in financial markets is one of the most challenging problems in quantitative finance. This capstone project focuses on predicting the next-day price direction of Bitcoin using momentum indicators and technical analysis features. The goal is to build a machine learning model that can identify patterns in historical price and volume data to forecast whether Bitcoin will move up, down, or remain relatively stationary on the following trading day.

The challenge lies in the inherent noise and randomness of financial markets, where even small predictive edges can be valuable when combined with proper risk management. This project explores whether momentum indicators and deep learning models can extract meaningful signals from Bitcoin's price history.

Goals
-----

The primary goals of this capstone project are:

1. **Feature Engineering**: Create a comprehensive set of momentum indicators, volatility measures, and volume-based features from historical OHLC (Open, High, Low, Close) and volume data.

2. **Target Definition**: Develop a robust 3-class target variable that filters out noise by only classifying significant price movements (≥1% change) while treating smaller movements as "stationary."

3. **Model Comparison**: Evaluate and compare multiple modeling approaches, from traditional machine learning baselines (Logistic Regression, Random Forest) to deep learning architectures (Feedforward Neural Networks, LSTM).

4. **Time Series Validation**: Implement proper time-aware data splitting and validation to prevent data leakage and ensure realistic performance estimates.

5. **Performance Analysis**: Assess model performance using appropriate metrics for multi-class classification, including ROC-AUC curves, confusion matrices, and classification reports.

Project Structure & Notebooks
------------------------------

This project is organized into four sequential notebooks that build upon each other:

1. **`0_EDA.ipynb <0_EDA.ipynb>`_** - Exploratory Data Analysis
   * Loads and examines raw OHLC (Open, High, Low, Close) and volume data
   * Visualizes price movements and trading volume over time
   * Identifies data quality issues, missing values, and temporal patterns
   * Prepares the dataset for feature engineering by sorting chronologically and setting date as index

2. **`1_Features_and_Target.ipynb <1_Features_and_Target.ipynb>`_** - Feature Engineering and Target Definition
   * **Momentum Indicators**: Creates moving averages (EMA), crossover signals, Bollinger Bands, and RSI (Relative Strength Index)
   * **Volatility Features**: Computes Average True Range (ATR) and realized volatility measures
   * **Volume Features**: Calculates On-Balance Volume (OBV) and Volume-Weighted Average Price (VWAP)
   * **Price Position Features**: Determines price position within recent high/low ranges
   * **Target Definition**: Creates a 3-class target variable:
     - **Class 0 (Down)**: Price decrease ≤ -1%
     - **Class 1 (Stationary)**: Price change between -1% and +1%
     - **Class 2 (Up)**: Price increase ≥ +1%
   * This 3-class approach filters out noise from small price movements and focuses on significant directional changes

3. **`2_Baseline.ipynb <2_Baseline.ipynb>`_** - Baseline Model Evaluation
   * Implements time-aware cross-validation using `TimeSeriesSplit` to prevent data leakage
   * Tests traditional machine learning baselines:
     - **Logistic Regression**: Linear classifier with multinomial loss for 3-class classification
     - **Random Forest**: Ensemble method with class balancing to handle class imbalance
     - **ARIMA**: Traditional time series forecasting model (converted to direction predictions)
   * Evaluates models using ROC-AUC, accuracy, F1-scores, and confusion matrices
   * Provides feature importance analysis to identify which indicators are most predictive

4. **`3_Model.ipynb <3_Model.ipynb>`_** - Deep Learning Models
   * Creates sequences of 50 timesteps for time series modeling (uses past 50 days to predict next day)
   * Implements proper scaling order: create sequences → split train/test → scale using only training data
   * Trains two neural network architectures:
     - **Simple Feedforward Network**: Flattens sequences and uses dense layers (16 → 8 → 4 → 3 neurons)
     - **LSTM Network**: Preserves temporal structure with LSTM layer (32 units) followed by dense layers
   * Evaluates models with comprehensive metrics:
     - Multi-class ROC curves (one-vs-rest) with per-class AUC scores
     - Confusion matrices and classification reports
     - Time series plots comparing predictions vs. actual values
   * Results show LSTM achieves better performance (micro-average AUC 0.68) with a defensive bias, excelling at predicting downward movements (AUC 0.73) and stationary periods (AUC 0.65) while struggling with upward movements (AUC 0.50)

Key Findings
-------------

* The LSTM model demonstrates superior performance compared to baseline models, achieving a micro-average AUC of 0.68
* Models show a **defensive bias**, performing best at identifying downward price movements and stationary periods, which could be valuable for risk management
* Proper time series validation and feature scaling order are critical to prevent data leakage and obtain realistic performance estimates
* The 3-class target definition (filtering movements <1%) helps reduce noise and focus on significant price changes
* Even moderate predictive edges (55-60% accuracy) can be valuable when combined with proper position sizing and risk management

