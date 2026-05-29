# Databricks notebook source
# MAGIC %md
# MAGIC # **PySpark DataFrame Practice Dataset and Transformation Questions**

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark = SparkSession.builder.appName("PySparkPractice").getOrCreate()

# Employee Dataset
employee_data = [
(101, "Sravan", "Data Engineer", "IT", 75000, "Hyderabad", 28,
"2021-05-10", "Male"),
(102, "Ravi", "Software Engineer", "IT", 68000, "Bangalore", 30,
"2020-03-15", "Male"),
(103, "Priya", "Data Analyst", "Analytics", 62000, "Chennai", 26,
"2022-01-12", "Female"),
(104, "Kiran", "Manager", "HR", 90000, "Mumbai", 35, "2018-07-19",
"Male"),
(105, "Anjali", "HR Executive", "HR", 45000, "Pune", 24, "2023-02-20",
"Female"),
(106, "Vikram", "Data Scientist", "Analytics", 98000, "Delhi", 32,
"2019-11-25", "Male"),
(107, "Sneha", "Developer", "IT", 71000, "Hyderabad", 27, "2021-08-17",
"Female"),
(108, "Rahul", "Tester", "QA", 55000, "Chennai", 29, "2020-06-10",
"Male"),
(109, "Meena", "QA Lead", "QA", 83000, "Bangalore", 33, "2017-09-14",
"Female"),
(110, "Arjun", "Support Engineer", "Support", 50000, "Pune", 31,
"2022-04-11", "Male")
]
columns = ["emp_id", "name", "designation", "department", "salary", "city",
"age", "joining_date", "gender"]
emp_df = spark.createDataFrame(employee_data, columns)
emp_df.show()


# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Select() Transformation Questions

# COMMAND ----------

# 1. Select only employee name and salary columns
emp_df.select("name", "salary").show()

# 2. Select emp_id, department and city columns
emp_df.select("emp_id", "department", "city").show()

# 3. Select only name and age columns
emp_df.select("name", "age").show()

# 4. Select designation and salary columns
emp_df.select("designation", "salary").show()

# 5. Select emp_id, name and joining_date columns
emp_df.select("emp_id", "name", "joining_date").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. filter() / where() Transformation Questions
# MAGIC

# COMMAND ----------

# 1. Find employees whose salary is greater than 70000
emp_df.filter(col("salary") > 70000).show()

# 2. Find employees working in IT department
emp_df.filter(col("department") == "IT").show()

# 3. Find employees whose age is less than 30
emp_df.filter(col("age") < 30).show()

# 4. Find female employees
emp_df.filter(col("gender") == "Female").show()

# 5. Find employees from Hyderabad city
emp_df.filter(col("city") == "Hyderabad").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. withColumn() Transformation Questions
# MAGIC

# COMMAND ----------

# 1. Add a new column bonus with 10% of salary
emp_df.withColumn("bonus", col("salary") * 0.10).show()

# 2. Add a new column tax with 5% of salary
emp_df.withColumn("tax", col("salary") * 0.05).show()

# 3. Add salary increment of 5000
emp_df.withColumn("salary_increment", col("salary") + 5000).show()

# 4. Create age_group column
emp_df.withColumn("age_group", when(col("age") < 30, "Young").otherwise("Senior")).show()

# 5. Create yearly salary column
emp_df.withColumn("yearly_salary", col("salary") * 12).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. withColumnRenamed() Questions
# MAGIC

# COMMAND ----------

# 1. Rename emp_id to employee_id
emp_df.withColumnRenamed("emp_id", "employee_id").show()

# 2. Rename designation to role
emp_df.withColumnRenamed("designation", "role").show()

# 3. Rename salary to monthly_salary
emp_df.withColumnRenamed("salary", "monthly_salary").show()

# 4. Rename city to work_location
emp_df.withColumnRenamed("city", "work_location").show()

