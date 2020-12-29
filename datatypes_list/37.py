'''
Write a Python program to find common items from two lists.
'''

color1 = ["Red", "Green", "Orange", "White","White"]
color2 = ["Black", "Green", "White", "Pink","White"]
common=[]
for i in color1:
    if i in color2:
      common.append(i) 
      color2.remove(i)
print(common)

