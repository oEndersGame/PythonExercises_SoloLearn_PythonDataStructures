# Problem:
'''
You need to make a back button for a browser.
You use a stack to store the website links visited. Each new link visited is pushed onto the stack.
The back button needs to pop the top link from the stack and navigate to it.

The given code declares a Browser class as a stack and implements some of its methods. Then, some links are pushed onto the stack.
A while loop is then used to go back to all links and print them.

Implement the required pop() method for the Browser, so that the given code works as expected.

NOTE: Note, that the pop() method needs to return the value, so that it can be printed.
'''
#--------------------------------------------#

# CODE:

class Browser:
    def __init__(self):
        self.links = []

    def is_empty(self):
        return self.links == []

    def push(self, link):
        self.links.insert(0, link)

    def pop(self):
        return self.links.pop(0)

    def printStack(self):
        return self.links

x = Browser()
x.push('about:blank')
x.push('www.sololearn.com')
x.push('www.sololearn.com/courses/')
x.push('www.sololearn.com/courses/python/')

while not x.is_empty():
    print(x.pop())