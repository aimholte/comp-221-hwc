# A.J. Imholte
# Comp 221
# HWC

import itertools


def alphameticSolver(string1 = 'rubeus', string2 = 'sirius'):
    dict = {'r':0, 'u':0, 'b':0, 'e':0, 's': 0, 'i':0, 'a':0, 'z':0, 'k':0, 'n':0}
    answer = ()
    allPermutations = list(itertools.permutations(range(10)))
    for permutation in allPermutations:
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
            answer = permutation
            print(answer)
            print(dict)
print(alphameticSolver())

