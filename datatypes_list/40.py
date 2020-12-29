'''
Write a Python program to split a list based on first character of word.
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
Sample Output
a                                                                                                             
ask                                                                                                           
b                                                                                                             
be                                                                                                            
c                                                                                                             
call                                                                                                          
come                                                                                                          
d                                                                                                             
do        
-----
w                                                                                                             
want                                                                                                          
work
'''
'''
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
letter_list=set([s[0] for s in word_list])
d={}
for letter in letter_list:
   print(letter)
   for ele in word_list:
     if letter==ele[0]:
        print(ele)


                      or
'''
from itertools import groupby
from operator import itemgetter
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
for key,groups in groupby(sorted(word_list),lambda x:x[0]):
   print(key)
   for group in groups:
    print(group)
