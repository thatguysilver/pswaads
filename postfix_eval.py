import sys
from  stack import Stack

def do_math(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 + op2

def postfix_eval(postfix_expr):

    operand_stack = Stack()

    token_list = postfix_expr.split()

    for token in token_list:
        if token in '1234567890':
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

try:
    if sys.argv > 1:
        print(postfix_eval(' '.join(sys.argv[1:])))
    else:
        print("Not a string, dipshit")
except IndexError:
    print('''
    Formatted incorrectly. It needs to be only single-digit integers and 
    operators with all spaces between them.
    ''')
