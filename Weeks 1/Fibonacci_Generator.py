n=int(input("Enter the limit:"))
a=0
b=1
cnt=0
while cnt<n:
    print(a)
    c=a+b
    a=b
    b=c
    cnt+=1