'''
All of these check to see if two strings are anagramous (word?) of each other.

This is essentially a speed test, comparing multiple methods to solve the same 
thing.

'''

import time

def anagram_checkoff(s1, s2):
    '''
    This first solution converts both strings to lists and iterates through 
    them, letter by letter. This is an O(n^2) solution.
    '''

    start = time.time()

    alist = list(s2)

    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
            pos2 = 0
            found = False
            while pos2 < len(alist) and not found:
                if s1[pos1] == alist[pos2]:
                    found = True
                else:
                    pos2 = pos2 + 1
            
            if found:
                alist[pos2] = None
            else:
                still_ok = False

            pos1 = pos1 + 1

    end = time.time()

    return f'\nCheckoff method. anagram: {still_ok}. Time: {end-start} seconds \n'

def anagram_alphabetical(s1, s2):
    '''
    Method using an alphabetical sorting, followed by a comparison. This method
    Is a little faster and seems to scale better than the last one. It has
    the same Big-O (O(n^2)) as the last one, due to the expense required to 
    alphabetize the incoming lists, since those are methods in and of themeselves.
    '''

    start = time.time()

    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False

    end = time.time()

    return f'Alphabetize and sort method. Anagram: {matches}. Time: {end - start} \n'

def anagram_counting(s1, s2):
    '''
    Because the iterations aren't nested, we only have to iterate through each
    item in each listified strings once each. If the strings are of the same
    length, the computer performs 2n actions. Since we have to iterate through a
    single list of 26 characters once, this means that the equation is 
    T(n) = 2n + 26, which as n becomes large becomes O(n) steps. This is the most 
    efficient algorithm we've seen thus far.
    '''

    start = time.time()

    counter1 = [0]*26 #for every possible letter of the alphabet.
    counter2 = [0]*26 #for every possible letter of the alphabet.

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a') #ord of a is 97. So it keeps a counter for that char.
        counter1[pos] += 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        counter2[pos] += 1

    j = 0

    still_ok = True
    while j < 26 and still_ok:
        if counter1[j] == counter2[j]:
            j += 1
        else:
            still_ok = False

    end = time.time()
    
    return f'Character-counting method. Anagram: {still_ok}. Time: {end - start}, \n'


print(anagram_checkoff('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))
print(anagram_alphabetical('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))
print(anagram_counting('abcdefghijklmnopqrstuvwxyz', 'zyxwvutsrqponmlkjihgfedcba'))
