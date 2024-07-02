#memoization 
#travelling sales 
def cost(curr,visited,G,dp):
    n=len(G)
    if len(visited)==n:
        return G[curr][0]
    visit=tuple(visited)
    if(curr,visit) in dp:
        return dp[(curr,visit)]
    min_cost=float('inf')
    for i in range(n):
        if i not in visited:
            new_visit=visited+[i]
            new_cost=G[curr][i]+ cost(i,new_visit,G,dp)
            min_cost=min(min_cost,new_cost)
    dp[(curr,visit)]=min_cost
    return min_cost

G=[
    [0,4,7,5,5],
    [4,0,2,3,8],
    [7,2,0,3,4],
    [5,3,3,0,6],
    [5,8,4,6,0]
]
dp={}
n=len(G)
print("minimum cost=",cost(0,[0],G,dp))