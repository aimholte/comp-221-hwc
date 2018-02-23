# A.J. Imholte
# Comp 221
# HWC

import itertools

# The solution to this problem is the permutation (4, 0, 7, 2, 9, 5, 1, 3, 6, 8) where the letters are mapped to the values
# as follows: {'r': 4, 'u': 0, 'b': 7, 'e': 2, 's': 9, 'i': 5, 'a': 1, 'z': 3, 'k': 6, 'n': 8}
# (This can be found by running this Python file as well)

'''
Given the words "Rubeus" and "Sirius", finds what permutation of numbers results in the word "Azkaban".
'''
def alphameticSolver(string1 = 'rubeus', string2 = 'sirius'):
    dict = {'r':0, 'u':0, 'b':0, 'e':0, 's': 0, 'i':0, 'a':0, 'z':0, 'k':0, 'n':0} # dictionary holding all unique letters
    answer = ()
    allPermutations = list(itertools.permutations(range(10))) # A list of all the possible permutations for this problem
    for permutation in allPermutations: # Assign the values from a permutation to its letter
        dict['r'] = permutation[0]
        dict['u'] = permutation[1]
        dict['b'] = permutation[2]
        dict['e'] = permutation[3]
        dict['s'] = permutation[4]
        dict['i'] = permutation[5]
        dict['a'] = permutation[6]
        dict['z'] = permutation[7]
        dict['k'] = permutation[8]
        dict['n'] = permutation[9]
        if((dict.get('r') * 100000 + dict.get('u') * 10000 + dict.get('b') * 1000 + 100 * dict.get('e') + 10* dict.get('u')
           + dict.get('s') + dict.get('s') * 100000 + dict.get('i') * 10000 + dict.get('r') * 1000 + dict.get('i') * 100 + dict.get('u') * 10 + dict.get('s'))
               == (dict.get('a') * 1000000 + dict.get('z') * 100000 + dict.get('k') * 10000 + dict.get('a') * 1000 +
           dict.get('b') * 100 + dict.get('a') * 10 + dict.get('n'))):
            # This if statement is pretty ugly, but all it is doing is checking to see if the assigned values for the first word
            # and the second word results in a sum that would spell the desired word, "Azkaban".
            answer = permutation
            print(answer)
            print(dict)
print(alphameticSolver())

