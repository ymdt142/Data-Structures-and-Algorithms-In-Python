class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
    def indertlast(self,data):
        node=Node(data)
        if(self.head==None):
            self.head=node
            self.last=node
        else:
            self.last.next=node
            self.last=node
    def traverse(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
    def reverse(self):
        self.current=self.head
        self.before=self.head
        self.next=self.head
        while(self.current!=None):
            self.next=self.current.next
            self.current.next=self.before
            self.before=self.current
            self.current=self.next
        self.t=self.head
        self.head=self.before
        self.t.next=None
l=LinkedList()
l.indertlast(1)
l.indertlast(2)
l.indertlast(3)
l.indertlast(4)
l.indertlast(5)
l.traverse()
l.reverse()
l.traverse()

