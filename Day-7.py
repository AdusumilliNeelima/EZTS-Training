class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def preorder(root):
    if root==None:
        return
    print(root.value)
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
print("pre")
preorder(root)
print("post")
postorder(root)
print("in")
inorder(root)

#levelorder
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def levelorder(root):
    Q=[root]
    Q.append(None)
    while len(Q)>0:
        curr=Q.pop(0)
        if curr==None:
            if len(Q)==0:
                break
            else:
                print()
                Q.append(None)
        else:
            print(curr.value,end=" ")
            if curr.left!=None:
                Q.append(curr.left)
            if curr.right!=None:
                Q.append(curr.right)
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
    root.left.right.left=node(9)
    root.left.right.right=node(10)
    root.right.right.right=node(11)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)
levelorder(root)

#height of a tree

class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def height(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    return max(lh,rh)+1
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
    root.left.right.left=node(9)
    root.left.right.right=node(10)
    root.right.right.right=node(11)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)
    print(height(root))

#to print only leafnodes

class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def preorder(root):
    if root==None:
        return
    #print(root.value)
    preorder(root.left)
    preorder(root.right)
    if root.left==None and root.right==None:
        print(root.value)
def leafnode(root):
    if root==None:
        return 0
    preorder(root.left)
    preorder(root.right)
    if root.left==None and root.right==None:
        print(root.value)
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
    root.left.right.left=node(9)
    root.left.right.right=node(10)
    root.right.right.right=node(11)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)
preorder(root)
#top view
class node:
     def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
class node_data:
    def __init__(self,Node,Hkey):
        self.node=Node
        self.hkey=Hkey

def topview(root):
  temp=node_data(root,0)
  Q=[temp]
  Q.append(None)
  key_dict={}
  
  while len(Q)!=0:
    curr=Q.pop(0)
    if curr==None:
      if len(Q)==0:
        break
      else:
        Q.append(None)
    else:
      if curr.hkey not in key_dict.keys():
        key_dict[curr.hkey]=curr.node.value
      
      if curr.node.left!=None:
        temp=node_data(curr.node.left,curr.hkey-1)
        Q.append(temp)
      if curr.node.right!=None:
        temp=node_data(curr.node.right,curr.hkey+1)
        Q.append(temp)
  for i in sorted(key_dict):
    print(key_dict[i])
  print(key_dict) 
if __name__=='main_':
  root=node(1)
  root.left=node(2)
  root.right=node(3)
  
  root.left.left=node(4)
  root.left.right=node(5)
  
  root.right.left=node(6)
  root.right.right=node(7)
  root.left.right.left=node(9)
  root.left.right.right=node(10)
  root.right.right.right=node(11)
  root.left.right.left.left=node(12)
  root.left.right.left.right=node(13)
  levelorder(root)
  print("\n",height(root))
  print("TOPVIEW")
  topview(root)
#bottomview
class node:
     def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
class node_data:
    def __init__(self,Node,Hkey):
        self.node=Node
        self.hkey=Hkey
def bottomview(root):
    temp=node_data(root,0)
    q=[temp]
    q.append(None)
    key_dict={}
    while len(q)!=0:
        curr=q.pop(0)
        if curr==None:
            if len(q)==0:
                break
            else:
                q.append(None)
        else:
                key_dict[curr.hkey]=curr.node.value
        if curr.node.left!=None:
                temp=node_data(curr.node.left,curr.hkey-1)
                q.append(temp)
        if curr.node.right!=None:
                temp=node_data(curr.node.left,curr.hkey+1)
                q.append(temp)
    for i in sorted(key_dict):
        print(key_dict[i])
    print(key_dict)
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
    root.left.right.left=node(9)
    root.left.right.right=node(10)
    root.right.right.right=node(11)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)
    bottomview(root)

class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def leftview(root):
    Q=[root]
    Q.append(None)
    while len(Q)>0:
        curr=Q.pop(0)
        if curr==None:
            if len(Q)==0:
                break
            else:
                print(Q[0].value)
                Q.append(None)
        else:
            print(curr.value,end=" ")
            if curr.left!=None:
                Q.append(curr.left)
            if curr.right!=None:
                Q.append(curr.right)
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)
    root.left.left=node(4)
    root.left.right=node(5)
    root.right.left=node(6)
    root.right.right=node(7)
    root.left.right.left=node(9)
    root.left.right.right=node(10)
    root.right.right.right=node(11)
    root.left.right.left.left=node(12)
    root.left.right.left.right=node(13)
leftview(root)


        
                







