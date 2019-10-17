class Queue():
    def __init__(self):
        self.l=[]
        self.ll=[]
        self.m=-1
        self.mm=-1
        self.p=0
    def push(self,e):
        self.l.append(e)
        self.m+=1
    def pop(self):
        self.a=self.ll[self.mm]
        del self.ll[self.mm]
        self.mm-=1
        del self.l[0]
        return self.a
    def swap(self):
        for i in range(self.m,-1,-1):
            self.ll.append(self.l[i])
            self.mm+= 1
    def enqueue(self,ele):
        self.push(ele)
    def dequeue(self):
        if(self.ll==[]):
            self.swap()
            print("Pooped "+str(self.pop()))
        else:
            print("Pooped " + str(self.pop()))
q=Queue()
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
q.enqueue(1)
print(q.l)
q.dequeue()
print(q.l)
q.dequeue()
q.dequeue()
print(q.l)
