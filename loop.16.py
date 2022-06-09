var=int(input("enter number"))
rev=0
i=0
while var>0:
    b=var%10
    rev=rev*10+b
    var=var//10
    i=i+1
print(rev)    