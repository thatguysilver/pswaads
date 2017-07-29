import sys
from stack import Stack

def base_converter(dec_num, base):

    digits = '012356789ABCDEF'
    
    remainder_stack = Stack()

    while dec_num > 0:
        remainder = dec_num % base
        remainder_stack.push(remainder)
        dec_num = dec_num // base

    new_string = ''
    while not remainder_stack.is_empty():
        new_string = new_string + digits[remainder_stack.pop()]

    return new_string

try: 
    if len(sys.argv) > 1: 
        print(base_converter(int(sys.argv[1]), int(sys.argv[2])))
    else:
        print('You need to type something.')
except ValueError:
    print('Not a base 10 integer, dipshit.')
    
#WAAAAY simpler than you'd expect.
