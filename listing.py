'''
Trying to learn about the different list concatenation methods in py
and examine their efficiency.
'''

import time

def iterate_concat():

    start = time.time()
    new_list = []
    for i in range(1000):
        new_list += [i]
    end = time.time()
    return f'Regular iteration took {end - start} seconds.'

def append_concat():

    start = time.time()
    new_list = []
    for i in range(1000):
        new_list.append(i)

    end = time.time()

    return f'Append method took {end - start} seconds.'

def list_comp_concat():
    start = time.time()
    new_list = [i for i in range(1000)]
    end = time.time()
    
    return f'Using a list comprehension took {end - start} seconds.'

def make_list():
    start = time.time()
    new_list = list(range(1000))
    end = time.time()

    return f'Creating a list from a range took {end - start} seconds.'

print(iterate_concat())
print(append_concat()) 
print(list_comp_concat()) 
print(make_list())

