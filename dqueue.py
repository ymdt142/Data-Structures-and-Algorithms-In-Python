class Dqueue():
    def __init__(self):
        self.item=[]
    def isEmpty(self):
        return(self.item==[])
    def size(self):
        return(len(self.item))
    def addFront(self,ele):
        self.item.append(ele)
    def addRear(self,ele):
        self.item.insert(0,ele)
    def delFront(self):
        return self.item.pop()
    def delRear(self):
        return self.item.pop(0)
dq=Dqueue()
print(dq.isEmpty())
print(dq.size())
dq.addFront(5)
dq.addFront(4)
dq.addFront(3)
dq.addRear(2)
dq.addRear(1)
dq.addRear(0)
print(dq.item )
print(dq.delFront())
print(dq.item)
print(dq.delFront())
print(dq.item)
print(dq.delRear())
print(dq.item)
print(dq.delRear())
print(dq.item)
