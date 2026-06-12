# Beginner Explanatory Guide: SEC-301: Fix SQL Injection Vulnerabilities in User Search

> **Task Type**: Product Task  
> **Domain/Focus**: Security in Database Queries

---

## 1. The Goal (In-Depth Beginner Explanation)

### The Core Problem
In the context of our application, the user search module is currently vulnerable to SQL injection attacks. SQL injection is a type of security exploit where an attacker can manipulate SQL queries by injecting malicious input. For instance, if a user inputs a search query like `' OR '1'='1`, the application could execute a query that returns all records from the database instead of just the intended results. This is a critical security flaw because it allows unauthorized access to sensitive data, potentially exposing user information and compromising the integrity of the database.

The problem arises from the way SQL queries are constructed in the code. Currently, the application uses string concatenation to build SQL queries, which is unsafe. This method allows attackers to manipulate the SQL commands by inserting their own code through user inputs. Fixing this issue is crucial not only for protecting user data but also for maintaining the trust of users in the application. If left unaddressed, these vulnerabilities could lead to severe data breaches and legal ramifications for the organization.

### Jargon Buster (Key Terms Explained)
* **SQL Injection**: A code injection technique that exploits a security vulnerability in an application's software by manipulating SQL queries. For example, if a user inputs `'; DROP TABLE users; --`, it could delete the entire users table if not properly handled.
* **Parameterized Queries**: A method of structuring SQL queries that separates the SQL code from the data being input. This prevents attackers from injecting malicious SQL code. For instance, using `cursor.execute("SELECT * FROM users WHERE name = ?", (name,))` ensures that `name` is treated as data, not executable code.
* **String Concatenation**: The process of joining strings together to form a new string. In SQL queries, this can lead to vulnerabilities if user input is directly concatenated into the query string. For example, `query = "SELECT * FROM users WHERE name = '" + user_input + "'"` is unsafe.
* **Input Sanitization**: The process of cleaning user input to remove or escape potentially harmful characters. This is crucial for preventing SQL injection and other types of attacks.

### Expected Outcome
After implementing the solution, the user search module should behave securely and correctly. The expected outcomes are as follows:

- **Before**: If a user inputs a malicious query like `' OR '1'='1`, the application returns all user records, exposing sensitive data.
- **After**: The same input should return zero results, effectively blocking the SQL injection attempt. Additionally, normal search queries should still function correctly, returning the expected user records without any security risks.

---

## 2. Related Coding Concepts & Syntax (50% Theory, 50% Practice)

### Concept 1: Parameterized Queries
#### 📘 Theoretical Overview (50%)
* **Why it exists**: Parameterized queries exist to enhance security by preventing SQL injection attacks. When user input is directly included in SQL statements, it can lead to vulnerabilities. By using parameterized queries, the database treats user input as data rather than executable code, which significantly reduces the risk of injection attacks.
* **Key Mechanisms**: The core mechanism involves using placeholders (often represented by `?` in SQLite) in the SQL statement. When the query is executed, the database engine safely binds the user input to these placeholders, ensuring that any malicious input is not executed as part of the SQL command.

#### 💻 Syntax & Practical Examples (50%)
* **Language Syntax**:
  ```python
  import sqlite3

  # Establish a connection to the database
  conn = sqlite3.connect('example.db')

  # Create a cursor object
  cursor = conn.cursor()

  # Using parameterized queries
  name = "Alice"
  cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
  results = cursor.fetchall()
  ```
* **Real-World Application**:
  ```python
  def search_user_by_name(name):
      conn = sqlite3.connect('example.db')
      cursor = conn.cursor()
      # Using parameterized query to prevent SQL injection
      cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
      return cursor.fetchall()
  ```

---

## 3. Step-by-Step Logic & Walkthrough

1. **Step 1: Locate and Analyze the Target File**
   * Navigate to the `userSearch.py` file in the `p-w11-task-03` folder. This file contains the methods that need to be modified to prevent SQL injection.
   * Focus on the methods `search_by_name`, `search_by_email`, and `get_by_role`. These methods currently use string concatenation to build SQL queries.

2. **Step 2: Input Verification & Validation**
   * Before modifying the SQL queries, ensure that the input values are valid. Check for edge cases such as empty strings or null values. For example, if `name` is an empty string, the search should return no results.

3. **Step 3: Core Implementation / Modification**
   * Modify each method to use parameterized queries instead of string concatenation. For example:
     - Change `query = f"SELECT * FROM users WHERE name LIKE '%{name}%'"` to `query = "SELECT * FROM users WHERE name LIKE ?"`.
     - Use `cursor.execute(query, ('%' + name + '%',))` to safely bind the user input.

4. **Step 4: Output Verification & Testing**
   * After making the changes, run the tests in `test_security.py` to ensure that all tests pass. This will verify that the search functionality works correctly and that SQL injection attempts return zero results.

---

## 4. Detailed Walkthrough of Test Cases

### Test Case 1: Standard / Success Case
* **Description**: This test checks if the search function correctly returns results for a valid input.
* **Inputs**:
  ```json
  {
    "name": "Alice"
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The input value "Alice" is received by the `search_by_name` function.
  2. The function constructs a parameterized query: `query = "SELECT * FROM users WHERE name LIKE ?"`
  3. The main logic executes: `cursor.execute(query, ('%Alice%',))`, which safely binds the input.
  4. The function returns the final result, which should include Alice's record.
* **Expected Output**: 
  ```json
  [
    (1, 'Alice Admin', 'alice@corp.com', 'admin')
  ]
  ```

### Test Case 2: Edge Case / Validation Fail
* **Description**: This test checks if the search function correctly handles an SQL injection attempt.
* **Inputs**:
  ```json
  {
    "name": "' OR '1'='1"
  }
  ```
* **Step-by-Step Execution Trace**:
  1. The input value `"' OR '1'='1"` is received by the `search_by_name` function.
  2. The function constructs a parameterized query: `query = "SELECT * FROM users WHERE name LIKE ?"`
  3. The validation block detects that the input is an injection attempt but is safely handled by the parameterized query.
  4. The execution is completed, and the function returns zero results.
* **Expected Output**: 
  ```json
  []
  ``` 

This guide provides a comprehensive understanding of the task at hand, ensuring that even beginners can grasp the concepts and steps necessary to fix SQL injection vulnerabilities in the user search module.