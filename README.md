<div align="center">

# 📊 Superstore Sales Data Analysis

### End-to-End Data Analysis Project using Python, MySQL & Data Visualization

<img src="https://img.shields.io/badge/Python-3.12-blue?logo=python">
<img src="https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql">
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-green?logo=pandas">
<img src="https://img.shields.io/badge/Matplotlib-Visualization-red">
<img src="https://img.shields.io/badge/Status-Completed-brightgreen">

</div>

---

# 📖 Project Overview

This project demonstrates a complete **Business Data Analysis Workflow** using the Superstore Sales dataset.

Starting from raw CSV data, the project imports data into MySQL, performs SQL analysis, exploratory data analysis (EDA), business visualization, and finally generates an automated Word business report.

This project is designed as a portfolio project for **Data Analyst**, **Business Analyst**, and **Python Developer** positions.

![Monthly Sales Trend](image/monthly_sales.png)

---

# 🎯 Objectives

- Import raw CSV data into MySQL
- Perform SQL business analysis
- Conduct Exploratory Data Analysis (EDA)
- Build business-style visualizations
- Generate an automated Word report
- Demonstrate an end-to-end data analysis workflow

---

# 📂 Project Structure

```text
superstore-sales-analysis
│
├── data
│   ├── train.csv
│   └── clean_superstore.csv
│
├── image
│   ├── monthly_sales.png
│   ├── category_sales.png
│   ├── region_sales.png
│   ├── segment_sales.png
│   ├── top10_products.png
│   └── sales_distribution.png
│
├── python
│   ├── 01_import_mysql.py
│   ├── 02_eda_analysis.py
│   ├── 03_visualization.py
│   └── 04_export_report.py
│
├── sql
│   └── analysis.sql
│
├── report
│   └── Superstore_Report.docx
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🔄 Workflow

```text
CSV Dataset
      │
      ▼
Import into MySQL
      │
      ▼
SQL Analysis
      │
      ▼
Python EDA
      │
      ▼
Business Visualization
      │
      ▼
Word Report
```

---

# 📊 Dataset Information

| Item | Value |
|------|------|
| Dataset | Superstore Sales |
| Records | 9,800 |
| Columns | 18 |
| Missing Values | Postal Code (11) |
| Database | MySQL |

---

# 🛠 Tech Stack

| Technology | Description |
|------------|-------------|
| Python | Data Analysis |
| MySQL | Database |
| Pandas | Data Processing |
| SQLAlchemy | Database Connection |
| PyMySQL | MySQL Driver |
| Matplotlib | Data Visualization |
| python-docx | Word Report |
| OpenPyXL | Excel Processing |

---

# 📈 SQL Analysis

The SQL module includes:

- Total Sales
- Total Orders
- Average Sales
- Monthly Sales Trend
- Category Analysis
- Regional Analysis
- Top Products
- Top Customers

---

# 🔍 Exploratory Data Analysis (EDA)

EDA includes:

- Data Overview
- Data Types
- Missing Value Detection
- Duplicate Detection
- Descriptive Statistics
- Sales Analysis
- Category Analysis
- Region Analysis
- Customer Segment Analysis
- Top Products Analysis

---

# 📊 Data Visualization

The project automatically generates the following charts:

| Chart | Description |
|--------|-------------|
| 📈 Monthly Sales Trend | Monthly sales changes |
| 📊 Sales by Category | Category comparison |
| 🌍 Sales by Region | Regional comparison |
| 👥 Sales by Segment | Customer segment analysis |
| 🏆 Top 10 Products | Best-selling products |
| 📉 Sales Distribution | Sales distribution |

All charts are exported as high-resolution PNG images.

---

# 📄 Automated Business Report

The project automatically generates:

```
Superstore_Report.docx
```

The report contains:

- Executive Summary
- Business Overview
- Six Business Charts
- Key Findings
- Business Conclusion

---

# 📌 Key Findings

- Total Sales exceeded **$2.26 Million**
- Technology generated the highest revenue
- West region achieved the best performance
- Consumer customers contributed the largest sales
- Sales show a long-tail distribution
- High-value products significantly impact total revenue

---

# ▶️ How to Run

### Step 1: Install dependencies

Run these commands from the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Step 2: Configure MySQL

Create the `superstore_analysis` database, then copy the example configuration:

```powershell
Copy-Item .env.example .env
```

Open `.env` and replace `replace_with_your_password` with your local MySQL
password. The `.env` file is excluded from Git and must never be committed.

### Step 3: Import data into MySQL

```powershell
python python/01_import_mysql.py
```

### Step 4: Run SQL analysis

```sql
sql/analysis.sql
```

### Step 5: Perform EDA

```powershell
python python/02_eda_analysis.py
```

### Step 6: Generate visualizations

```powershell
python python/03_visualization.py
```

### Step 7: Generate the business report

```powershell
python python/04_export_report.py
```

All Python scripts use paths relative to the repository, so the project can be
cloned and run from any local directory.

---

# 📷 Project Output

After running all scripts, the project generates:

```
clean_superstore.csv
```

```
6 Business Charts
```

```
Superstore_Report.docx
```

---

# 🚀 Skills Demonstrated

✔ Python Programming

✔ SQL

✔ MySQL

✔ Data Cleaning

✔ Exploratory Data Analysis

✔ Business Visualization

✔ Report Automation

✔ Data Storytelling

---

# 📚 Future Improvements

- Dashboard using Power BI
- Interactive dashboard using Plotly
- Machine Learning Sales Forecasting
- Customer Segmentation
- Profit Analysis
- Time Series Forecasting

---

# 👨‍💻 Author

**Hongyang Song**

Data Analysis Portfolio

2026

---

<div align="center">

⭐ If you like this project, feel free to give it a Star!

</div>
