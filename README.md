## Challenge understanding:
### Main Challenge: 
 create an algorithm that implements a calculator using Reverse Polish Notation (RPN). 
 Reverse Polish Notation is a mathematical notation in which every operator follows all of its operands. 
 It does not need any parentheses as long as each operator has a fixed number of operands.
 ### Extension:
- **FastAPI Implementation**: Develop a REST API with endpoints to evaluate expressions and return results.
- **Database Integration**: Use an Postgresql database to store operations and results.
- **CSV Export**: Provide an endpoint to export data from the database to a CSV file.

## Explanation of code:
- **Input Handling**: The expression is split into individual tokens (numbers and operators).
- **Stack Initialization**: An empty list is used as a stack to store numbers.
- **Operators Dictionary**: A dictionary maps operators to their corresponding lambda functions for easy computation.
- **Token Processing**:
    If a token is an operator, two operands are popped from the stack, the operation is performed, and the result is pushed back onto the stack.
    If a token is a number, it is converted to a float and pushed onto the stack.
- **Final Result**: After processing all tokens, the remaining item on the stack is the result of the expression.

This code handles basic arithmetic operations (+, -, *, /). You can extend the operators dictionary to support more operations if needed.

### Running the app:
To run the application, you simply need to execute docker-compose up. 
This command will create and run two containers: one for the PostgreSQL database, initialized with an init.sql script to set up the necessary schema and tables, and the other for the backend application, which depends on the database
```sh

docker-compose up
```

Additionally, I have implemented unit tests to verify the correctness of the algorithm used in the calculation process.
```sh

python -m unittest test_rpn_service.py
```

### Understanding Database tables:
![image](https://github.com/BenrhayemRacem/ayomi_ex1/assets/59982299/81051060-d959-421b-badf-8191ecab9804)

### Explanation:
- Classes:
  
  - **Operation**: Represents the operation table with fields id, created_at, expression, result, and updated_at.
  
  - **Step**: Represents the step table with fields id, created_at, index, execution, operation_id, and updated_at.
- Relationship:
     A Operation can contain multiple Step objects (1 to 0..* relationship). The foreign key (operation_id) in the step table references the primary key (id) in the operation table.

The **operation table** saves the expression and the result after RPN calculation.

The **step table** saves the steps executed to calculate the result of an expression.

### Example:

Expression: "2 3 + 5 *" --> Result : 25

Steps : 
-  2 + 3 = 5
- 5 * 5 = 25

## Docs:
You can access API docs on:
```sh

localhost:8000/docs
```
