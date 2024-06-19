#returning maximum vowel repetition
#Background: A group of friends embarks on a picnic and decides to engage in a friendly
#  competition during their journey. The game they choose involves each participant stating
#  a sentence about themselves. The objective is to have the sentence with the highest frequency
#  of any single vowel. In the event of a tie, the winner is determined by the alphabetical
#  precedence of the most frequent vowel.

# Objective: Develop a program that assists in determining the winner of the game by analysing 
# the sentences provided by each player. The program should accept a string input, which represents
#  the sentence spoken by a player, and output the most frequent vowel(s) in that sentence. 
# If multiple vowels tie for highest frequency, all such vowels should be printed in alphabetical
#  order.

# Requirements:
# •	The program must handle multiple sentences as input, one for each player.
# •	The output must clearly indicate the most frequent vowel(s) for each input sentence.
# •	In case of ties, vowels must be sorted alphabetically and displayed accordingly.

# Test cases:
# Input	Output
# [
#     ["Alex", "I enjoy hiking in the mountains."],
#     ["Sam", "A lovely sunny day at the beach."],
#     ["Jamie", "Reading a book is my favorite pastime."],
#     ["Taylor", "I love playing video games on weekends."],
#     ["Chris", "Exploring new cities is exciting and fun."]
# ]	{
# 'Alex': ['I'], 
# 'Sam': ['A'], 
# 'Jamie': ['A', 'I'], 
# 'Taylor': ['E'], 
# 'Chris': ['I']
# }


def count_vowel(s):
    dic={'A':0,'E':0,'I':0,'O':0,'U':0}
    for i in s:
        if i=='a' or i=='A':
            dic['A']=+1
        elif i=='e' or i=='E':
            dic['E']=+1
        elif i=='i' or i=='I':
            dic['I']=+1
        elif i=='o' or i=='O':
            dic['O']=+1
        elif i=='u' or i=='U':
            dic['U']=+1
    x=max(dic.values())
    result=[]
    for i,j in dic.items():
        if j==x:
            result.append(i)
    return result
i_p=[
    ["alex","i enjoy hiking in the mountains"],
    ["sam","i enjoy a holiday"],
    ["jamie",'reading a book is my favourite']
]
op={}
for i in op:
    op[i[0]]=count_vowel(i[1])
print(op)

#for fixed 

mxlst=[2,4,3,5,6,3,4,6,7,1,2,5]
mx=sum=0
for i in range(0,len(mxlst)-2):
    sum=mxlst[i]+mxlst[i+1]+mxlst[i+2]
    if sum > mx:
        mx=sum
        pos=i
print(max,mxlst[pos],mxlst[pos+1],mxlst[pos+2])

# for k digits 

mxlst=[2,4,3,5,6,3,4,6,7,1,2,5]
mx=sum=0
k=int(input("enter thr no of continous digit"))
for i in range(0,len(mxlst)-k+1):
    sum=0
    for j in range(0,k):
        sum+=mxlst[i+j]
    if sum > mx:
        mx=sum
        pos=i
    print(max)
for j in range(0,k):
    print(mxlst[pos+j])
#print(cnt+1)
#Scenario: Alex, an intrepid treasure hunter, is navigating through a labyrinth with seven checkpoints.
# At each checkpoint, there are multiple gates, each marked with a number representing the potential clues or challenges it holds. 
# Only one gate at each checkpoint leads to the next, and the correct gate is determined by an equilibrium condition: the sum of all 
# integers (clues/challenges) on its left must be equal to the sum of allintegers on its right. If no such gate exists, the middle gate 
# is deemed correct.

#  Objective: Develop a program that assists Alex in identifying the correct gates at each checkpoint to reach the final destination. 
#  The program should accept an array A of N integers, where each integer represents the number of clues or challenges associated with 
#  a gate and output the index of the equilibrium gate.
 
# Requirements: The program must process an array of integers as input for each checkpoint.
                # The output must clearly indicate the index of equilibrium gate.
                # If no equilibrium gate exists, the program should return the midpoint state.
def gate(lst):
    flag=False
    for i in range(len(lst)):
        ls=sum(lst[0:1])
        rs=sum(lst[i:])
        if ls==rs:
            flag=True
            eq_gate=i
            break
    if flag:
        return(eq_gate)
    else:
        if len(lst)%2==0:
            mid=len(lst)//2-1
        else:
            mid=len(lst)//2
        return(mid)
    
i_p=[
    [2,2,1,2,1],
    [4,2,3,1,2,1,2,3],
    [1,1,1,1,1],
    [3,0,3],
    [1,2,1,1,2,1],
    [1,1,1,2,1],
    [5,2,1,3,1,2,5] 
    ]

result={}
for i in i_p:
    st="checkpoint"+str(i_p.index(i)+1)
    result[st]=gate(i)
print(result)

#max sum array


# sample input: [2,4,3,5,6,3,4,6,7,1,2,5]
# output: [4,6,7]


def max_sum(k,lst):
    s=[]
    for i in range(len(lst)-(k-1)):
        s.append(sum(lst[i:(i+k)]))
    m=s.index(max(s))
    result=lst[m:m+k]
    return result
    
k=int(input())
#lst=list(map(int,input().split()))
lst=[2,4,3,5,6,3,4,6,7,1,2,5]
print(max_sum(k,lst))


#TYPE2


def max_sum(k,lst):
    m=0
    s=sum(lst[:k])
    for i in range(1,len(lst)-(k-1)):
        m=s-lst[i-1]+lst[i+k-1]
        if s<m:
            s=m
            pos=i
    result=lst[pos:pos+k]
    return result
    
k=int(input("Enter the number of continuous inputs:"))
#lst=list(map(int,input().split()))
lst=[2,4,3,5,6,3,4,6,7,1,2,5]
print(max_sum(k,lst))

#TYPE3
l=[2,4,3,5,6,3,4,6,7,1,2,5]
sum=max=0
k=int(input("Enter the no of continuous digit: "))
for i in range(0,len(l)-(k-1)):
    sum=0
    for j in range(0,k):
        sum=sum+l[i+j]
    if max<sum:
        max=sum
        pos=i
        
print(max)
for j in range(0,k):
    print(l[pos+j])

#sliding window
def max_sum(k,lst):
    window=max=0
    window=sum(lst[:k])  #WINDOW
    for i in range(1,len(lst)-(k-1)):
        if max<window:
            max=window
            pos=i
            window=window-lst[i-1]+lst[i+k-1]    #SLIDER
    result=lst[pos:pos+k]
    return result

k=int(input("Enter the number of continuous inputs: "))
#lst=list(map(int,input().split()))
lst=[2,3,4,5] #6,3,4,6,7,1,2,5
print(max_sum(k,lst))            

#matching cards

#You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are 
# matching if the cards have the same value.

# Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the 
# picked cards. If it is impossible to have matching cards, return -1

# Input: cards = [3,4,2,3,4,7] 
# Output: 4 
# Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. 
# Note that picking up the cards [4,2,3,4] is also optimal.   

card=list(map(int,input().split()))
min=999
f=False
for i in range(len(card)):
    s=0
    for j in range(i+1,len(card)):
        if card[i]==card[j]:
            s=j-i+1 
            if min>s:
                min=s
                f=True
if f:
    print(min)
else:
    print(-1)
# i/p:4 3 2 4 5 3
# o/p:4





