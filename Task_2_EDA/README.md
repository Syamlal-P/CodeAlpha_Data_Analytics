📊 Task 2: Exploratory Data Analysis (EDA)

CodeAlpha Data Analytics Internship – January 2026

📌 Objective

The objective of Task 2 is to perform Exploratory Data Analysis (EDA) on the dataset collected in Task 1 (Data Collection & Web Scraping).
This task focuses on understanding the dataset, identifying patterns and trends, detecting anomalies, validating assumptions, and uncovering meaningful insights using statistical analysis and visualizations.

EDA serves as a critical foundation for any data-driven system, especially for applications like fashion and outfit recommendation systems.

📂 Dataset Description

Source: Public fashion-related web pages (scraped in Task 1)

Domain: Fashion & Apparel

Format: CSV

Nature: Structured dataset created specifically for analytics purposes

Typical Attributes Include:

Product / Item Name

Category (Shirt, Pant, Dress, etc.)

Brand

Price

Additional attributes depending on source availability

📌 The dataset is custom-built to support analytics and recommendation-based use cases.

🧠 Key Questions Explored

Before starting the analysis, the following business and analytical questions were framed:

Which fashion category appears most frequently?

What is the overall price distribution of fashion items?

Do certain brands consistently have higher prices?

Are there missing, duplicate, or inconsistent values?

Are there any extreme price outliers?

How does price vary across different categories?

These questions guided the entire EDA process.

🛠️ Tools & Technologies Used

Python

Pandas – data manipulation and analysis

NumPy – numerical operations

Matplotlib – data visualization

Seaborn – statistical visualizations

Jupyter Notebook – interactive analysis environment

📁 Folder Structure
Task_2_EDA/
│
├── data/
│   ├── raw/
│   │   └── fashion_dataset.csv
│   └── processed/
│       └── cleaned_fashion_data.csv
│
├── notebooks/
│   └── eda_fashion.ipynb
│
├── visuals/
│   ├── category_distribution.png
│   ├── price_analysis.png
│   ├── brand_trends.png
│   └── missing_values.png
│
├── reports/
│   └── EDA_Report.md
│
├── requirements.txt
│
└── README.md

📊 Analysis Performed

The following steps were carried out during EDA:

1️⃣ Data Understanding

Dataset shape and structure

Column names and data types

Summary statistics

2️⃣ Data Quality Checks

Missing value detection

Duplicate record identification

Inconsistent category/brand names

3️⃣ Trend & Pattern Analysis

Category-wise frequency analysis

Price distribution analysis

Brand-level price comparisons

4️⃣ Anomaly Detection

Identification of extreme price values

Detection of abnormal records

5️⃣ Data Visualization

Bar charts for category distribution

Histograms and box plots for price analysis

Visual representation of missing values

All visual outputs are saved inside the visuals/ directory.

📈 Key Insights (Summary)

Certain fashion categories dominate the dataset, indicating higher availability or demand.

Price distribution shows both affordable and premium segments.

Some brands consistently fall into higher price ranges.

A small number of missing and inconsistent values were identified and addressed.

Outliers were detected, emphasizing the importance of data cleaning before modeling.

(Detailed insights are documented in reports/EDA_Report.md)

⚠️ Data Issues Identified

Missing values in selected attributes

Price outliers

Minor inconsistencies in category naming

These issues were documented and addressed to prepare the dataset for further analysis or modeling tasks.

🔮 Relevance to Future Tasks

The insights from this EDA:

Help refine feature selection

Support recommendation logic

Improve data-driven decision-making

Prepare the dataset for advanced analytics or machine learning

This task acts as a bridge between raw data collection and intelligent system development.