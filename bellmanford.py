#bellmanford algo,dynamic programming
graph=[
    [0,6,4,5,False,False],
    [False,0,False,False,-1,False],
    [False,-2,0,False,3,False],
    [False,False,-2,0,False,-1],
    [False,False,False,False,0,3],
    [False,False,False,False,False,0]
]
d={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',}
E_L=[]
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j]!=False and graph[i]!=0:
            E_L.append(tuple((i,j)))
print(E_L)
dist={}
for i in range(len(graph)):
    dist[i]=float('inf')
dist[0]=0
print(dist)
for i in range(len(graph)-1):
    for j in E_L: 
        new_dist=dist[j[0]]+graph[j[0]][j[1]]
        if dist[j[1]]>new_dist:
            dist[j[1]]=new_dist
print(dist)


