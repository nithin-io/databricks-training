# Databricks notebook source
# MAGIC %md
# MAGIC **Reading and displaying the empData Data**

# COMMAND ----------

df1 = spark.read.format("csv").option("header",True).option("inferSchema",True).load("/Volumes/workspace/default/databricks2027/empData.csv")
df1.display()

# COMMAND ----------

# MAGIC %md
# MAGIC **Reading and displaying the Big Sales Data**

# COMMAND ----------

df2 = spark.read.format("csv").option("header",True).option("inferSchema",True).load("/Volumes/workspace/default/databricks2027/Big Sales.csv")
df2.display()