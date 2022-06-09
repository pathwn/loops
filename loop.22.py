a=int(input("enter number"))
rev=0
temp=a
while temp>0:
    rem=temp%10
    rev=rev*10+rev
    temp=temp//10
    if (a==rev):
        print("palindrom number")
    else:
        print("not palindrom number")    