# 5. Rename joining_date to doj
emp_df.withColumnRenamed("joining_date", "doj").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. drop() Transformation Questions
# MAGIC

# COMMAND ----------

# 1. Drop age column
emp_df.drop("age").show()

# 2. Drop gender column
emp_df.drop("gender").show()

# 3. Drop joining_date column
emp_df.drop("joining_date").show()

# 4. Drop city and age columns
emp_df.drop("city", "age").show()

# 5. Drop designation column
emp_df.drop("designation").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. distinct() Questions
# MAGIC

# COMMAND ----------

# 1. Find distinct departments
emp_df.select("department").distinct().show()

# 2. Find distinct cities
emp_df.select("city").distinct().show()

# 3. Find distinct designations
emp_df.select("designation").distinct().show()

# 4. Find distinct genders
emp_df.select("gender").distinct().show()

# 5. Find unique department and city combinations
emp_df.select("department", "city").distinct().show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 7. dropDuplicates() Questions
# MAGIC

# COMMAND ----------

# 1. Remove duplicate rows based on emp_id
emp_df.dropDuplicates(["emp_id"]).show()

# 2. Remove duplicates based on department
emp_df.dropDuplicates(["department"]).show()

# 3. Remove duplicates based on city
emp_df.dropDuplicates(["city"]).show()

# 4. Remove duplicates based on department and city
emp_df.dropDuplicates(["department", "city"]).show()

# 5. Remove duplicate employees based on name
emp_df.dropDuplicates(["name"]).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 8. sort() / orderBy() Questions
# MAGIC

# COMMAND ----------

# 1. Sort employees by salary ascending
emp_df.orderBy("salary").show()

# 2. Sort employees by age descending
emp_df.orderBy(col("age").desc()).show()

# 3. Sort employees by department and salary
emp_df.orderBy("department", "salary").show()

# 4. Sort employees by city
emp_df.orderBy("city").show()

# 5. Sort employees by joining_date descending
emp_df.orderBy(col("joining_date").desc()).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 9. groupBy() Questions
# MAGIC

# COMMAND ----------

# 1. Find average salary by department
emp_df.groupBy("department").avg("salary").show()

# 2. Find maximum salary in each department
emp_df.groupBy("department").max("salary").show()

# 3. Find minimum age in each department
emp_df.groupBy("department").min("age").show()

# 4. Count employees in each city
emp_df.groupBy("city").count().show()

# 5. Find total salary by gender
emp_df.groupBy("gender").sum("salary").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 10. agg() Questions
# MAGIC

# COMMAND ----------

# 1. Find total salary of all employees
emp_df.agg(sum("salary")).show()

# 2. Find average employee age
emp_df.agg(avg("age")).show()

# 3. Find max and min salary together
emp_df.agg(max("salary").alias("max_salary"), min("salary").alias("min_salary")).show()

# 4. Find count of employees
emp_df.agg(count("*").alias("employee_count")).show()

# 5. Find average salary and average age department-wise
emp_df.groupBy("department").agg(avg("salary").alias("avg_salary"), avg("age").alias("avg_age")).show()

# COMMAND ----------

# MAGIC %md
# MAGIC # Department Dataset
# MAGIC

# COMMAND ----------

department_data = [
("IT", "John"),
("HR", "Smith"),
("QA", "David"),
("Analytics", "Kevin"),
("Support", "Robert")
]
dept_columns = ["department", "manager"]
dept_df = spark.createDataFrame(department_data, dept_columns)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 11. join() Questions
# MAGIC

# COMMAND ----------

# 1. Perform inner join between emp_df and dept_df
emp_df.join(dept_df, "department", "inner").show()

# 2. Perform left join
emp_df.join(dept_df, "department", "left").show()

# 3. Perform right join
emp_df.join(dept_df, "department", "right").show()

# 4. Perform full outer join
emp_df.join(dept_df, "department", "outer").show()

