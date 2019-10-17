a='aaaAABBACDEffaa'
r=''
i=1
cnt=1
while(i<len(a)):
    if a[i-1]==a[i]:
        cnt+=1
    else:
        r=r+a[i-1]+str(cnt)
        cnt=1
    i+=1
r=r+a[i-1]+str(cnt)
print(r)