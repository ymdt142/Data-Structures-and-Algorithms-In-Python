#this is kandes alogorithm
a=[1,2,-1,3,4,10,10,-10,-1]
max_sub_array=a[0]
current=a[0]
for i in a[1:]:
    if i>(current+i):
        current=i
    else:
        current+=i
    if current>max_sub_array:
        max_sub_array=current
print(max_sub_array)
