# Week 4 Sales Analytics Capstone

## Project Overview

This project focuses on analyzing sales data using Python, Pandas, data visualization, machine learning, and Power BI. The objective is to understand sales performance, identify trends, compare product and regional sales, and build a regression model to predict sales values.

## Objectives

- Clean and preprocess sales data.
- Perform Exploratory Data Analysis (EDA).
- Create visualizations to identify sales trends and patterns.
- Build a sales prediction regression model.
- Evaluate the model using MAE, RMSE, and R-squared.
- Create an interactive Power BI dashboard.
- Present findings and business recommendations.

## Dataset

The project uses `sales_data.csv`.

The dataset contains the following columns:

- `order_id`
- `customer_name`
- `order_date`
- `category`
- `sub_category`
- `product_name`
- `quantity`
- `unit_price`
- `total_price`
- `region`

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- OpenPyXL
- Microsoft Power BI

## Project Structure

```text
Week4_Sales_Capstone/
│
├── data/
│   └── sales_data.csv
│
├── notebooks/
│
├── outputs/
│   ├── dataset_summary.csv
│   ├── cleaned_sales_data.csv
│   ├── cleaned_sales_data.xlsx
│   ├── 01_sales_distribution.png
│   ├── 02_top_products.png
│   ├── 03_sales_by_region.png
│   ├── 04_monthly_sales_trend.png
│   ├── 05_sales_by_category.png
│   ├── 06_quantity_vs_sales.png
│   ├── 07_avg_unit_price.png
│   ├── sales_predictions.csv
│   ├── model_metrics.csv
│   └── sales_model.pkl
│
├── eda_analysis.py
├── visualize_sales.py
├── sales_prediction.py
├── prepare_dashboard.py
├── Week4_Sales_Dashboard.pbix
└── README.md
```

*Note: Some output files will be created only after the corresponding Python scripts run successfully.*

## Installation

Install the required Python libraries using:

```bash
python -m pip install pandas numpy matplotlib seaborn scikit-learn joblib openpyxl
```

## How to Run the Project

### 1. Exploratory Data Analysis

Run the following command:

```bash
python eda_analysis.py
```

This script displays the first rows, dataset dimensions, data types, missing values, duplicate records, and statistical summary.

Output: `outputs/dataset_summary.csv`

### 2. Data Visualization

Run:

```bash
python visualize_sales.py
```

This script creates graphs to analyze:

- Sales distribution
- Top products by sales
- Sales by region
- Monthly sales trends
- Sales share by category
- Quantity versus sales
- Average unit price by category

The graphs are saved in the `outputs/` folder.

### 3. Prepare Dashboard Data

Run:

```bash
python prepare_dashboard.py
```

This script prepares the cleaned sales dataset and exports CSV and Excel files for Power BI.

Output files:

- `outputs/cleaned_sales_data.csv`
- `outputs/cleaned_sales_data.xlsx`

### 4. Sales Prediction Model

Run:

```bash
python sales_prediction.py
```

This script trains a Random Forest regression model and evaluates its performance.

Output files:

- `outputs/sales_predictions.csv`
- `outputs/model_metrics.csv`
- `outputs/sales_model.pkl`

## Power BI Dashboard

The interactive Power BI dashboard includes:

- Total Sales KPI card
- Total Orders KPI card
- Sales by Region chart
- Top Products chart
- Monthly Sales Trend chart
- Region slicer
- Category slicer
- Order Date slicer

Import `outputs/cleaned_sales_data.csv` into Power BI Desktop, create the visuals, and save the report as `Week4_Sales_Dashboard.pbix`.

## Model Evaluation

The regression model uses the following evaluation metrics:

**MAE (Mean Absolute Error):** Measures the average absolute difference between actual and predicted sales.

**RMSE (Root Mean Squared Error):** Measures prediction error while penalizing larger errors more strongly.

**R-squared (R²):** Measures how well the model explains variation in the target values compared with a baseline.

The actual metric values should be recorded after running the model.

**Important limitation:** If `total_price` is directly calculated as `quantity × unit_price`, predicting it from these same variables may reproduce a known calculation rather than forecast future sales. Interpret the model results accordingly.

## Findings and Recommendations

After completing the analysis, use the actual results to answer these questions:

1. Which region has the highest total sales?
2. Which product generates the highest revenue?
3. Which category contributes the most to total sales?
4. What patterns appear in monthly sales?
5. Are there missing values or duplicate records?
6. How well does the regression model perform on the test dataset?
7. What actions could improve business performance?

Recommendations should be based on the findings from the actual dataset.

## Conclusion

This project demonstrates an end-to-end data analytics workflow, from data cleaning and exploratory analysis to visualization, regression modeling, and interactive dashboard development.

It provides practical experience with Python, data analysis, machine learning, and Power BI.

## Author

Name: SUdarshan Kumar jha
Project: Week 4 Sales Analytics Capstone  
Interests: Data Analytics and Artificial Intelligence/Machine Learning

## License

This project is intended for educational and portfolio purposes.
