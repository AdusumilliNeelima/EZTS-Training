#bubble sort

l=list(map(int,input().split()))
n=len(l)
for j in range(0,n):
    for i in range(0,n-1-j):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)

#selection sort

l=[9,7,5,8,10,26,44,3,1]
n=len(l)
pos=0
for j in range(0,n):
    pos=j
    min=l[j]
    for i in range(j,n):
        if l[i]<min:
            min=l[i]
            pos=i
        l[j],l[pos]=l[pos],l[j]
print(l)
#quick sort
def divide(l,low,high):
    p=l[high]
    pi=high
    j=low-1
    for i in range(low,high):
        if l[i]<=p:
            j+=1
            l[i],l[j]=l[j],l[i]
    j+=1
    l[j],l[pi]=l[pi],l[j]
    pi=j
    return pi
def quick_sort(l,low,high):
    if low<high:
        pi=divide(l,low,high)
        print(pi,low,high)
        quick_sort(l,low,pi-1)
        quick_sort(l,pi+1,high)
    return 
if __name__=="__main__":
    l=list(map(int,input().split()))
    low=0
    high=len(l)-1
    print(low,high)
    quick_sort(l,0,len(l)-1)
    print("sorted array",l)

#merge sort
def merge(left,right):
    i=j=0
    temp=[]

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            temp.append(left[i])
            i+=1
        else:
            temp.append(right[j])
            j+=1
            
    while i<len(left):
        temp.append(left[i])
        i+=1
        
    while j<len(right):
        temp.append(right[j])
        j+=1

    return temp

def mergesort(L):
    if len(L) <= 1:
        return L
        
    mid = len(L)//2
    left=L[:mid] 
    right=L[mid:]
    
    left_sorted = mergesort(left)
    right_sorted = mergesort(right)
    
    return merge(left_sorted,right_sorted)


if __name__=="__main__":
    L=list(map(int,input().split())) # 4 7 8 3 2 9 1 5
    sorted=mergesort(L)

    print("Sorted Array = ",sorted)