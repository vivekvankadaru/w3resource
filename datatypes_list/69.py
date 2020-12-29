'''
Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
'''

l=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
l_tuples=[tuple(x) for x in l]
l_set=set(l_tuples)
l_list=[list(x) for x in l_set]
print(l_list)

'''
   or
import itertools
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", num)
num.sort()
new_num = list(num for num,_ in itertools.groupby(num))
print("New List", new_num)

'''
