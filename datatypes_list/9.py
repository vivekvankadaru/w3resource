'''
Write a Python program to clone or copy a list.
'''

from copy import deepcopy
l=[1,2,3,4,5,6]
l1=deepcopy(l)
l[2]='a'
print(l1)