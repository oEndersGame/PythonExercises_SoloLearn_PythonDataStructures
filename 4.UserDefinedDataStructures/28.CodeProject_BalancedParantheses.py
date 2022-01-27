# Problem:
'''
Parentheses are balanced, if all opening parentheses have their corresponding closing parentheses.

Given an expression as input, we need to find out whether the parentheses are balanced or not.
For example, "(x+y)*(z-2*(6))" is balanced, while "7-(3(2*9))4) (1" is not balanced.

The problem can be solved using a stack.
Push each opening parenthesis to the stack and pop the last inserted opening parenthesis whenever a closing parenthesis is encountered.
If the closing bracket does not correspond to the opening bracket, then stop and say that the brackets are not balanced.
Also, after checking all the parentheses, we need to check the stack to be empty -- if it's not empty, then the parentheses are not balanced.

Implement the balanced() function to return True if the parentheses in the given expression are balanced, and False if not.

Sample Input:
(a( ) eee) )
Sample Output:
False

NOTE: You can use a simple list for a stack. Use list.insert(0, item) to push on the stack, and list.pop(0) to pop the
top item. You can access the top element of the stack using list[0].
'''
#--------------------------------------------#

# CODE:

class stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.insert(0,item)
    def pop(self):
        return self.items.pop(0)
    def __call__(self):
        return self.items

def balanced(expression):
    #your code goes here
    x = stack()
    for char in expression:
        if char == '(':
            x.push(char)
        if char == ')':
            if '(' in x():
                x.pop()
            else:
                return False
    if not x():
        return True
    return False

print(balanced(input()))