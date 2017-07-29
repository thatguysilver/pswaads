#measureing the difference between pop() and pop(0).$a

import timeit

popzero = timeit.Timer('x.pop(0)', 'from __main__ import x')
popend = timeit.Timer('x.pop()', 'from  __main__ import x')

for i in range(1000000, 1000000000, 1000000000000):
    x = list(range(i))
    pt = popend.timeit(number = 1000)
    
    x = list(range(i))
    pz = popzero.timeit(number = 1000)
    
    print(f'{pz}, {pt}')

print('genuinely not sure what dude is trying to show here. Also, this program is not working properly.')
