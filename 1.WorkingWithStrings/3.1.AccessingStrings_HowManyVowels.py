# Problem:
'''
You need to make a program that counts the number of vowels in a given text.
The vowels are a, e, i, o, and u.

Take a string as input and output the number of vowels.

Sample Input:
this is great

Sample Output:
4

NOTE: There are 4 vowels in the given text.
'''
#--------------------------------------------#

# CODE:

text = input()

count = 0
for i in text:
    if i in ["a", "e", "i", "o","u"]:
        count += 1
print (count)