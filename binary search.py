a=[1,2,3,4,5,6,7,8,9]
l=0
search=1
h=len(a)-1
mid=(l+h)//2
found=0
while(l<=h):
    #print("low " + str(l) + " mid " + str(mid) + " high " + str(h))
    if(a[mid]==search):
        found=1
        break
    elif(search<a[mid]):
        h=mid-1
        mid=(l+h)//2
    else:
        l=mid+1
        mid=(l+h)//2
if(found==1):
    print("Found")
else:
    print("Not Found")