from collections import deque
from inspect import stack
from operator import contains
from tkinter import TRUE

class Stack():
    def __init__(self,initial=None):
        if initial == None:
            self.container = deque()
        else:
            self.container = deque(initial)
    
    def size(self):
        return len(self.container)
    
    def isEmpty(self):
        return self.size()<=0

    def push(self, value):
        self.container.append(value)
        return str(value) + "Inserted!"

    def pop(self):
        if not self.isEmpty():
            return self.container.pop()

    def peek(self):
        if not self.isEmpty():
            return self.container[-1]

     
def reverse(string):
    result = ""
    tempStack = Stack(string)
    
    while not tempStack.isEmpty():
        result += tempStack.pop()

    return result

def reverseWords(string):
    split = string.split()

    result = ""
    for string in split:
        result += reverse(string)
        result += " "
    
    return result
    
if __name__ == "__main__":

    string = "i love my country"
    #str1 = ""

    print(reverse(string))
    print(reverseWords(string))



#### OUTPUT ####
# yrtnuoc ym evol i
# i evol ym yrtnuoc
