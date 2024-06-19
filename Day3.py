#prime
m=int(input("enter the number"))
flag=0
for i in range(2,(m//2)+1):
    if(m%i==0):
        flag=1
        break
if(m<0):
    flag=1
elif m==1:
    flag=0
if (flag==1):
    print("invalid")
else:
    print("valid")

# prime check prod of next prime number 

def check_prime(m):
    flag=0
    for i in range(2,(m//2)+1):
        if(m%i==0):
            flag=1
            break
    if(m<0):
        flag=1
    elif m==1:
        flag=0
    if (flag==1):
        return 0
    else:
        return 1

n=int(input("enter the value of n"))
flag=0
result=[]
k=n+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        result.append(k)
    else:
        k=k+1
sum=0
for i in range(n+1,k):
    sum+=i
result.append(sum)
p1=k
flag=0
k=p1+1
while flag< 1:
    flag=check_prime(k)
    if flag==1:
        p2=k
    else:
        k=k+1

p3=p1*p2
flag=check_prime(p3)
if flag==0:
    result.append(False)
else:
    result.append(True)
prime_key=tuple(result)
print(prime_key)

#diwali contest

cnt=0
time=0
p=int(input("Enter the minutes taken to reach the destination:"))
mins_rem=240-p
for i in range(mins_rem):
    prd=5*i
    time=time+prd
    if prd in range(mins_rem-time):
        cnt=cnt+1
print("Number of problems he can solve:",cnt)