# 5. Find employees along with manager names
emp_df.join(dept_df, "department", "inner").select("emp_id", "name", "department", "manager").show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Additonal Dataset

# COMMAND ----------

new_emp_data = [
(111, "Teja", "Developer", "IT", 72000, "Hyderabad", 26, "2023-01-10",
"Male"),
(112, "Divya", "Analyst", "Analytics", 65000, "Bangalore", 25,
"2022-11-05", "Female")
]
new_emp_df = spark.createDataFrame(new_emp_data, columns)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 12. Union() Questions
# MAGIC

# COMMAND ----------

# 1. Union emp_df with new_emp_df
emp_union_df = emp_df.union(new_emp_df)
emp_union_df.show()

# 2. Count total rows after union
emp_df.union(new_emp_df).count()

# 3. Remove duplicates after union
emp_df.union(new_emp_df).distinct().show()

# 4. Find all IT employees after union
emp_df.union(new_emp_df).filter(col("department") == "IT").show()

# 5. Sort unioned dataframe by salary
emp_df.union(new_emp_df).orderBy("salary").show()

# COMMAND ----------

# ================================
# PySpark Complete Setup Code
# ================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# Create Spark Session
spark = SparkSession.builder \
    .appName("PySparkPractice") \
    .getOrCreate()

# ================================
# Employee Data
# ================================

emp_data = [
    (101, "Arun", "IT", 75000, 28, "Male", "Chennai", "2022-01-10", "Software Engineer"),
    (102, "Priya", "HR", 65000, 30, "Female", "Hyderabad", "2021-03-15", "HR Manager"),
    (103, "Rahul", "IT", 82000, 27, "Male", "Bangalore", "2020-07-20", "Data Engineer"),
    (104, "Sneha", "Finance", 72000, 29, "Female", "Pune", "2019-11-05", "Financial Analyst"),
    (105, "Kiran", "QA", 58000, 26, "Male", "Chennai", "2023-02-18", "QA Engineer"),
    (106, "Meena", "IT", 91000, 32, "Female", "Hyderabad", "2018-06-25", "Senior Developer"),
    (107, "Vijay", "Support", 45000, 24, "Male", "Bangalore", "2022-08-12", "Support Engineer"),
    (108, "Anjali", "Analytics", 88000, 31, "Female", "Pune", "2020-04-01", "Data Analyst")
]

emp_columns = [
    "emp_id",
    "name",
    "department",
    "salary",
    "age",
    "gender",
    "city",
    "joining_date",
    "designation"
]

emp_df = spark.createDataFrame(emp_data, emp_columns)

# ================================
# Department Data
# ================================

dept_data = [
    ("IT", "Ramesh"),
    ("HR", "Suresh"),
    ("Finance", "Mahesh"),
    ("QA", "Ganesh"),
    ("Support", "Lokesh"),
    ("Analytics", "Rajesh")
]

dept_columns = ["department", "manager"]

dept_df = spark.createDataFrame(dept_data, dept_columns)

# ================================
# New Employee Data
# ================================

new_emp_data = [
    (109, "Deepak", "IT", 76000, 29, "Male", "Chennai", "2021-09-10", "Developer"),
    (110, "Pooja", "HR", 62000, 27, "Female", "Mumbai", "2022-05-14", "HR Executive")
]

new_emp_df = spark.createDataFrame(new_emp_data, emp_columns)

# ================================
# Skills Data
# ================================

skills_data = [
    (101, ["Python", "Spark", "SQL"]),
    (102, ["Excel", "Communication"]),
    (103, ["Python", "AWS", "Spark"]),
    (104, ["Finance", "Excel"]),
    (105, ["Testing", "Selenium"]),
    (106, ["Python", "Scala", "Spark"]),
    (107, ["Linux", "Networking"]),
    (108, ["SQL", "PowerBI", "Python"])
]

skills_columns = ["emp_id", "skills"]

