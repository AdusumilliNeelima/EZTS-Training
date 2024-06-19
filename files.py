import os
#To write to the file
with open ("neelima.txt",'w')as f:
    f.write("i am neelima")
    f.close()
#To read from file
with open("neelima.txt",'r')as f:
    s=f.read()  
    f.close()
    #To replace
s=s.replace("ballari","bitm")
with open ("neelima.txt",'w')as f:
    f.write(s)
    f.close()
    #To read at specific positions
with open("neelima.txt",'rb')as f:
    print(f.tell())
    f.seek(-35,2)
    print(f.read().decode('utf-8'))
    f.close()
with open("neelima.txt",'r+b')as f:
    print(f.tell())
     
    f.seek(-35,2)
    print(f.tell())
    f.write(b"#")
    print(f.read().decode('utf-8'))
    f.close()
# to delete
os.remove("neelima.txt")