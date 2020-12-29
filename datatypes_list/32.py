'''
Write a Python program to check whether a list contains a sublist
'''

l1=[1,2,3,4,5]
l2=[6,7,8,9,1,3,2,4]
print((set(l2)&set(l1)).issubset(set(l1)))