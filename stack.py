#!/usr/bin/python3

#define stack class
class Stack:
    #constructor function
    def __init__(self):
        self._stack = list()

    #add items
    def push(self, value):
        self._stack.append(value)

    #remove items
    def pop(self):
        try:
            self._stack[0]
        except:
            print("The stack is empty")
        else:
            print(self._stack.pop())
          