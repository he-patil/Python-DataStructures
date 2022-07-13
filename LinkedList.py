
from asyncio.windows_events import NULL


class Node():
    def __init__(self, data=None,next=NULL):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = NULL
        self.length = 0

    def previousIndex(self, index):
        counter=1

        if self.length<1  or index > self.length or index==0:
            return NULL

        itr = self.head
        while counter<index:
            itr = itr.next
            counter+=1
        
        return itr

    def previousOfValue(self, data):
        counter=1
        itr = self.head

        while itr and itr.data != data :
            itr = itr.next
            counter+=1

        return counter

    def printList(self):
        itr = self.head
        while itr:
            print(itr.data,"-->",end=" ")
            itr = itr.next
        print("null")


    def insertAtIndex(self,index,data):
        if index > self.length:
            return "Index out of bound"

        if index==0:
            newNode = Node(data,self.head)
            self.head = newNode
            self.length+=1
            return str(data)+" inserted at index "+str(index)

        tempNode = self.previousIndex(index)
        newNode = Node(data,tempNode.next)
        tempNode.next = newNode
        self.length+=1
        return str(data)+" inserted at index "+str(index)

    def insertAtBeginning(self, data):
        return self.insertAtIndex(0, data)

    def removeFromIndex(self,index):
        if index>=self.length:
            return "Index out of bound"

        if index==0:
            data = self.head.data
            self.head = self.head.next
            self.length-=1
            return str(data)+" removed from index "+ str(index)
        
        tempNode = self.previousIndex(index)
        data = tempNode.next.data
        tempNode.next = tempNode.next.next
        self.length-=1
        return str(data)+" removed from index "+ str(index)
    
    def removeFromBeginning(self):
        return self.removeFromIndex(0)

    def insertAfterValue(self, dataAfter, dataInsert):
        index = self.previousOfValue(dataAfter)
        print("Inserting after ",dataAfter)
        if index == self.length+1:
            return "Data not found"
        return self.insertAtIndex(index,dataInsert)

    def removeValue(self,data):
        index = self.previousOfValue(data)
        print("Deleting ",data)
        if index == self.length+1:
            return "Data not found"
        return self.removeFromIndex(index-1)

if __name__=="__main__":

    linkedList = LinkedList()
    linkedList.printList()

    print()
    print(linkedList.insertAtIndex(0,2))
    linkedList.printList()
    
    print()
    print(linkedList.insertAtBeginning(6))
    linkedList.printList()

    print()
    print(linkedList.insertAtIndex(1,8))
    linkedList.printList()
    
    print()
    print(linkedList.insertAtIndex(0,9))
    linkedList.printList()

    print()
    print(linkedList.insertAtIndex(3,15))
    linkedList.printList()

    print()
    print(linkedList.insertAtIndex(4,20))
    linkedList.printList()

    print()
    print(linkedList.insertAtIndex(6,30))
    linkedList.printList()

    print()
    print(linkedList.insertAtIndex(8,40))
    linkedList.printList()

    print()
    print(linkedList.removeFromBeginning())
    linkedList.printList()

    print()
    print(linkedList.removeFromIndex(3))
    linkedList.printList()

    print(linkedList.removeFromIndex(4))
    linkedList.printList()

    print()
    print(linkedList.removeFromIndex(4))
    linkedList.printList()

    print()
    print(linkedList.insertAfterValue(6,20))
    linkedList.printList()

    print()
    print(linkedList.insertAfterValue(2,50))
    linkedList.printList()

    print()
    print(linkedList.insertAfterValue(9,20))
    linkedList.printList()

    print()
    print(linkedList.removeValue(6))
    linkedList.printList()

    print()
    print(linkedList.removeValue(50))
    linkedList.printList()

    print()
    print(linkedList.removeValue(15))
    linkedList.printList()

    print()
    print(linkedList.removeValue(40))
    linkedList.printList()




#### OUTPUT ####
# null

# 2 inserted at index 0
# 2 --> null

# 6 inserted at index 0
# 6 --> 2 --> null

# 8 inserted at index 1
# 6 --> 8 --> 2 --> null

# 9 inserted at index 0
# 9 --> 6 --> 8 --> 2 --> null

# 15 inserted at index 3
# 9 --> 6 --> 8 --> 15 --> 2 --> null

# 20 inserted at index 4
# 9 --> 6 --> 8 --> 15 --> 20 --> 2 --> null

# 30 inserted at index 6
# 9 --> 6 --> 8 --> 15 --> 20 --> 2 --> 30 --> null

# Index out of bound
# 9 --> 6 --> 8 --> 15 --> 20 --> 2 --> 30 --> null

# 9 removed from index 0
# 6 --> 8 --> 15 --> 20 --> 2 --> 30 --> null

# 20 removed from index 3
# 6 --> 8 --> 15 --> 2 --> 30 --> null
# 30 removed from index 4
# 6 --> 8 --> 15 --> 2 --> null

# Index out of bound
# 6 --> 8 --> 15 --> 2 --> null

# Inserting after  6
# 20 inserted at index 1
# 6 --> 20 --> 8 --> 15 --> 2 --> null

# Inserting after  2
# 50 inserted at index 5
# 6 --> 20 --> 8 --> 15 --> 2 --> 50 --> null

# Inserting after  9
# Data not found
# 6 --> 20 --> 8 --> 15 --> 2 --> 50 --> null

# Deleting  6
# 6 removed from index 0
# 20 --> 8 --> 15 --> 2 --> 50 --> null

# Deleting  50
# 50 removed from index 4
# 20 --> 8 --> 15 --> 2 --> null

# Deleting  15
# 15 removed from index 2
# 20 --> 8 --> 2 --> null

# Deleting  40
# Data not found
# 20 --> 8 --> 2 --> null