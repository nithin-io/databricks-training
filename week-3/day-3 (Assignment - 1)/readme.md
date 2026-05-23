# 📘 Week-3 Day-3
## 🚀 Databricks PySpark DataFrame Assignment  

---

## 🎯 Objective

The objective of this assignment is to practice various PySpark DataFrame operations in Databricks, including:

- SELECT
- ALIAS
- FILTER / WHERE
- WITHCOLUMNRENAMED
- WITHCOLUMN
- TYPECASTING
- SORT / ORDERBY
- LIMIT

This assignment helps in understanding real-time DataFrame transformations using PySpark.

---

# 🛠️ Technologies Used

| Technology | Description |
|---|---|
| Databricks | Cloud-based big data platform |
| PySpark | Spark Python API |
| Python | Programming Language |
| Apache Spark | Distributed processing engine |

---

# 📂 Dataset Used

### Employee DataFrame Columns

| Column Name | Description |
|---|---|
| emp_id | Employee ID |
| emp_name | Employee Name |
| age | Employee Age |
| city | Employee City |
| designation | Job Role |
| salary | Employee Salary |
| joining_date | Date of Joining |
| department | Department Name |

---

# ⚙️ Steps Performed

## 📁 1. Created Workspace Folder

Created a workspace folder named:

```python
Databricks2027
```

---

## 📓 2. Created Notebook

Created notebook:

```python
PySpark-Assignment
```

Language Used:

```python
Python
```

---

## 🧾 3. Created Employee DataFrame

Created DataFrame using employee records and schema columns.

```python
df = spark.createDataFrame(data, columns)
```

---

## 👀 4. Displayed DataFrame

```python
df.show()
```

---

# 🔹 5. SELECT Operations

Performed:

✅ Selecting single columns  
✅ Selecting multiple columns  
✅ Selecting first 5 columns  
✅ Dropping columns  
✅ Department-based selection  

### Example

```python
df.select("emp_name","salary").show()
```

---

# 🔹 6. ALIAS Operations

Performed aliasing for better readability.

### Example

```python
df.select(df.emp_name.alias("employee_name")).show()
```

---

# 🔹 7. FILTER / WHERE Operations

Applied filtering using:

- Greater Than
- Less Than
- Between
- AND / OR Conditions
- startswith()
- endswith()
- contains()

### Example

```python
df.filter(df.salary > 70000).show()
```

---

# 🔹 8. withColumnRenamed Operations

Renamed DataFrame columns.

### Example

```python
df.withColumnRenamed("salary","monthly_salary").show()
```

---

# 🔹 9. withColumn Operations

Created new derived columns:

| New Column | Purpose |
|---|---|
| bonus | 10% bonus |
| annual_salary | Yearly salary |
| tax | Tax calculation |
| updated_salary | Salary increment |
| salary_category | High/Medium/Low |
| age_group | Young/Adult |
| joining_year | Extracted joining year |
| double_salary | Double salary |

### Example

```python
df.withColumn("bonus",df.salary*0.10).show()
```

---

# 🔹 10. TYPECASTING Operations

Converted datatypes using cast().

### Example

```python
df.withColumn("salary",df.salary.cast("float")).show()
```

---

# 🔹 11. SORT / ORDERBY Operations

Performed sorting:

✅ Ascending  
✅ Descending  
✅ Multiple column sorting  
✅ Top salary records  

### Example

```python
df.orderBy(df.salary.desc()).show()
```

---

# 🔹 12. LIMIT Operations

Displayed limited records from DataFrame.

### Example

```python
df.limit(5).show()
```

---

# ✅ Output

Successfully executed all PySpark DataFrame operations in Databricks notebook and verified outputs.

---

# 📚 Learning Outcome

Through this assignment, I learned:

- Creating DataFrames in PySpark
- Selecting and filtering records
- Renaming columns
- Creating derived columns
- Applying conditional transformations
- Typecasting columns
- Sorting records
- Limiting DataFrame rows
- Practical implementation of PySpark DataFrame APIs

---

# 📌 Assignment Sections Completed

| Completed Topics |
|---|
| ✅ SELECT |
| ✅ ALIAS |
| ✅ FILTER / WHERE |
| ✅ WITHCOLUMNRENAMED |
| ✅ WITHCOLUMN |
| ✅ TYPECASTING |
| ✅ SORT / ORDERBY |
| ✅ LIMIT |

