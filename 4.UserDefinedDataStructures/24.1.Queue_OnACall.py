# Problem:
'''
You are making a call center application, which should handle customers in a queue.
The CallCenter class is implemented as a Queue. Each element of the queue has the topic of the call as its value. The two possible values are 'general' and 'technical'. A 'general' call takes on average 5 minutes to handle, while a 'technical' call requires 10 minutes.
The given code adds multiple customers to the Queue from user input.
You need to dequeue all added customers, calculate and output the total time required to handle all calls.

NOTE: Use a while loop to dequeue all the customers from the queue, until it is empty.
'''
#--------------------------------------------#

# CODE:

class CallCenter:
    def __init__(self):
      self.customers = []

    def is_empty(self):
      return self.customers == []

    def add(self, x):
      self.customers.insert(0, x)

    def next(self):
      return self.customers.pop()


c = CallCenter()

while True:
    n = input()
    if n == 'end':
        break
    c.add(n)

#your code goes here
tiempo_total = 0
while not c.is_empty():
  if c.next() == "general":
    tiempo_total += 5
  else: tiempo_total += 10
print(tiempo_total)