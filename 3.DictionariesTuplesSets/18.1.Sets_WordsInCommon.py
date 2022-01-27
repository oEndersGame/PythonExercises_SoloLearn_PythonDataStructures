# Problem:
'''
Given two sentences, you need to find and output the number of the common words (words that are present in both sentences).

Sample Input:
this is some text
I would like this tea and some cookies

Sample Output:
2

The words 'some' and 'this' appear in both sentences.

NOTE: You can use the split() function to get a list of words in a string and then use the set() function to convert it
into a set. For example, to convert the list x to a set you can use: set(x)
'''
#--------------------------------------------#

# CODE:

# 1.Solution:
s1 = set(input().split())
s2 = set(input().split())

match = s1 & s2
print( len(match))

"""
# 2. and shorter Solution:
s1 = set(input().split())
s2 = set(input().split())

print( len(s2 & s1))
"""