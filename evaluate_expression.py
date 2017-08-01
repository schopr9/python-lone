"""
1. While there are still tokens to be read in,                 
   1.1 Get the next token.
   1.2 If the token is:
       1.2.1 A number: push it onto the value stack.
       1.2.2 A variable: get its value, and push onto the value stack.
       1.2.3 A left parenthesis: push it onto the operator stack.
       1.2.4 A right parenthesis:
         1 While the thing on top of the operator stack is not a 
           left parenthesis,
             1 Pop the operator from the operator stack.
             2 Pop the value stack twice, getting two operands.
             3 Apply the operator to the operands, in the correct order.
             4 Push the result onto the value stack.
         2 Pop the left parenthesis from the operator stack, and discard it.
       1.2.5 An operator (call it thisOp):
         1 While the operator stack is not empty, and the top thing on the
           operator stack has the same or greater precedence as thisOp,
           1 Pop the operator from the operator stack.
           2 Pop the value stack twice, getting two operands.
           3 Apply the operator to the operands, in the correct order.
           4 Push the result onto the value stack.
         2 Push thisOp onto the operator stack.
2. While the operator stack is not empty,
    1 Pop the operator from the operator stack.
    2 Pop the value stack twice, getting two operands.
    3 Apply the operator to the operands, in the correct order.
    4 Push the result onto the value stack.
3. At this point the operator stack should be empty, and the value
   stack should have only one value in it, which is the final result.
"""

output = []

def evaluate_expression(operator, a, b):
    if operator == "-":
        return b - a
    elif operator == "+":
        return a + b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if a == 0:
            raise "divide by zero"
        return  b / a 
    return  0           

def hasPrecedence(op1, op2):

    if (op2 == '(' or op2 == ')'):
        return False
    if ((op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-')):
        return False
    else:
        return True

input = '352 + 3 + (5 * (5 / 2))'
input_array = list(input)
value_stack = []
operator_stack = []
x = 0

for i in range(len(input_array) - 2):
    print input_array[x]
    if input_array[x] == ' ':
        x += 1
        continue

    if input_array[x].isdigit():
        number = input_array[x]
        while input_array[x + 1].isdigit():
            x = x + 1
            number = number + input_array[x]
        value_stack.append(int(number))
        x += 1
    elif input[x] == '(':
        operator_stack.append(input[x])
        x += 1
    elif input[x] == ')':
        print operator_stack
        for k in range (len(operator_stack) - 1, 0, -1):
            if operator_stack[k] == '(':
                operator_stack.pop()
                break
            result = evaluate_expression(operator_stack.pop(), value_stack.pop(), value_stack.pop())
            print result
            value_stack.append(result)
        x += 1
    elif input[x] == '+' or input[x] == '-' or input[x] == '*' or input[x] == '/':        
        
        while operator_stack != [] and hasPrecedence(input[x], operator_stack[-1]):            
            value_stack.append(evaluate_expression(operator_stack.pop(), value_stack.pop(), value_stack.pop()))

        operator_stack.append(input[x]);
        x += 1
while operator_stack != []:
    value_stack.append(evaluate_expression(operator_stack.pop(), value_stack.pop(), value_stack.pop()))
    
    
print value_stack
print operator_stack
print output