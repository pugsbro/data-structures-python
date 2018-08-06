class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.headval = None

    def printlist(self):
        printnode = self.headval
        while (printnode!=None):
            print(printnode.dataval)
            printnode = printnode.next

    def append(self, newdata):
        #add to end of list 
        newnode = Node(newdata)

        if self.headval == None:
            self.headval = newnode
            return
        
        last = self.headval
        while (last.next):
            last = last.next

        last.next = newnode

    def start(self, newdata):
        #add to beginning of list 
        newnode = Node(newdata)
        newnode.next = self.headval
        self.headval = newnode

    def after(self, node, newdata):
        newnode = Node(newdata)
        newnode.next = node.next
        node.next = newnode
        
    def remove(self,removekey):
        Head = self.headval

        if Head != None:
            if Head.dataval == removekey:
                self.headval = Head.next 
                return 
        
        while Head!=None:
            if Head.next.dataval == removekey:
                break
            Head = Head.next
        
        Head.next = Head.next.next 
       

    def size(self):

        count = 0
        countNode = self.headval        
        while(countNode!=None):
            countNode = countNode.next
            count = count + 1

        print count 