skills_df = spark.createDataFrame(skills_data, skills_columns)

# ================================
# Shuffled DataFrame
# ================================

shuffled_df = emp_df.select(
    "name",
    "emp_id",
    "department",
    "salary",
    "age",
    "gender",
    "city",
    "joining_date",
    "designation"
)

# ================================
# Extra Column DataFrame
# ================================

extra_col_df = emp_df.withColumn(
    "bonus",
    col("salary") * 0.10
)

# ================================
# Display Data
# ================================

print("Employee Data")
emp_df.show()

print("Department Data")
dept_df.show()

print("Skills Data")
skills_df.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 13. unionByName() Questions
# MAGIC

# COMMAND ----------

# 1. Show first 3 records
emp_df.limit(3).show()

# 2. Show first 5 employees
emp_df.limit(5).show()

# 3. Get top 2 highest salary employees
emp_df.orderBy(col("salary").desc()).limit(2).show()

# 4. Get first 4 IT employees
emp_df.filter(col("department") == "IT").limit(4).show()

# 5. Show first employee record
emp_df.limit(1).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 15. sample() Questions
# MAGIC

# COMMAND ----------

# 1. Take 50% sample of data
emp_df.sample(False, 0.5).show()

# 2. Take 30% sample with seed
emp_df.sample(False, 0.3, seed=10).show()

# 3. Take sample from IT employees
emp_df.filter(col("department") == "IT").sample(False, 0.5).show()

# 4. Compare full data vs sampled data
print("Full Count:", emp_df.count())
print("Sample Count:", emp_df.sample(False, 0.5).count())

# 5. Take random sample of 5 rows
emp_df.sample(False, 0.8).limit(5).show()

# COMMAND ----------

# MAGIC %md
# MAGIC # Skill Dataset

# COMMAND ----------

skills_data = [
(101, ["Python", "Spark", "Azure"]),
(102, ["Java", "SQL"]),
(103, ["Power BI", "SQL"])
]
skills_columns = ["emp_id", "skills"]
skills_df = spark.createDataFrame(skills_data, skills_columns)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 16. explode() Questions
# MAGIC

# COMMAND ----------

# 1. Split joining_date into year, month and day
emp_df.select(split(col("joining_date"), "-").alias("date_parts")).show(truncate=False)

# 2. Split designation into words
emp_df.select(split(col("designation"), " ").alias("designation_words")).show(truncate=False)

# 3. Split city names
emp_df.select(split(col("city"), " ").alias("city_parts")).show(truncate=False)

# 4. Extract year from joining_date
emp_df.withColumn("year", split(col("joining_date"), "-")[0]).show()

# 5. Create separate columns using split
emp_df.withColumn("year", split(col("joining_date"), "-")[0]).withColumn("month", split(col("joining_date"), "-")[1]).withColumn("day", split(col("joining_date"), "-")[2]).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 17. split() Questions
# MAGIC

# COMMAND ----------

# 1. Split joining_date into year, month and day
emp_df.select(split(col("joining_date"), "-").alias("date_parts")).show(truncate=False)

# 2. Split designation into words
emp_df.select(split(col("designation"), " ").alias("designation_words")).show(truncate=False)

# 3. Split city names
emp_df.select(split(col("city"), " ").alias("city_parts")).show(truncate=False)

# 4. Extract year from joining_date
emp_df.withColumn("year", split(col("joining_date"), "-")[0]).show()

# 5. Create separate columns using split
emp_df.withColumn("year", split(col("joining_date"), "-")[0]).withColumn("month", split(col("joining_date"), "-")[1]).withColumn("day", split(col("joining_date"), "-")[2]).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 18. concat() / concat_ws() Questions
# MAGIC

# COMMAND ----------

# 1. Concatenate name and department
emp_df.select(
    concat(col("name"), col("department")).alias("emp_dept")
).show()

