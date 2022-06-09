a=int(input("enter number"))
i=1
while i<=a//2:
    if a%2==0:
        print("it is not prime number")
        break
    i=i+1
else:
    print("it is prime number")    