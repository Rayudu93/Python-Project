p=[7,1,5,3,6,4]
ans=0
minval=p[0]
for i in range(len(p)-1):
    minval=min(minval,p[i])
    if(p[i]>p[i+1]):
        temp=p[i]-minval
        ans+=temp
        minval=p[i+1]
    else:
        if i==len(p)-2:
            ans+=p[i+1]-minval
            minval=p[i+1]
print(ans)
