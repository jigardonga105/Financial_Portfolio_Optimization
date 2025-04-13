# 📈 Financial Portfolio Optimization using Machine Learning

## 📝 Summary / Abstract

This project aims to develop a machine learning-based model for dynamically optimizing financial portfolios for small and mid-level investors. By adjusting asset allocations across mutual funds, gold bonds, government securities, and hybrid funds based on historical and current market data, the model seeks to maximize returns while managing risks. The approach addresses the limitations of static models and enhances flexibility in response to market fluctuations.

---

## 🏁 Introduction

Traditional portfolio management techniques often fail to adapt to rapidly changing market conditions, making them ineffective for small and mid-level investors. This project proposes a data-driven model that dynamically optimizes portfolio allocations, improving the balance of risk and return across multiple asset classes.

---

## 🎯 Motivation

Small and mid-sized investors lack access to advanced financial advisory tools, making it challenging to navigate market volatility. This project aims to bridge this gap by providing an accessible solution for dynamic portfolio optimization.

---

## 🥅 Objective

The main objective of this project is to develop a machine learning model that:

1. Adapts to real-time market data.  
2. Integrates multiple asset types (mutual funds, gold bonds, etc.).  
3. Addresses different risk profiles (low, medium, high).  
4. Maximizes returns while managing risks effectively.  

---

## ⚙️ Methodology

### 📊 Data Sources

- **Nifty 50 Stock Data**: Yahoo Finance, NSE  
- **Index Data**: Yahoo Finance, RBI  
- **Mutual Fund Data**: Yahoo Finance  
- **Gold Bond Data**: Yahoo Finance, RBI  
- **Fixed Deposit Data**: RBI, Banks' websites  

---

### 📚 Data Preparation

- **Data Cleaning**: Handling missing data and outliers.  
- **Feature Selection**: Using **Random Forest**.  
- **Scaling**: Standardizing data for model compatibility.  

---

### 🧠 Machine Learning Models

- **Main Model**: LSTM (Long Short-Term Memory)  
- **Forecasting**: Prophet, ARIMA  
- **Automation**: PyCaret  
- **Feature Selection**: Random Forest  
- **Validation**: Cross-validation for model selection.  

---

## ⚙️ Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jigardonga105/Financial_Portfolio_Optimization.git
cd your-repo-name
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`
```

### 3. Install Required Libraries

```bash
pip install tensorflow keras pandas numpy scikit-learn yfinance pycaret prophet matplotlib seaborn plotly
```

---

### 🛠️ Tools and Technologies

- **Programming Language**: Python  
- **Libraries**: TensorFlow, Keras, Pandas, NumPy, Scikit-learn, yfinance, PyCaret, Prophet, Matplotlib, Seaborn, Plotly  
- **Version Control**: Git, GitHub  

---

## 📊 Results

- **Metrics**: Accuracy, precision, recall, F1 score.  
- **Risk Management**: Effective strategies for different risk profiles.  
- **Return Optimization**: Improved return rates compared to static models.  

---

## 🚀 Future Work

- Additional asset classes like real estate and cryptocurrencies.  
- Development of a real-time portfolio management dashboard.  

---

## 🤝 Contribution

Contributions are welcome! Please fork this repository and create a pull request.
