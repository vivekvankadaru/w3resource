'''
Write a Python program to pack consecutive duplicates of a given list elements into sublists
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After packing consecutive duplicates of the said list elements into sublists:
[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]
'''

l=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
from itertools import groupby
s=[list(group) for key,group in groupby(l)]
print(s)