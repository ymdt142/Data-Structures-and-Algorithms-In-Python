class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList():
    def __init__(self):
        self.head=None
    def deleteLast(self):
        self.temp = self.head
        while self.temp.next!=None:
            self.pre=self.temp
            self.temp=self.temp.next
        self.pre.next=None
    def insertLast(self,data):
        self.newnode=Node(data)
        if self.head==None:
            self.head=self.newnode
            self.last=self.newnode
        else:
            self.last.next=self.newnode
            self.last=self.newnode
            self.newnode.next=self.head

    def traverse(self):
        self.temp = self.head
        i=10 #traverse 10 values from the circular linklist
        while(i):
            print(self.temp.data,end='->')
            self.temp=self.temp.next
            i-=1
l=LinkedList()
l.insertLast(5)
l.insertLast(4)
l.insertLast(3)
l.insertLast(2)
l.insertLast(1)
l.insertLast(0)
l.traverse()

