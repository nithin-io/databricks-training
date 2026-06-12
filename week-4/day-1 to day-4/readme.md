# 🛒 E-Commerce Orders Analysis Using PySpark

<div align="center">

# 🚀 PySpark Data Engineering Assignment

### E-Commerce Analytics using PySpark

### 📌 Assignment Overview

This project focuses on analyzing E-Commerce Orders data using PySpark. The assignment covers DataFrame transformations, aggregations, joins, window functions, advanced transformations, and real-world Data Engineering scenarios commonly used in Databricks and Spark environments.

**Total Questions Solved:** 75

</div>

---

# 📅 Day 1: Basic Transformations & Filtering

## 🎯 Objective

Learn and implement fundamental DataFrame transformations and filtering operations.

## 📚 Topics Covered

| Topic                  | Description                   |
| ---------------------- | ----------------------------- |
| DataFrame Operations   | Select, Rename, Drop          |
| Column Transformations | Create Derived Columns        |
| Conditional Logic      | when(), otherwise()           |
| Date Functions         | DateType Conversion           |
| Filtering              | Business Rule-Based Filtering |

## ✅ Assignment Questions Covered

### Basic Transformations (1–10)

* Display selected columns
* Rename columns
* Create total_amount
* Apply discounts
* Convert dates
* Filter city-wise orders
* Create uppercase category
* Remove unwanted columns

### Filter Transformations (11–15)

* High-value orders
* Date range filtering
* Customer age filtering
* Product pattern filtering
* Multi-city filtering

## 🛠️ Key Functions

```python
select()
withColumn()
withColumnRenamed()
filter()
when()
to_date()
upper()
drop()
isin()
startswith()
```

## 🎓 Learning Outcomes

✔ DataFrame Transformations

✔ Column Manipulations

✔ Conditional Logic

✔ Filtering Techniques

✔ Date Handling

---

# 📅 Day 2: Aggregations & GroupBy Analysis

## 🎯 Objective

Perform business KPI calculations and category-wise sales analysis.

## 📚 Topics Covered

| Topic              | Description             |
| ------------------ | ----------------------- |
| Aggregations       | Sum, Avg, Count         |
| Revenue Analysis   | Sales Calculations      |
| GroupBy Operations | Category-Level Analysis |
| Customer Analytics | Revenue Reports         |

## ✅ Assignment Questions Covered

### Aggregations (16–22)

* Total Sales Amount
* Quantity Sold by Category
* Average Product Price
* Maximum Priced Product
* Minimum Priced Product
* Orders by City
* Highest Revenue Category

### GroupBy Transformations (23–28)

* Product Count by Category
* Average Quantity per City
* Revenue per City
* Revenue per Customer
* Top Customers
* Highest Sales City

## 🛠️ Key Functions

```python
groupBy()
sum()
avg()
count()
max()
min()
agg()
orderBy()
desc()
```

## 📊 Business Insights Generated

* Revenue by Category
* Revenue by City
* Customer Spending Reports
* Sales Performance Analysis

## 🎓 Learning Outcomes

✔ Business KPI Calculations

✔ Revenue Analytics

✔ Customer Revenue Analysis

✔ Category-Wise Reporting

---

# 📅 Day 3: Joins, Sorting & Window Functions

## 🎯 Objective

Perform advanced analytics using joins and window functions.

## 📚 Topics Covered

| Topic            | Description                  |
| ---------------- | ---------------------------- |
| Joins            | Combining Orders & Customers |
| Sorting          | Top-N Analysis               |
| Distinct         | Unique Value Extraction      |
| Window Functions | Ranking & Running Totals     |

## ✅ Assignment Questions Covered

### Join Transformations (29–34)

* Orders & Customers Join
* Customer Purchases
* Customer Spending Analysis
* Highest Spending Customer
* City-wise Spending
* Electronics Buyers

### Sorting & Distinct (35–38)

* Sort Products
* Distinct Categories
* Distinct Cities
* Top Expensive Orders

### Window Functions (39–45)

* Row Number
* Rank
* Dense Rank
* Highest Priced Product
* Second Highest Product
* Running Revenue
* Cumulative Quantity

## 🛠️ Key Functions

```python
join()
distinct()
orderBy()
Window()
partitionBy()
row_number()
rank()
dense_rank()
sum().over()
```

