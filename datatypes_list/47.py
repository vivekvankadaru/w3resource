'''
Write a Python program to insert an element before each element of a list

color = ['Red', 'Green', 'Black','Red', 'Green', 'Black','Red', 'Green', 'Black']

o/p
['c','Red','c', 'Green','c', 'Black','c','Red','c', 'Green','c', 'Black','c','Red','c', 'Green','c', 'Black']
'''
color = ['Red', 'Green', 'Black','Red', 'Green', 'Black','Red', 'Green', 'Black']
string_='c'
op=[]
for ele in color:
  op.append(string_)
  op.append(ele)
print(op)
'''
op=[]
color = ['Red', 'Green', 'Black','Red', 'Green', 'Black','Red', 'Green', 'Black']
for ele in color:
  for v in ('c',ele):
    op.append(v)
print(op)
'''