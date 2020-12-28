'''
Write a Python program to generate all permutations of a list in Python
'''

from itertools import permutations
l=[1,2,3,4]
for i in permutations(l,2):
    print(i)