a="aaaAAAbcdefaa"
d={}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
aa=''
for i in a:
    if i not in aa:
        aa+=i+str(d[i])
print(aa)