
binary=input("enter number")
decimai=0
p=1
while binary!=0:
    rev=binary%10
    binary=binary//10
    decimal=decimal+rev*p
    p=p*2
print(decimal)    