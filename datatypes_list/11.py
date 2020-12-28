'''
Write a Python function that takes two lists and returns True if they have at least one common member.
'''

l1=[1,2,3,4,5]
l2=[6,7,8,9,]

if set(l1)&set(l2):
    print('Have common element')
else:
    print('No common ele')