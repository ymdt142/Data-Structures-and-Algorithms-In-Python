class MaxHeap():
    def __init__(self):
        self.heap=[0]
        self.size=0
    def insert(self,i):
        self.heap.append(i)
        self.size+=1
        self.heapifyUP(self.size)
    def heapifyUP(self,i):
        while i//2>0:
            if self.heap[i]>self.heap[i//2]:
                self.heap[i],self.heap[i//2]=self.heap[i//2],self.heap[i]
            i=i//2
    def delRoot(self):
        if(self.size>0):
            self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
            self.size -= 1
            self.heapifyDown(self.size)
    def heapifyDown(self,i):
        j=1
        mx=0
        while(j*2<i):
            if self.heap[j*2]<self.heap[j] and self.heap[j*2+1]<self.heap[j]:
                break
            if self.heap[j*2]>self.heap[j*2+1]:
                mx=j*2
            else:
                mx=j*2+1
            if self.heap[j]<self.heap[mx]:
                self.heap[j],self.heap[mx]=self.heap[mx],self.heap[j]
            j=mx
    def getvla(self):
        for i in range(1,self.size+1):
            print(self.heap[i],end=" ")
        print('')
mh=MaxHeap()
mh.insert(10)
mh.insert(20)
mh.insert(15)
mh.insert(30)
mh.insert(40)
mh.getvla()
mh.delRoot()
mh.getvla()



