# 📊 Task 2: Exploratory Data Analysis (EDA)

This task is part of the **CodeAlpha Data Analytics Internship (January 2026)**.
The objective of Task-2 is to perform **Exploratory Data Analysis (EDA)** on a
real-world dataset collected during **Task-1 (Web Scraping)**.

The analysis focuses on understanding the structure, quality, and patterns
within a **fashion product dataset**, which serves as the data foundation for
an outfit recommendation system.

---

## 🎯 Objectives of This Task

- Understand the structure and contents of the dataset
- Identify data types and missing values
- Perform basic data cleaning and preprocessing
- Analyze price distribution and product characteristics
- Visualize trends and patterns using charts and plots
- Generate insights to support future analytics and recommendation logic

---

## 📁 Dataset Description

The dataset was obtained via **web scraping** in Task-1 and contains
information about fashion products.

### Columns Included:
- `product_name` – Name of the clothing item
- `category` – Product category (Fashion)
- `price` – Product price (string with currency symbol)
- `price_numeric` – Cleaned numeric price for analysis
- `product_url` – Link to the product page
- `image_url` – Product image URL

Total records: **16 fashion products**

---

## 🛠️ Tools & Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 📊 Analysis Performed

### 1. Data Overview
- Dataset shape and structure inspection
- Data types and non-null value checks
- Duplicate and missing value analysis

### 2. Data Cleaning
- Converted price values from string to numeric format
- Verified data consistency across columns

### 3. Exploratory Analysis
- Category distribution analysis
- Price distribution analysis
- Boxplot to detect price spread and outliers
- Text-based feature exploration (product name length)

---

## 📈 Visualizations Generated

The following visualizations were created and saved for reference:

- **Price Distribution Bar Chart**
- **Category Distribution Bar Chart**
- **Price Boxplot**
- *(Optional)* Product Name Length Distribution
- *(Optional)* Missing Values Visualization

All visual outputs are available in the `visuals/` directory.

---

## 📌 Key Insights

- All products belong to a single category (Fashion), ensuring dataset consistency
- Prices show variation across products, indicating scope for budget-based filtering
- No missing values detected in critical columns
- Clean numeric pricing enables further statistical analysis and visualization

---

## 🚀 Relevance to Outfit Recommendation System

This EDA helps establish a strong analytical foundation for:
- Price-based outfit recommendations
- Category-level filtering
- Integration with visualization dashboards (Task-3)
- Sentiment and text analysis (Task-4)

---

## 📂 Folder Structure
Task_2_EDA/
├── data/
│ └── fashion_products.csv
├── notebooks/
│ └── fashion_eda.ipynb
├── visuals/
│ ├── price_distribution.png
│ ├── category_distribution.png
│ └── price_boxplot.png
├── reports/
│ └── eda_summary.md
├── README.md
├── requirements.txt

---

## ✅ Task Status

✔ Task-2 completed successfully  
✔ Meets all CodeAlpha EDA criteria  
✔ Ready for submission and further tasks
