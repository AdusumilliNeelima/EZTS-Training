#BODMAS parenthesis checker

class stcak:
  def _init_(self):
    self.itt=[]
  def push(self,data):
    self.itt.append(data)
  def pop(self):
    return self.itt.pop()
  def size(self):
    return len(self.itt)
# directly we can use OB="[({}".
#and CB="})]" and then use i in OB and use i in CB for the next condition. 
n=input("enter the expression:")
s=stcak()
flag=0
for i in n:
  if i=='(' or i=='[' or i=='{':
    s.push(i)
    print(f"pushed {i} onto the stack")
    
  if i==')' or i==']' or i=='}':
    x=s.pop()
      
    print(f"popped {i} out of the stack")
    if x=='(' and i==')':
      pass
    elif x=='[' and i==']':
      pass
    elif x=='{' and i=='}':
      pass
    else:
      flag=1
      break
  
if flag==0 and s.size()==0:
  print("valid expression")
else:
  print("invalid expression ")
#stack-factory
class stcak:
  def _init_(self):
    self.itt=[]
  def push(self,data):
    self.itt.append(data)
  def pop(self):
    return self.itt.pop()
  def size(self):
    return len(self.itt)
  def top(self):
    return self.itt[-1]
  
l=[3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
o=[0]*len(l)
s=stcak()
for i in range(len(l)-1,-1,-1):
  if s.size()!=0:
    while s.size()!=0 and s.top()<=l[i]:
      if s.top()<=l[i]:
        s.pop()
      
  if s.size()==0:
    o[i]=-1
  else:
    o[i]=s.top()
  s.push(l[i])
print(o)
 
#LINKED LIST
class LinkedList:
    def _init_(self,data):
        self.data=data
        self.next=None
class list:
    head=None
    tail=None
    size=0
    def insertf(self):
        data=int(input("enter the data: "))
        temp=LinkedList(data)
        if self.head==None:
            self.head=self.tail=temp
        else:
            temp.next=self.head
            self.head=temp
        self.size+=1

    def inserte(self):
        data=int(input("enter the data: "))
        temp=LinkedList(data)
        if self.head==None:
            self.head=self.tail=temp
        else:
            self.tail.next=temp
            self.tail=temp
        self.size+=1

    def display(self):
        if self.head==None:
            print("list is empthy")
        else:
            curr=self.head
            while curr!=None:
                print(curr.data)
                curr=curr.next

l=list()
l.insertf()
l.insertf()
l.inserte()
l.inserte()
l.display()
str=input()

class node:
    def __init__(self,data):
        self.value=data
        self.next=None
Head=tail=node(10)
#Head.next=node(20)
#Head.next.next=node(30)
tail.next=node(20)
tail=tail.next
tail.next=node(30)
tail=tail.next
tail.next=node(40)
tail=tail.next
def print_link_list(Head):
    if Head == None:
        print("empty list")
    curr=Head
    while curr!=None:
        print(curr.value)
        curr=curr.next
#insertion at front
def insert_frt(Head,data):
    new=node(data)
    if Head == None:
        Head=new
    else:
        new.next=Head
        Head=new
insert_frt(Head,60)
#insertion at end
temp=None
curr=None
def insert_end(head,data):
    new=node(data)
    if Head == None:
            Head=new
    else:
        while curr!=None:
            temp.next=None
            curr.next=temp
insert_end(Head,70)
print_link_list(Head)
#insertion inbetween
#delete at beginning
def dele_frt(Head):
    Head=Head.next
def dele_end(Head):
    curr.next.next=None
def dele_anywhr(prev,curr):
    prev.next=curr.next

# basic calci
op=['+','-','*','/']
for i in str:
    if i in op:
        x=i
        str=str.replace(i," ")
l=list(map(float,str.split(" ")))
match x:
    case"+":
        print(l[0]+l[1])
    case"-":
        print([0]-l[1])
    case"*":
         print(l[0]*l[1])
    case"/":
         print(l[0]-l[1])
    