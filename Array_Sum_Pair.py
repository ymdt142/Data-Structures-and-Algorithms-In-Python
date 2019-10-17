class ArraySum():
    def print_pair(self,a,b):
        c=0
        d={}
        self.ll=[]
        for l in a:
            target=b-l
            if target in a:
                if str(target) not in d:
                    if str(l) not in d:
                        d[str(target)] = 1
                        d[str(l)] = 1
                        self.ll.append((target, l))
                        c += 1
    def test(self):
        return self.ll
        print(c)

a=ArraySum()
a.print_pair([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1],10)
print(a.test())
a.print_pair([1,2,3,1],3)
print(a.test())
a.print_pair([1,3,2,2],4)
print(a.test())
a.print_pair([2,2,2,2],4)
print(a.test())