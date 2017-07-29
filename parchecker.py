#In which Y.T. learns how to evaluate parantheses.

import sys
from stack import Stack

def matches(open, close):
    opens = '([{'
    closers = ')]}'
    return opens.index(open) == closers.index(close)


def par_checker(string):
    s = Stack()                            
    balanced = True                        
    index = 0

    while index < len(string) and balanced:
        symbol = string[index]             
        
        if symbol in '([{':
            s.push(symbol)
        elif symbol not in '([{' and symbol not in ')]}':
            return 'non-paranthetical character detected'
        else:
            if  s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index += 1

    if balanced and s.is_empty():
        return True
    else:
        return False


if len(sys.argv) > 1:
    print(par_checker(sys.argv[1]))
else:
    print('You need to put something in.')

#Basically, the way this works, if there is anything left on the end of the 
#string by the time the program ends, we get False. Note that this does not