# 2. Create full employee details column
emp_df.select(
    concat_ws(
        " | ",
        col("emp_id"),
        col("name"),
        col("department"),
        col("salary")
    ).alias("employee_details")
).show(truncate=False)

# 3. Concatenate city and department with hyphen
emp_df.select(concat_ws("-", col("city"), col("department")).alias("city_department")).show()

# 4. Create employee label using concat_ws
emp_df.select(concat_ws("_", col("emp_id"), col("name")).alias("employee_label")).show()

# 5. Combine name and designation
emp_df.select(concat_ws(" - ", col("name"), col("designation")).alias("employee_role")).show(truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 19. cast() Questions
# MAGIC

# COMMAND ----------

# 1. Cast salary to double
emp_df.withColumn("salary_double", col("salary").cast("double")).show()

# 2. Cast age to string
emp_df.withColumn("age_string", col("age").cast("string")).show()

# 3. Convert joining_date to date type
emp_df.withColumn("joining_date", col("joining_date").cast("date")).show()

# 4. Cast emp_id to string
emp_df.withColumn("emp_id_string", col("emp_id").cast("string")).show()

# 5. Create numeric bonus column
emp_df.withColumn("bonus", (col("salary") * 0.10).cast("double")).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 20. alias() Questions
# MAGIC

# COMMAND ----------

# 1. Display salary as monthly_salary
emp_df.select(
    col("salary").alias("monthly_salary")
).show()

# 2. Display department as dept_name
emp_df.select(
    col("department").alias("dept_name")
).show()

# 3. Use alias in aggregation
emp_df.groupBy("department").agg(
    avg("salary").alias("average_salary")
).show()

# 4. Rename average salary column using alias
emp_df.agg(
    avg("salary").alias("avg_salary")
).show()

# 5. Use alias in joins
emp_df.alias("e") \
      .join(
          dept_df.alias("d"),
          col("e.department") == col("d.department"),
          "inner"
      ) \
      .select(
          col("e.name"),
          col("d.manager")
      ) \
      .show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 21-50 Sections Answers

# COMMAND ----------

# DBTITLE 1,Cell 48
# 21. lit() Questions

# 1. Add company_name column
emp_df.withColumn("company_name", lit("ABC Technologies")).show()

# 2. Add country column with value India
emp_df.withColumn("country", lit("India")).show()

# 3. Add constant bonus column
emp_df.withColumn("bonus", lit(5000)).show()

# 4. Add status column as Active
emp_df.withColumn("status", lit("Active")).show()

# 5. Add training column with Yes
emp_df.withColumn("training", lit("Yes")).show()

# 22. when() / otherwise() Questions

# 1. Categorize salary as High and Low
emp_df.withColumn("salary_category", when(col("salary") >= 70000, "High").otherwise("Low")).show()

# 2. Categorize employees based on age
emp_df.withColumn("age_category", when(col("age") < 30, "Young").otherwise("Experienced")).show()

# 3. Create experience level column
emp_df.withColumn("experience_level", when(col("age") < 28, "Junior").when(col("age") < 33, "Mid-Level").otherwise("Senior")).show()

# 4. Mark employees eligible for bonus
emp_df.withColumn("bonus_eligible", when(col("salary") > 60000, "Yes").otherwise("No")).show()

# 5. Create department category column
emp_df.withColumn("dept_category", when(col("department").isin("IT", "Analytics"), "Technical").otherwise("Non-Technical")).show()

# 23. substring() Questions

# 1. Extract first 3 characters from name
emp_df.withColumn("name_prefix", substring("name", 1, 3)).show()

# 2. Extract year from joining_date
emp_df.withColumn("joining_year", substring("joining_date", 1, 4)).show()

# 3. Extract first 2 letters of department
emp_df.withColumn("dept_code", substring("department", 1, 2)).show()

# 4. Extract last 3 characters from designation
emp_df.withColumn("designation_suffix", substring(col("designation"), -3, 3)).show()

# 5. Create short employee code
emp_df.withColumn("emp_code", concat(substring("name", 1, 3), col("emp_id"))).show()

# 24. regexp_replace() Questions

# 1. Replace spaces in designation with underscore
emp_df.withColumn("designation", regexp_replace("designation", " ", "_")).show()

# 2. Remove vowels from names
emp_df.withColumn("name_no_vowels", regexp_replace("name", "[AEIOUaeiou]", "")).show()

# 3. Replace Hyderabad with HYD
emp_df.withColumn("city", regexp_replace("city", "Hyderabad", "HYD")).show()

# 4. Remove special characters
emp_df.withColumn("clean_name", regexp_replace("name", "[^a-zA-Z0-9]", "")).show()

# 5. Standardize department names
emp_df.withColumn("department", regexp_replace("department", "IT", "Information Technology")).show()

# 25. like() Questions

# 1. Find names starting with S
emp_df.filter(col("name").like("S%")).show()

# 2. Find designations ending with Engineer
emp_df.filter(col("designation").like("%Engineer")).show()

# 3. Find cities containing 'a'
emp_df.filter(col("city").like("%a%")).show()

# 4. Find departments starting with A
emp_df.filter(col("department").like("A%")).show()

# 5. Find employees whose name contains 'ra'
emp_df.filter(col("name").like("%ra%")).show()

# 26. isin() Questions

# 1. Find employees from Hyderabad and Bangalore
emp_df.filter(col("city").isin("Hyderabad", "Bangalore")).show()

# 2. Find employees in IT and QA departments
emp_df.filter(
    col("department").isin("IT", "QA")).show()

# 3. Find employees with age 28, 30 and 35
emp_df.filter(
    col("age").isin(28, 30, 35)).show()

# 4. Filter female employees from Pune and Chennai
emp_df.filter(
    (col("gender") == "Female") &
    (col("city").isin("Pune", "Chennai"))).show()

# 5. Find employees with specific emp_ids
emp_df.filter(
    col("emp_id").isin(101, 105, 109)).show()

# 27. between() Questions

# 1. Find employees with salary between 50000 and 80000
emp_df.filter(
    col("salary").between(50000, 80000)).show()

# 2. Find employees aged between 25 and 30
emp_df.filter(
    col("age").between(25, 30)).show()

# 3. Find salaries between 60000 and 90000
emp_df.filter(
    col("salary").between(60000, 90000)).show()

# 4. Find employees joined between years
emp_df.filter(
    year(col("joining_date")).between(2020, 2022)).show()

# 5. Find employees with emp_id between 102 and 108
emp_df.filter(
    col("emp_id").between(102, 108)).show()

# 28. pivot() Questions

# 1. Pivot department with average salary
emp_df.groupBy("gender") \
      .pivot("department") \
      .avg("salary") \
      .show()

# 2. Pivot city with employee count
emp_df.groupBy("department") \
      .pivot("city") \
      .count() \
      .show()

# 3. Pivot gender with total salary
emp_df.groupBy("department") \
      .pivot("gender") \
      .sum("salary") \
      .show()

# 4. Pivot department with maximum age
emp_df.groupBy("gender") \
      .pivot("department") \
      .max("age") \
      .show()

# 5. Create department-wise summary table
emp_df.groupBy("gender") \
      .pivot("department") \
      .agg(avg("salary")) \
      .show()


# ==========================================
# 29. stack() Questions
# ==========================================

# Create pivot dataframes for stack examples
pivot_df = emp_df.groupBy("gender").pivot("department").avg("salary")
city_pivot_df = emp_df.groupBy("department").pivot("city").count()
gender_pivot_df = emp_df.groupBy("department").pivot("gender").sum("salary")

# 1. Convert pivoted salary table back to rows
pivot_df.selectExpr(
    "gender",
    "stack(6, 'IT', IT, 'HR', HR, 'QA', QA, 'Analytics', Analytics, 'Support', Support, 'Finance', Finance) as (department, salary)"
).show()

# 2. Unpivot city data
city_pivot_df.selectExpr(
    "department",
    "stack(4, 'Hyderabad', Hyderabad, 'Bangalore', Bangalore, 'Chennai', Chennai, 'Pune', Pune) as (city, count)"
).show()

# 3. Convert department columns into rows
pivot_df.selectExpr(
    "gender",
    "stack(6, 'IT', IT, 'HR', HR, 'QA', QA, 'Analytics', Analytics, 'Support', Support, 'Finance', Finance) as (department, value)"
).show()

# 4. Practice stack function
gender_pivot_df.selectExpr(
    "department",
    "stack(2, 'Male', Male, 'Female', Female) as (gender, total_salary)"
).show()

# 5. Create normalized dataframe
pivot_df.selectExpr(
    "gender",
    "stack(6, 'IT', IT, 'HR', HR, 'QA', QA, 'Analytics', Analytics, 'Support', Support, 'Finance', Finance) as (department, metric)"
).show()

# 30. Window Functions Questions

# 1. Find rank of employees based on salary
window_spec = Window.orderBy(col("salary").desc())
emp_df.withColumn("rank", rank().over(window_spec)).show()

# 2. Find dense_rank department-wise
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())

