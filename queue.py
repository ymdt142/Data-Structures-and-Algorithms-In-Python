class Queue():
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return(self.item==[])
    def size(self):
        return(len(self.item))
    def enqueue(self,ele):
        self.item.insert(0,ele)
    def dequeue(self):
         return self.item.pop()
q=Queue()
print(q.size())
print(q.isEmpty())
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)
q.enqueue(2)
print(q.item)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.item)

