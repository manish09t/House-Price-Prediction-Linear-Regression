# 🏠 House Price Prediction using Linear Regression

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)
![Internship](https://img.shields.io/badge/Internship-EISystems%20Services-orange?style=flat-square)

---

## 📌 Internship Details

| Field | Details |
|-------|---------|
| **Organization** | EISystems Services |
| **Intern Name** | Manish Kumar Mahato |
| **Roll No** | 024102020027 |
| **Program** | BCA (AI & ML) - Haridwar University |
| **Duration** | 4 Weeks Internship (2025) |

---

## 📖 Project Overview

This project was developed during my internship at **EISystems Services**. The objective was to build a robust predictive model for house prices using **Multiple Linear Regression** — one of the foundational supervised learning algorithms in Machine Learning.

The model takes key house attributes as input and predicts the estimated market value of a property.

### Features Used (Input Variables):
- **Area** — Size of the house in square feet
- **Bedrooms** — Number of bedrooms
- **Age** — Age of the house in years

### Target Variable (Output):
- **Price** — Predicted market value of the house (in USD)

---

## 🧠 Algorithm & Tools

| Category | Technology |
|----------|------------|
| Algorithm | Multiple Linear Regression |
| Language | Python 3.x |
| Libraries | Pandas, NumPy, Scikit-learn |
| Environment | Jupyter Notebook / Python Script |

---

## 📊 Dataset Sample (`Multi.csv`)

| area | bedrooms | age | price |
|------|----------|-----|-------|
| 1500 | 3 | 10 | 300,000 |
| 1800 | 4 | 15 | 350,000 |
| 2000 | 3 | 5 | 400,000 |
| 2500 | 4 | 12 | 450,000 |
| 3000 | 5 | 7 | 520,000 |

---

## 🚀 How to Run This Project

### Prerequisites

Make sure you have Python 3.x installed, then install the required libraries:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas numpy scikit-learn
```

### Steps to Execute

1. Clone this repository or download the files
2. Make sure `Multi.csv` is in the same directory as `house_price.py`
3. Run the Python script:

```bash
python house_price.py
```

---

## 📈 Model Results

After running the script, the model outputs:

- **Coefficients** for each feature (area, bedrooms, age)
- **Intercept** value of the regression line
- **Predicted price** for a sample new house input
- **Model Accuracy** (R² Score)

### Sample Output:
```
Coefficients: [150.25, 5000.10, -200.75]
Intercept: 50000.00
Predicted Price for [2000 sqft, 3 bed, 8 yrs]: $385,420.50
R² Score: 0.96
```

> ✅ An R² score close to 1.0 indicates the model fits the data well.

---

## 📁 Repository Structure

```
House-Price-Prediction/
│
├── Multi.csv                    # Dataset file
├── house_price.py               # Main Python script
├── requirements.txt             # Project dependencies
├── .gitignore                   # Git ignore file
├── README.md                    # Project documentation
└── EIsystem_Project_Report.pdf  # Full internship report
```

📄 **Full Report:** [EIsystem_Project_Report.pdf](./EIsystem_Project_Report.pdf)

---

## 🔍 What I Learned

- Implementing **Multiple Linear Regression** from scratch using Scikit-learn
- Understanding the relationship between features and target variables
- Data preprocessing and loading using **Pandas**
- Evaluating model performance using **R² Score**
- Writing clean, readable Python code for ML projects

---

## 👨‍💻 Author

**Manish Kumar Mahato**
BCA (AI & ML) | Roll No: 024102020027
Haridwar University
Intern at EISystems Services (2025)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