emp_df.withColumn("dense_rank", dense_rank().over(window_spec)).show()

# 3. Find row_number for employees
window_spec = Window.orderBy("emp_id")
emp_df.withColumn("row_num", row_number().over(window_spec)).show()

# 4. Find lead salary
window_spec = Window.orderBy("salary")
emp_df.withColumn("next_salary", lead("salary").over(window_spec)).show()

# 5. Find lag salary
window_spec = Window.orderBy("salary")
emp_df.withColumn("previous_salary", lag("salary").over(window_spec)).show()

# 31. repartition() Questions

# 1. Repartition dataframe into 4 partitions
repartitioned_df = emp_df.repartition(4)
print("Dataframe repartitioned to 4 partitions")

# 2. Repartition by department
dept_repartitioned_df = emp_df.repartition("department")
print("Dataframe repartitioned by department column")

# 3. Check partition count (Note: .rdd.getNumPartitions() not available on serverless)
print("Note: Partition count verification not available on serverless compute")

# 4. Compare repartition and coalesce
repartition_df = emp_df.repartition(4)
coalesce_df = emp_df.coalesce(2)
print("Repartition and coalesce operations completed")
print("Note: Partition count comparison not available on serverless compute")

# 5. Repartition large datasets
large_df = emp_df.repartition(8)
print("Large dataset repartitioned to 8 partitions")

