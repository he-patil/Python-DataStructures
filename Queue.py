from collections import deque
from Stack import *
import queue

class Queue():
    def __init__(self, initial=None):
        if initial == None:
            self.container = deque()
        else:
            self.container = deque(reverse(initial))
        
    def size(self):
        return len(self.container)
    
    def isEmpty(self):
        return self.size()<=0

    def enque(self, value):
        self.container.appendleft(value)
        return str(value) + "Inserted!"

    def deque(self):
        if not self.isEmpty():
            return self.container.pop()

    def front(self):
        if not self.isEmpty():
            return self.container[-1]

def printBinary(limit):
    q = Queue("1")
    
    for i in range(limit):
        front = q.deque()
        print(front)
        q.enque(front+"0")
        q.enque(front+"1")
        
def main():
    printBinary(15)

    string = "i love my country"
    #str1 = ""

    q = Queue(string)
    print(q.container)

    q.enque("a")
    print(q.container)

    print(q.front())
    print(q.deque())
    print(q.container)

    print(q.isEmpty())
    print(q.size())

if __name__ == "__main__":
    main()


#### OUTPUT ####
# 1
# 10
# 11
# 100
# 101
# 110
# 111
# 1000
# 1001
# 1010
# 1011
# 1100
# 1101
# 1110
# 1111
# deque(['y', 'r', 't', 'n', 'u', 'o', 'c', ' ', 'y', 'm', ' ', 'e', 'v', 'o', 'l', ' ', 'i'])
# deque(['a', 'y', 'r', 't', 'n', 'u', 'o', 'c', ' ', 'y', 'm', ' ', 'e', 'v', 'o', 'l', ' ', 'i'])
# i
# i
# deque(['a', 'y', 'r', 't', 'n', 'u', 'o', 'c', ' ', 'y', 'm', ' ', 'e', 'v', 'o', 'l', ' '])
# False
# 17