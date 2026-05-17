# 📅 Week 2 - Day 7

# 🔤 SQL String Functions Assignment

## 🎯 Objective

The objective of this practice session is to understand and implement **SQL String Functions** using relational database tables such as **Employee Records**. This session focuses on text manipulation, formatting operations, string searching, extraction, replacement, trimming spaces, and real-time business string processing.

---

# 🧱 Database Setup

The following table was used for SQL String Functions practice:

👨‍💼 Employee Records

The database schema includes:

- Employee name formatting
- Email string extraction
- Department text processing
- City string cleaning
- NULL string handling
- String-based business data analysis

---

# 🔑 Core Concepts Implemented

- String Length Analysis
- Text Case Conversion
- String Trimming
- String Concatenation
- Character Extraction
- Substring Search
- String Replacement
- String Padding
- NULL Handling
- CSV String Search Logic

---

# 📚 Topics Covered

## 1️⃣ LENGTH() / CHAR_LENGTH() Function

### Using:

```sql
LENGTH(string)
CHAR_LENGTH(string)
```

### Purpose

- Calculate total string length
- Character counting analysis
- Validate text size

**Note:**  
CHAR_LENGTH() is safer for multi-byte characters.

---

## 2️⃣ UPPER() / LOWER() Function

### Using:

```sql
UPPER(string)
LOWER(string)
```

### Purpose

- Convert text case
- Standardize formatting
- Improve consistency

---

## 3️⃣ TRIM() / LTRIM() / RTRIM() Function

### Using:

```sql
TRIM(string)
LTRIM(string)
RTRIM(string)
```

### Purpose

- Remove unwanted spaces
- Clean imported text
- Normalize records

---

## 4️⃣ CONCAT() Function

### Using:

```sql
CONCAT(str1, str2)
```

### Purpose

- Join multiple strings
- Generate readable output
- Build formatted reports

---

## 5️⃣ CONCAT_WS() Function

### Using:

```sql
CONCAT_WS(separator, values)
```

### Purpose

- Join strings using separator
- Create structured display output
- Reporting-friendly formatting

---

## 6️⃣ SUBSTRING() / SUBSTR() Function

### Using:

```sql
SUBSTRING(string,start,length)
SUBSTR(string,start,length)
```

### Purpose

- Extract selected text
- Partial string analysis
- Retrieve meaningful segments

---

## 7️⃣ LEFT() / RIGHT() Function

### Using:

```sql
LEFT(string,n)
RIGHT(string,n)
```

### Purpose

- Extract prefix characters
- Extract suffix characters
- Short text formatting

---

## 8️⃣ INSTR() Function

### Using:

```sql
INSTR(string,substring)
```

### Purpose

- Find substring position
- Locate characters
- Validation analysis

---

## 9️⃣ LOCATE() Function

### Using:

```sql
LOCATE(substring,string)
```

### Purpose

- Search substring position
- Flexible indexing
- Pattern identification

---

## 🔟 REPLACE() Function

### Using:

```sql
REPLACE(string,old,new)
```

### Purpose

- Replace unwanted text
- Standardize values
- Clean inconsistent data

---

## 1️⃣1️⃣ REVERSE() Function

### Using:

```sql
REVERSE(string)
```

### Purpose

- Reverse text strings
- Analytical text testing
- Transformation operations

---

## 1️⃣2️⃣ LPAD() / RPAD() Function

### Using:

```sql
LPAD(string,length,pad)
RPAD(string,length,pad)
```

### Purpose

- Add padding characters
- Fixed-width formatting
- Professional reporting alignment

---

## 1️⃣3️⃣ TRIM() + REPLACE() Combined Usage

### Using:

```sql
TRIM(REPLACE(string,' ',''))
```

### Purpose

- Remove internal spaces
- Normalize text storage
- Data cleanup operations

---

## 1️⃣4️⃣ IFNULL() Function

### Using:

```sql
IFNULL(value,replacement)
```

### Purpose

- Replace NULL values
- Avoid blank outputs
- Ensure readable reporting

---

## 1️⃣5️⃣ COALESCE() Function

### Using:

```sql
COALESCE(value1,value2)
```

### Purpose

- Return first non-NULL value
- Safe fallback logic
- Default data handling

---

## 1️⃣6️⃣ FIND_IN_SET() Function

### Using:

```sql
FIND_IN_SET(value,csv_list)
```

### Purpose

- Search CSV strings
- Membership validation
- Set-based text checks

---

# 💻 Practice Work

✅ Solved 30 SQL String Function queries

📈 Covered beginner to advanced-level string operations

🌍 Practiced real-world scenarios including:

- Employee name formatting
- Email extraction
- Department standardization
- City string cleanup
- NULL handling
- Text analytics

---

# 🧠 Key Learnings

- Understanding SQL string manipulation
- Cleaning raw text efficiently
- Standardizing business records
- Extracting useful text patterns
- Performing text validation
- Handling NULL string values professionally

---

# 🛠️ Tools Used

🧪 DB-Fiddle

🐬 MySQL

🌐 GitHub

---

# 🚀 Next Steps

- Learn advanced REGEXP functions
- Practice pattern matching queries
- Explore string indexing optimization
- Build text analytics reports

---

# 📁 Files Included

| File Name | Description |
|-----------|-------------|
| datacreation.sql | Employee table structure with sample string data |
| practice_queries.sql | Collection of SQL string function queries |
| README.md | Documentation for Day 7 SQL String Functions practice |

---

# ✅ Conclusion

This practice session strengthened SQL String Functions fundamentals through hands-on implementation of text formatting, searching, extraction, replacement, trimming, concatenation, and NULL handling. The exercises improved practical SQL query-writing confidence for handling real-world business text data efficiently in production environments.
This practice session strengthened SQL String Functions fundamentals through hands-on implementation of text formatting, searching, extraction, replacement, trimming, concatenation, and NULL handling. The exercises improved practical SQL query-writing confidence for handling real-world business text data efficiently in production environments.