# COMMAND ----------

# MAGIC %md
# MAGIC # Project 1: Employee Salary Analysis
# MAGIC

# COMMAND ----------

# 1. Find average salary department-wise
emp_df.groupBy("department").avg("salary").show()

# 2. Find highest salary employee in each department
from pyspark.sql.window import Window

window_spec = Window.partitionBy("department").orderBy(col("salary").desc())

emp_df.withColumn("rank", dense_rank().over(window_spec)).filter(col("rank") == 1).show()

# 3. Find employees earning above department average
dept_avg = emp_df.groupBy("department").agg(avg("salary").alias("avg_salary"))

emp_df.join(dept_avg, "department").filter(col("salary") > col("avg_salary")).show()

# 4. Department-wise employee count
emp_df.groupBy("department").count().show()

# 5. Department-wise salary summary
emp_df.groupBy("department").agg(min("salary").alias("min_salary"), max("salary").alias("max_salary"), avg("salary").alias("avg_salary")).show()

# COMMAND ----------

# MAGIC %md
# MAGIC # Project 2: Employee Skills Analysis

# COMMAND ----------

# 1. Explode skills array
skills_df.select("emp_id", explode("skills").alias("skill")).show()

# 2. Count employees by skill
skills_df.select(explode("skills").alias("skill")).groupBy("skill").count().show()

