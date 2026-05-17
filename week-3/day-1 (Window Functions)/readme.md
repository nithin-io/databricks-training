# 📅 Week 3 - Day 1

# 🏆 SQL Window Assignment (ROW_NUMBER, RANK, DENSE_RANK)

## 🎯 Objective

The objective of this practice session is to understand and implement **SQL Window Ranking Functions** using relational database tables such as **Employees**. This session focuses on ranking data records, assigning sequential row numbers, handling duplicate rankings, partition-based ranking, and real-time business analytical reporting using advanced SQL window functions.

---

# 🧱 Database Setup

The following table was used for SQL Window Functions practice:

👨‍💼 **Employees**

The database schema includes:

- Employee salary records
- Department-wise employee grouping
- Joining date analysis
- Duplicate salary handling
- Ranking-based business insights

---

# 🔑 Core Concepts Implemented

- Sequential Row Assignment
- Partition-Based Ranking
- Duplicate Rank Handling
- Dense Ranking Logic
- Salary-Based Sorting
- Date-Based Ranking
- Department-wise Analysis
- Real-Time Business Ranking Scenarios

---

# 📚 Topics Covered

## 1️⃣ ROW_NUMBER() Function

Using:

`ROW_NUMBER() OVER()`

Assigning:

- Unique sequential row numbers
- Ordered salary ranking
- Date-based row numbering
- Department-wise numbering

---

## 2️⃣ Global Ranking

Applying:

`ORDER BY`

Ranking employees based on:

- Highest salary
- Lowest salary
- Latest joining date
- Alphabetical employee names

---

## 3️⃣ Department-Wise Partitioning

Using:

`PARTITION BY department`

Performing:

- Salary ranking inside departments
- Joining date sequencing
- Name-wise numbering
- Internal department analytics

---

## 4️⃣ RANK() Function

Using:

`RANK() OVER()`

Features:

- Duplicate values receive same rank
- Ranking gaps appear automatically

Examples:

- Salary competition ranking
- Department-wise salary comparison
- Joining-date hierarchy

---

## 5️⃣ DENSE_RANK() Function

Using:

`DENSE_RANK() OVER()`

Features:

- Duplicate values share same rank
- No ranking gaps

Used for:

- Compact salary ranking
- Continuous department ranking
- Performance hierarchy generation

---

## 6️⃣ Salary-Based Ranking Analysis

Performing:

- Highest-paid employee identification
- Lowest salary comparison
- Duplicate salary detection
- Compensation hierarchy creation

Business Use Cases:

- Payroll analysis
- Compensation benchmarking
- Promotion eligibility ranking

---

## 7️⃣ Joining Date Ranking

Finding:

- Recently joined employees
- Oldest employees
- Department joining sequence

Useful for:

- Experience analysis
- Employee tenure reporting
- Workforce growth tracking

---

## 8️⃣ Alphabetical Ranking Operations

Sorting employees based on:

- Employee name ascending
- Department-wise alphabetical ranking

Used for:

- HR reporting
- Employee directory generation
- Structured listing

---

## 9️⃣ Real-Time Business Partition Analytics

Applying ranking within departments for:

- Chennai salary comparison
- Hyderabad salary hierarchy
- Bangalore joining analysis

Helps in:

- Regional performance analysis
- Departmental comparisons
- Internal organizational reporting

---

## 🔟 Duplicate Value Handling

Comparing behavior of:

**ROW_NUMBER()**

- Always unique

**RANK()**

- Duplicate ranks with gaps

**DENSE_RANK()**

- Duplicate ranks without gaps

Improves understanding of ranking strategy selection.

---

# 💻 Practice Work

✅ Solved **24 SQL Window Function queries**

📈 Covered beginner to advanced ranking scenarios

🌍 Practiced real-world analytical scenarios including:

- Salary leaderboard generation
- Department-wise ranking
- Employee hierarchy analysis
- Date-based reporting
- Duplicate value handling

---

# 🧠 Key Learnings

- Understanding SQL window function behavior
- Differentiating ranking methods
- Applying partition-based analysis
- Handling duplicate ranking values
- Performing advanced business analytics
- Writing production-ready ranking queries

---

# 🛠️ Tools Used

🧪 **DB-Fiddle**

🐬 **MySQL**

🌐 **GitHub**

---

# 🚀 Next Steps

- Learn **LEAD() and LAG()**
- Practice **FIRST_VALUE() and LAST_VALUE()**
- Explore advanced analytical reporting
- Build ranking dashboards using SQL

---

# 📁 Files Included

| File Name | Description |
|-----------|-------------|
| `data_creation.sql` | Employees table structure with sample records |
| `practice_queries.sql` | Collection of ROW_NUMBER(), RANK(), DENSE_RANK() queries |
| `README.md` | Documentation for Day 5 SQL Window Functions practice |

---

# ✅ Conclusion

This practice session strengthened SQL analytical query-writing skills through hands-on implementation of **ROW_NUMBER(), RANK(), and DENSE_RANK()** functions. The exercises improved practical understanding of sequential numbering, duplicate ranking behavior, partition-based analysis, and real-time business reporting scenarios, building strong foundational knowledge for advanced SQL analytics and reporting solutions.
