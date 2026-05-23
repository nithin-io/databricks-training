# 📘 Week-2 : SQL Functions & Data Manipulation
## 🚀 Databricks Assignment Repository 

---

# 🌟 Overview

This repository contains all assignments completed during **Week-2** in Databricks.

The assignments focus on practicing SQL queries, data manipulation techniques, joins, date functions, string functions, regex operations, numeric functions, null handling, and timestamp functions using Databricks SQL.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Databricks | Cloud-based notebook platform |
| SQL | Query Language |
| Python | Notebook Support |
| Apache Spark SQL | Query Processing Engine |

---

# 📂 Topics Covered (7 Days)

| Day | Topic |
|---|---|
| Day-1 | Data Manipulation |
| Day-2 | String Functions |
| Day-3 | Numeric Functions |
| Day-4 | Date Functions |
| Day-5 | Timestamp Functions |
| Day-6 | Null Functions |
| Day-7 | Joins & Regex Functions |

---

# 📅 Day-Wise Assignment Details

---

# 🔹 Day-1 : Data Manipulation

## 📘 Topics Practiced

- SELECT
- WHERE
- ORDER BY
- LIMIT
- DISTINCT
- ALIAS
- GROUP BY
- HAVING

## ✅ Example

```sql
SELECT emp_name, salary
FROM employee;
```

---

# 🔹 Day-2 : String Functions

## 📘 Topics Practiced

- UPPER()
- LOWER()
- INITCAP()
- CONCAT()
- SUBSTRING()
- LENGTH()
- TRIM()
- REPLACE()

## ✅ Example

```sql
SELECT UPPER(emp_name)
FROM employee;
```

---

# 🔹 Day-3 : Numeric Functions

## 📘 Topics Practiced

- ROUND()
- CEIL()
- FLOOR()
- ABS()
- POWER()
- SQRT()
- MOD()

## ✅ Example

```sql
SELECT ROUND(salary,2)
FROM employee;
```

---

# 🔹 Day-4 : Date Functions

## 📘 Topics Practiced

- CURRENT_DATE()
- DATE_ADD()
- DATE_SUB()
- DATEDIFF()
- ADD_MONTHS()
- LAST_DAY()

## ✅ Example

```sql
SELECT CURRENT_DATE();
```

---

# 🔹 Day-5 : Timestamp Functions

## 📘 Topics Practiced

- CURRENT_TIMESTAMP()
- HOUR()
- MINUTE()
- SECOND()
- UNIX_TIMESTAMP()

## ✅ Example

```sql
SELECT CURRENT_TIMESTAMP();
```

---

# 🔹 Day-6 : Null Functions

## 📘 Topics Practiced

- IS NULL
- IS NOT NULL
- COALESCE()
- NVL()
- IFNULL()

## ✅ Example

```sql
SELECT *
FROM employee
WHERE salary IS NULL;
```

---

# 🔹 Day-7 : Joins & Regex Functions

## 📘 Joins Practiced

- INNER JOIN
- LEFT JOIN
- RIGHT JOIN
- FULL JOIN
- CROSS JOIN

## 📘 Regex Functions Practiced

- REGEXP_REPLACE()
- REGEXP_EXTRACT()
- RLIKE

## ✅ Join Example

```sql
SELECT e.emp_name, d.department_name
FROM employee e
INNER JOIN department d
ON e.dept_id = d.dept_id;
```

## ✅ Regex Example

```sql
SELECT REGEXP_REPLACE(emp_name,'a','@')
FROM employee;
```

---

# 📊 Dataset Used

## Employee Table Columns

| Column Name | Description |
|---|---|
| emp_id | Employee ID |
| emp_name | Employee Name |
| age | Employee Age |
| city | Employee City |
| designation | Job Role |
| salary | Salary |
| joining_date | Joining Date |
| department | Department |

---

# ⚙️ Workflow Followed

## ✅ Step-1

Created workspace folder in Databricks.

---

## ✅ Step-2

Created notebooks for daily assignments.

Example:

```python
Week2-Day1
Week2-Day2
Week2-Day3
```

---

## ✅ Step-3

Created tables and inserted employee data.

---

## ✅ Step-4

Executed SQL queries for each topic.

---

## ✅ Step-5

Verified outputs in Databricks notebook.

---

# 📈 Learning Outcomes

By completing Week-2 assignments, I learned:

✅ SQL query writing  
✅ Data manipulation operations  
✅ String processing functions  
✅ Numeric calculations  
✅ Date & timestamp handling  
✅ Null value handling  
✅ SQL joins  
✅ Regex operations in SQL  
✅ Query optimization basics  

---

# 🎯 Skills Gained

| Skill | Level |
|---|---|
| SQL Queries | Intermediate |
| Data Manipulation | Intermediate |
| String Functions | Intermediate |
| Joins Handling | Intermediate |
| Regex Functions | Intermediate |
| Date & Timestamp Functions | Intermediate |

---

# 📌 Assignment Summary

| Total Days Completed | 7 |
|---|---|
| Total Topics Covered | 7 |
| Platform Used | Databricks |
| Language Used | SQL |
| Query Engine | Spark SQL |

---

# 🏆 Final Outcome

Successfully completed all Week-2 SQL practice assignments in Databricks and gained hands-on experience in SQL query writing and data manipulation.

