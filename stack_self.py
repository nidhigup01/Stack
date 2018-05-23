# -*- coding: utf-8 -*-
"""
Created on Mon May 21 17:50:45 2018

@author: nidhi
# learned from udacity lessons and 
https://gist.github.com/adarsh0806/02d8e1d54d510294e75dfbc0d9bd7059
"""

class Element():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, head= None):
        self.head = head
        
    def insert_first(self, new_element):
        if self.head == None:
            self.head = new_element
        elif self.head:
            new_element.next = self.head
            self.head = new_element
        print('the element {} is inserted'.format(new_element.value))
   
    
#    def delete_first(self):
#        deleted = self.head
#        if self.head:
#            self.head = self.head.next
#            deleted.next = None
#            return deleted
    def delete_first(self):
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element.value
        else:
            return None
    
class Stack():
    def __init__ (self, top = None):
        self.ll = LinkedList(top)
    def push(self, new_element):
        self.ll.insert_first(new_element)
    def pop(self):
        return self.ll.delete_first()
        
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print ('satack.pop', stack.pop())
print (stack.pop())
print (stack.pop())
print (stack.pop())
stack.push(e4)
print (stack.pop())
        