# 3. Find employees with Python skill
skills_df.filter(array_contains("skills", "Python")).show()

# 4. Find most popular skill
skills_df.select(explode("skills").alias("skill")).groupBy("skill").count().orderBy(col("count").desc()).show()

# 5. Find distinct skills
skills_df.select(explode("skills").alias("skill")).distinct().show()

# COMMAND ----------

# MAGIC %md
# MAGIC # Project 3: Employee Performance Dashboard

# COMMAND ----------

# 1. Categorize employees by salary
emp_df.withColumn("salary_band", when(col("salary") >= 80000, "High").when(col("salary") >= 50000, "Medium").otherwise("Low")
).show()

# 2. Create yearly salary column
emp_df.withColumn("yearly_salary", col("salary") * 12).show()

# 3. Department-wise salary distribution
emp_df.groupBy("department").avg("salary").show()

# 4. Top 5 highest paid employees
emp_df.orderBy(col("salary").desc()).limit(5).show()

# 5. Employee summary dashboard
emp_df.groupBy("department"
).agg(
    count("*").alias("employee_count"),
    avg("salary").alias("avg_salary"),
    max("salary").alias("highest_salary")
).show()

# COMMAND ----------

# MAGIC %md
# MAGIC #  Bonus Challenges (1-10)

# COMMAND ----------

# =========================================================
# BONUS CHALLENGE QUESTIONS - COMPLETE CODE
# =========================================================

from pyspark.sql.functions import *
from pyspark.sql.window import Window

# Bonus Challenge 1
# Find Top 3 Highest Paid Employees in Each Department

window_spec = Window.partitionBy("department").orderBy(col("salary").desc())

emp_df.withColumn(
    "rank",
    dense_rank().over(window_spec)
).filter(
    col("rank") <= 3
).show()

# Bonus Challenge 2
# Find Employees Earning Above Department Average

dept_avg = emp_df.groupBy("department").agg(avg("salary").alias("avg_salary"))

emp_df.join(
    dept_avg,
    "department"
).filter(
    col("salary") > col("avg_salary")
).show()

# Bonus Challenge 3
# Find Second Highest Salary Employee

window_spec = Window.orderBy(col("salary").desc())

emp_df.withColumn("rank", dense_rank().over(window_spec)).filter(col("rank") == 2).show()

# Bonus Challenge 4
# Find Running Total of Salary

window_spec = Window.orderBy("emp_id")

emp_df.withColumn("running_total_salary", sum("salary").over(window_spec)).show()

# Bonus Challenge 5
# Find Salary Difference from Previous Employee

window_spec = Window.orderBy("salary")

emp_df.withColumn("previous_salary", lag("salary").over(window_spec)).withColumn("salary_difference", col("salary") - col("previous_salary")).show()

# Bonus Challenge 6
# Find Department with Highest Average Salary

emp_df.groupBy("department").agg(avg("salary").alias("avg_salary")).orderBy(col("avg_salary").desc()).limit(1).show()

# Bonus Challenge 7
# Find Most Common Skill

skills_df.select(explode("skills").alias("skill")).groupBy("skill").count().orderBy(col("count").desc()).limit(1).show()

# Bonus Challenge 8
# Find Employees Having More Than 2 Skills

skills_df.filter(size(col("skills")) > 2).show()

# Bonus Challenge 9
# Department-wise Salary Ranking

window_spec = Window.partitionBy("department").orderBy(col("salary").desc())
emp_df.withColumn("department_rank", rank().over(window_spec)).show()

# Bonus Challenge 10
# Employee Performance Summary

emp_df.groupBy("department").agg(count("*").alias("employee_count"), avg("salary").alias("avg_salary"), max("salary").alias("highest_salary"), min("salary").alias("lowest_salary")).show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## 