p=[7,1,5,3,6,4]
ans=0
for i in range(len(p)-1):
    for j in range(i+1,len(p)):
        temp=p[i]-p[j]
        ans=max(ans,temp)
print(ans)