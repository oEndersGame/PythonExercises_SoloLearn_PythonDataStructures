# Problem:
'''
You are making a program to analyze text.
Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.

Sample Input:
hello
l
Sample Output:
40

The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40.

NOTE: Division result is a float. Use the int() function to convert the result to an integer.
'''
#--------------------------------------------#

# CODE:

inp1 = input()
inp2 = input()

a = inp1.count(inp2)

outp = int(a / len(inp1)* 100)

print(outp)
