#maximum count including if max count is repeated
l=[1,2,3,2,3,1,2,1,1,1,2,2,3,3,3,4,4,3,2,1,1]
d={}
m=[]
for i in l:
    if i not in m:
        m.append(i)
        d[i]=l.count(i)
maxi=[]
print(d)
maxvalue=max(d.values())
#print(ele)
for i in d:
    if d[i]==maxvalue:
        maxi.append(i)

if len(maxi)>1:
    print(-1)
    print(maxi)
else:
    print(maxi.pop())