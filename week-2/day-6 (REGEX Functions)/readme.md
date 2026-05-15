# 📅 Week 2 - Day 6

# 🔍 SQL Regular Expressions (REGEX) Assignment

## 🎯 Objective

The objective of this practice session is to understand and implement **SQL Regular Expressions (REGEX Functions)** using relational database tables such as **Regex Practice Data**. This session focuses on pattern matching, text extraction, substring searching, validation rules, and real-time business data parsing using SQL REGEX operations.

---

# 🧱 Database Setup

The following table was used for SQL REGEX practice:

* 📝 Regex Practice

The database schema includes:

* Employee text identifiers
* Email address pattern extraction
* Phone number parsing
* Mixed alphanumeric value processing
* Country code detection
* Domain and username extraction

---

# 🔑 Core Concepts Implemented

* Pattern Matching
* String Extraction
* Numeric Detection
* Alphabetic Detection
* Boundary Matching
* Prefix and Suffix Search
* Continuous Sequence Identification
* Business Data Validation

---

# 📚 Topics Covered

## 1️⃣ Beginning Numeric Extraction

Using:

* `^[0-9]+`

Examples:

* Extract numeric values from the start of strings
* Identify starting number patterns
* Validate numeric prefixes

---

## 2️⃣ Ending Numeric Extraction

Using:

* `[0-9]+$`

Examples:

* Extract ending numeric values
* Validate suffix numbers
* Capture final digit sequences

---

## 3️⃣ First Character Extraction

Using:

* `^.`

Examples:

* Extract first character
* Detect starting symbols
* Identify string prefix

---

## 4️⃣ Last Character Extraction

Using:

* `.$`

Examples:

* Extract final character
* Detect ending symbol
* Validate suffix characters

---

## 5️⃣ Fixed-Length Numeric Matching

Using:

* `[0-9]{2}`

Examples:

* Extract exactly two digits
* Validate short numeric groups
* Pattern-restricted matching

---

## 6️⃣ Single Digit Detection

Using:

* `[0-9]`

Examples:

* Extract one numeric character
* Detect digit presence
* Basic numeric scanning

---

## 7️⃣ Country Code Extraction

Using:

* Numeric prefix extraction from phone numbers

Examples:

* Detect phone country code
* Validate international format
* Telecom data parsing

---

## 8️⃣ Numeric Extraction Between Text

Using:

* Numeric sequence between alphabets

Examples:

* Extract embedded numbers
* Parse mixed-value strings
* Business identifier extraction

---

## 9️⃣ Username Extraction from Email

Using:

* Text before `@`

Examples:

* Extract email usernames
* User identity parsing
* Login data processing

---

## 🔟 Domain Extraction from Email

Using:

* Text after `@`

Examples:

* Detect provider domains
* Domain validation
* Email parsing logic

---

## 1️⃣1️⃣ Domain Name Detection

Using:

* Domain extraction without `@`

Examples:

* Business email verification
* Domain-specific processing
* Email analytics

---

## 1️⃣2️⃣ Top-Level Domain Extraction

Using:

* Text after final dot

Examples:

* Extract `.com`, `.in`, `.uk`
* Validate TLD structure
* Regional domain classification

---

## 1️⃣3️⃣ Continuous Alphabetic Extraction

Using:

* `[A-Za-z]+`

Examples:

* Extract alphabetic sequences
* Validate text-only sections
* Character classification

---

## 1️⃣4️⃣ Continuous Numeric Extraction

Using:

* `[0-9]+`

Examples:

* Extract number groups
* Detect digit blocks
* Parse structured values

---

## 1️⃣5️⃣ Prefix Text Extraction

Using:

* First fixed-length characters

Examples:

* Extract identifiers
* Prefix validation
* Business code detection

---

## 1️⃣6️⃣ Suffix Text Extraction

Using:

* Last fixed-length characters

Examples:

* Extract ending codes
* Validate suffixes
* Country code parsing

---

## 1️⃣7️⃣ Employee Number Extraction

Using:

* Numeric sequence between text patterns

Examples:

* Extract employee IDs
* Business identifier parsing
* Structured code analysis

---

## 1️⃣8️⃣ Ending Country Code Detection

Using:

* Numeric suffix pattern

Examples:

* Country code validation
* Regional classification
* Text parsing logic

---

## 1️⃣9️⃣ Alphabetic Extraction Between Delimiters

Using:

* Text between underscores

Examples:

* Parse embedded text
* Detect location codes
* Structured string processing

---

## 2️⃣0️⃣ Plus-Sign Numeric Extraction

Using:

* Digits immediately after `+`

Examples:

* International number validation
* Country code detection
* Telecom formatting analysis

---

# 💻 Practice Work

✅ Solved 20 SQL REGEX extraction queries

📈 Covered beginner to advanced-level pattern matching

🌍 Practiced real-world scenarios including:

* Email parsing
* Phone validation
* Employee ID extraction
* Mixed-value processing
* Domain classification
* Structured business data extraction

---

# 🧠 Key Learnings

* Understanding SQL REGEX fundamentals
* Extracting structured text efficiently
* Applying regex boundaries effectively
* Validating business data patterns
* Handling email and phone parsing professionally
* Improving text-processing query logic

---

# 🛠️ Tools Used

* 🧪 DB-Fiddle
* 🐬 MySQL
* 🌐 GitHub

---

# 🚀 Next Steps

* Learn advanced REGEXP_REPLACE()
* Practice REGEXP_LIKE()
* Explore regex validation logic
* Build business data-cleaning queries

---

# 📁 Files Included

| File Name | Description |
|-----------|-------------|
| `data_creation.sql` | Regex practice table structure with sample data |
| `practice_queries.sql` | Collection of SQL REGEX extraction queries |
| `README.md` | Documentation for Day 6 SQL REGEX practice |

---

# ✅ Conclusion

This practice session strengthened SQL REGEX fundamentals through hands-on implementation of pattern matching, text extraction, numeric parsing, email validation, phone number analysis, and structured business data processing. The exercises improved practical SQL query-writing confidence for handling real-world text validation and regex-based database operations effectively in production environments.