## 📊 Business Insights Generated

* Customer Spending Patterns
* Top Revenue Customers
* Product Ranking Reports
* Running Sales Metrics

## 🎓 Learning Outcomes

✔ DataFrame Joins

✔ Ranking Techniques

✔ Window Analytics

✔ Running Aggregations

---

# 📅 Day 4: Advanced Transformations & Real-Time Scenarios

## 🎯 Objective

Solve real-world Data Engineering use cases using advanced PySpark features.

## 📚 Topics Covered

| Topic                    | Description                 |
| ------------------------ | --------------------------- |
| Advanced Transformations | Classification & Duplicates |
| Pivot & Unpivot          | Reporting                   |
| Arrays & Maps            | Complex Data Types          |
| Explode                  | Flatten Nested Data         |
| RDD Conversions          | DataFrame ↔ RDD             |
| Business Scenarios       | Customer Analytics          |

## ✅ Assignment Questions Covered

### Advanced Transformations (46–55)

* Customer Value Classification
* Duplicate Detection
* Remove Duplicates
* Pivot Reports
* Unpivot Reports
* Arrays
* Explode
* Maps
* RDD Conversions

### Real-Time Data Engineering Scenarios (56–65)

* Multi-category Customers
* Mobile & Laptop Buyers
* Repeat Customers
* Revenue Contribution %
* Monthly Sales Trends
* Top-Selling Products
* Bottom-Selling Products
* Customer Retention
* City Revenue Contribution
* Customer Segmentation

### Interview Questions (66–75)

* select() vs withColumn()
* distinct() vs dropDuplicates()
* groupBy() vs Window Functions
* Broadcast Join
* repartition() vs coalesce()
* Data Skew
* Join Optimization
* Small Files Problem
* Narrow vs Wide Transformations
* Catalyst Optimizer

## 🛠️ Key Functions

```python
pivot()
stack()
array()
explode()
create_map()
countDistinct()
rdd
toDF()
collect()
```

## 📊 Business Insights Generated

* Customer Segmentation
* Retention Analysis
* Revenue Contribution Reports
* Product Performance Analysis

## 🎓 Learning Outcomes

✔ Real-Time Data Engineering Scenarios

✔ Advanced Transformations

✔ Customer Segmentation

✔ Data Modeling Concepts

✔ Interview Preparation

---

# 📂 Dataset Information

## Orders Dataset

| Column Name |
| ----------- |
| order_id    |
| customer_id |
| product     |
| category    |
| price       |
| quantity    |
| order_date  |
| city        |

## Customers Dataset

| Column Name   |
| ------------- |
| customer_id   |
| customer_name |
| age           |
| city          |

---

# 🛠️ Technologies Used

* Python
* PySpark
* Apache Spark
* Databricks
* Spark SQL

---

# 🚀 Skills Practiced

### PySpark Core

* DataFrames
* Transformations
* Actions
* Filtering
* Aggregations

### Analytics

* Revenue Analysis
* Customer Analysis
* Sales Reporting

### Advanced Spark

* Joins
* Window Functions
* Pivot/Unpivot
* Arrays & Maps
* RDD Conversions

### Data Engineering

* Customer Segmentation
* Retention Analytics
* Revenue Contribution Analysis
* Real-Time Business Scenarios

---

# 📁 Repository Structure

```text
E-Commerce-PySpark-Assignment/
│
├── Day-1/
│   ├── Questions_1_to_15
│   └── README.md
│
├── Day-2/
│   ├── Questions_16_to_28
│   └── README.md
│
├── Day-3/
│   ├── Questions_29_to_45
│   └── README.md
│
├── Day-4/
│   ├── Questions_46_to_75
│   └── README.md
│
└── Main_README.md
```

---

# 🏆 Final Outcome

Successfully completed **75 PySpark Interview-Oriented Questions** covering:

✅ DataFrame Transformations

✅ Filtering Operations

✅ Aggregations & GroupBy

✅ Joins

✅ Window Functions

✅ Advanced Transformations

✅ Real-Time Data Engineering Scenarios

✅ Spark Interview Concepts

This project demonstrates practical PySpark skills commonly required for Data Engineer roles working with Apache Spark, Databricks, and large-scale data processing systems.

