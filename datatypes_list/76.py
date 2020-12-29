'''
Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters.
Original list:
[1, 1, 2, 3, 4, 4, 5, 1]
List reflecting the modified run-length encoding from the said list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Original String:
aabcddddadnss
List reflecting the modified run-length encoding from the said string:
[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]
'''

from itertools import groupby
l=[1, 1, 2, 3, 4, 4, 5, 1]
l='aabcddddadnss'
l_grouped=[[len(list(group)),key] for key,group in groupby(l)]
print(l_grouped)
final=[]
for ele in l_grouped:
	if ele[0]==1:
	   final.append(ele[1])
	else:
	   final.append(ele)
print(final)