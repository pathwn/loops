n=int(input("enter number"))
i=1
while i<=n:
    if i%2==0:
        print("+",i*i,end=" ")
    else:
        print("-",i*i,end=" ")
    i=i+1        