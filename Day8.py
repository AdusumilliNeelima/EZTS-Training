#graph traversal-DFS
'''s=[]
A={1:[(1,2,0),(1,3,0)],2:[(2,1,0),(2,7,0)],3:[(3,1,0),(3,5,0),(3,6,0)],4:[(4,7,0),(4,8,0)],5:[(5,3,0),(5,7,0)],6:[(6,3,0),(6,8,0)],7:[(7,2,0),(7,4,0),(7,5,0)],8:[(8,4,0),(8,6,0)]}
v={1:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False}
def dfs(A,v,s,e):
    if v[e]==False:
        s.append(e)
        v[e]=True
    else:
        return
    for i in A[e]:
        dfs(A,v,s,i[1])
    print(s.pop())
dfs(A,v,s,1)'''

#BFS
'''
Q=[]
G={1:[(1,2,0),(1,3,0)],2:[(2,1,0),(2,7,0)],3:[(3,1,0),(3,5,0),(3,6,0)],4:[(4,7,0),(4,8,0)],5:[(5,3,0),(5,7,0)],6:[(6,3,0),(6,8,0)],7:[(7,2,0),(7,4,0),(7,5,0)],8:[(8,4,0),(8,6,0)]}
def BFS(G,E):
    Q=[E]
    v={}
    for i in G.keys():
        v[i]=False
    v[E]=True
    while len(Q)!=0:
        curr=Q.pop(0)
        print(curr)
        for i in G[curr]:
            if v[i[1]]==False:
                Q.append(i[1])
                v[i[1]]=True
BFS(G,1)'''

#BINARY SEARCH TREE
lst=[4,6,7,3,8,2,5,9,1]
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
root=node(lst[0])
def insertion_bst(value,root):
    if root==None:
        root=node(value)
    if root.value>value:
        root.left=insertion_bst(value,root.left)
    if root.value<value:
        root.right=insertion_bst(value,root.right)
    return root
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)
for i in lst:
    insertion_bst(i,root)
inorder(root)







