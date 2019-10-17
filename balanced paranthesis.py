class Balanced_Paranthesis():
    def __init__(self,a):
        self.l=[]
        self.m=-1
        if(len(a)%2!=0):
            print(False)
        else:
            print(self.check(a))
    def push(self,s):
        self.l.append(s)
        self.m+=1
    def pop(self):
        del self.l[self.m]
        self.m-=1
        if(len(self.l)>0):
            return self.l[self.m]
        else:
            return 0
    def check(self,a):
        self.current=''
        for i in range(len(a)):
            if a[0]==")" or a[0]=="}" or a[0]=="]":
                return False
            if a[i]=="(" or a[i]=="{" or a[i]=="[":
                self.push(a[i])
                self.current=a[i]
            elif self.current=="(":
                if a[i]==")":
                    self.current=self.pop()
                else:
                     return False
            elif self.current=="{":
                if a[i]=="}":
                    self.current = self.pop()
                else:
                     return False
            elif self.current=="[":
                if a[i]=="]":
                    self.current = self.pop()
                else:
                     return False
        if(len(self.l)==0):
            return True
        else:
            return False
b=Balanced_Paranthesis("[](){([[[]]])}(")
b=Balanced_Paranthesis("[{{{(())}}}]((()))")
b=Balanced_Paranthesis("[[[]])]")



