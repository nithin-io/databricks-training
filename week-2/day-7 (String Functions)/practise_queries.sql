-- 1. Find length of full name
SELECT full_name, LENGTH(full_name) FROM employees;

-- 2. Find character length of full name
SELECT full_name, CHAR_LENGTH(full_name) FROM employees;

-- 3. Convert department to uppercase
SELECT UPPER(department) FROM employees;

-- 4. Convert city to lowercase
SELECT LOWER(city) FROM employees;

-- 5. Remove spaces from both sides of full name
SELECT TRIM(full_name) FROM employees;

-- 6. Remove left spaces
SELECT LTRIM(full_name) FROM employees;

-- 7. Remove right spaces
SELECT RTRIM(full_name) FROM employees;

-- 8. Concatenate full name and department
SELECT CONCAT(full_name, ' - ', department) AS emp_details FROM employees;

-- 9. Concatenate with separator
SELECT CONCAT_WS(' | ', emp_id, full_name, city) FROM employees;

-- 10. Extract first 7 characters of email
SELECT SUBSTRING(email, 1, 7) FROM employees;

-- 11. Extract first 5 characters using SUBSTR
SELECT SUBSTR(email, 1, 5) FROM employees;

-- 12. Extract first 4 characters of full name
SELECT LEFT(full_name, 4) FROM employees;

-- 13. Extract last 3 characters of city
SELECT RIGHT(city, 3) FROM employees;

-- 14. Find position of @ in email
SELECT email, INSTR(email, '@') FROM employees;

-- 15. Find position of dot in email
SELECT email, LOCATE('.', email) FROM employees;

-- 16. Replace Data with Big Data
SELECT REPLACE(department, 'Data', 'Big Data') FROM employees;

-- 17. Reverse full name
SELECT full_name, REVERSE(full_name) FROM employees;

-- 18. Pad emp_id with zeros
SELECT LPAD(emp_id, 5, '0') FROM employees;

-- 19. Pad city with *
SELECT RPAD(city, 15, '*') FROM employees;

-- 20. Remove spaces inside city name
SELECT TRIM(REPLACE(city, ' ', '')) FROM employees;

-- 21. Replace NULL remarks with No remarks
SELECT full_name, IFNULL(remarks, 'No remarks') FROM employees;

-- 22. Return first non-null value
SELECT full_name, COALESCE(remarks, 'N/A') FROM employees;

-- 23. Search Analytics in CSV list
SELECT FIND_IN_SET('Analytics', 'Data,Analytics,AI');

-- 24. Extract domain name from email
SELECT SUBSTRING_INDEX(email, '@', -1) FROM employees;

-- 25. Extract username from email
SELECT SUBSTRING_INDEX(email, '@', 1) FROM employees;

-- 26. Count total characters in department
SELECT department, LENGTH(department) FROM employees;

-- 27. Find employees whose name starts with K
SELECT full_name FROM employees WHERE full_name LIKE 'K%';

-- 28. Find employees whose city ends with e
SELECT city FROM employees WHERE city LIKE '%e';

-- 29. Find names containing 'a'
SELECT full_name FROM employees WHERE full_name LIKE '%a%';

-- 30. Compare city ignoring case
SELECT city FROM employees WHERE LOWER(city)='hyderabad';