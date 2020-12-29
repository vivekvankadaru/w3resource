'''
Write a Python program to convert a pair of values into a sorted unique array

L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]

Sorted Unique Data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
'''

l = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]

s={x[0] for x in l}|{x[1] for x in l}
print(sorted(s))
