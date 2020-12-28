'''
Write a Python program to generate a 3*4*6 3D array whose each element is *
'''

i=[]

for m in range(3):
  j=[]
  for n in range(4):
    k=[]
    for l in range(6):
      k.append('*')
    j.append(k)
  i.append(j)
print(i)

'''
   or
print([[['*' for x in range(6)] for col in range(4) ] for row in range(3)])