from stack import Stack

#I'm having trouble parsing this (mentally), so Imma comment everythng.

def infix_to_postfix(infix_expr):
    prec = {}           #First, we gotta make an empty dictionary.
    prec['*'] = 3       #Now, we set entries. All of these  are  
    prec['/'] = 3       #signs that indicate our level of precedence
    prec['+'] = 2       #for each operator. Note that '(' is of lowest
    prec['-'] = 2       #precedence.
    prec['('] = 1
    op_stack = Stack()
    postfix_list = []                  #Creates a list of postfix
    token_list = infix_expr.split()    #split around ' ', so we must seperate everyting by spaces.

    for token in token_list:           #Iterates through our newly-created list
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postfix_list.append(token) #Adds to the stack if it's a char
            
        elif token == '(':
            op_stack.push(token)       #Adds to stack if it's a left paranthesis.
        
        elif token == ')':             
            
            top_token = op_stack.pop()        #Removes the ')' and assigns it to top-token

            while top_token != '(':           #
                
                postfix_list.append(top_token)
                top_token = op_stack.pop()

        else:                                 #For our operators.
            while (not op_stack.is_empty()) and \
                    (prec[op_stack.peek()] >= prec[token]): 
                        postfix_list.append(op_stack.pop())
            op_stack.push(token) 
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())   #Adds the completed op_stack to postfix_list.

    return ' '.join(postfix_list)             #Creates string from postfix_list.

print(infix_to_postfix('A * B + C * D'))
print(infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )')) 
print(infix_to_postfix('1 + 3 * 5 / ( 6 - 4 )'))


'''
Why push? Why append?
append is a list operator, while we wrote 'push' to work specifically n any object.
So sometimes it's appropriate to use push / append.
'''
