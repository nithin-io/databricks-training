# 📅 Week-3 Day-2

# Databricks Session 2 - DataFrame Basic Operations using PySpark

## Objective

The objective of this assignment is to learn basic DataFrame operations using PySpark in Databricks.

---

## Technologies Used

- Databricks
- PySpark
- Python
- Unity Catalog Volume Storage

---

## Files Used

- `empData.csv`

---

## Steps Performed

### 1. Opened Existing Workspace Folder

Used folder:

`Databricks2027`

---

### 2. Created Notebook

Created a notebook named:

`Session-2`

Language used:

`Python`

---

### 3. Read Employee Data File

```python
df = spark.read.format("csv") \
.option("header",True) \
.option("inferSchema",True) \
.load("/Volumes/workspace/default/databricks2027/empData.csv")
```

---

### 4. Display Full Data

```python
display(df)
```

---

### 5. Display Schema

```python
df.printSchema()
```

---

### 6. Show First 5 Records

```python
df.show(5)
```

---

### 7. Count Total Records

```python
df.count()
```

---

### 8. Display Selected Columns

```python
df.select("EmpID","EmpName","Salary").show()
```

---

### 9. Describe Data

```python
df.describe().show()
```

---

## Output

Successfully performed basic DataFrame operations in Databricks notebook.

---

## Learning Outcome

By completing this assignment, I learned:

- How to read existing CSV files
- How to display DataFrame records
- How to print schema
- How to count records
- How to select required columns
- How to summarize DataFrame statistics

---

## Author

**Y Nithin**
