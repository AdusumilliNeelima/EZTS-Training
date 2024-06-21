#AVL tree

class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        self.height=1
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

def insert(root,sky):
    if not root:
        return node(sky)
    if sky<root.value:
        root.left=insert(root.left,sky)
    else:
        root.right=insert(root.right,sky)

    root.height=1+ max(ght(root.left),ght(root.right))
    
    BF=getBF(root)

    #rr rotation
    if BF>1 and sky<root.left.value:
        return rightrotate(root)
    #rl rotation
    if BF>1 and sky>root.left.value:
        root.left=leftrotate(root.left)
        return rightrotate(root)
    #ll rotation
    if BF<-1 and sky>root.right.value:
        return leftrotate(root)
    #lr rotation
    if BF<-1 and sky<root.right.value:
        root.right=rightrotate(root.right)
        return leftrotate(root)
    return root
def ght(root):
    if not root:
        return 0
    return root.height
def getBF(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)   
def leftrotate(A):
    B=A.right
    temp=B.left
    B.left=A
    A.right=temp
    A.height=1+ max(ght(A.left),ght(B.right))
    B.height=1+ max(ght(B.left),ght(A.right))
    getBF(A)
    getBF(B)

    return B 
def rightrotate(A):
    B=A.left
    temp=B.right
    B.right=A
    A.left=temp
    A.height=1+ max(ght(A.left),ght(B.right))
    B.height=1+ max(ght(B.left),ght(A.right))
    getBF(A)
    getBF(B)
    return B

if __name__=="__main__":
    root=None
    vl=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    for i in vl:
        root=insert(root,i)
    inorder(root)
# calculate the maximum number of commas used when printing the integers from 1 to 100,000 assume that each number is printed with the appropriate thousands separator

#in a array find the smallest positive integer
arr=[5,2,-3,-4,-5,7,8]
minn=[]
for i in arr:
    if i>0:
        minn.append(i)
print(minn)
min=minn[0]
for i in minn:
    if i<min:
        min=i
print(min)
#leetcode problem 41(type-1)
def func(lst):
    if 1 not in lst:
        return 1
    else:
        for i in range(1,12):
            if i not in lst:
                return i
                break
lst=[1,2,0]
maxi=max(lst)
#print(maxi)
print(func(lst))










