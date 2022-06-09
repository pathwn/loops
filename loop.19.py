num=int(input("enter number"))
temp=num
sum=0
digit=0
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
    if num==sum:
        print("num armstrong number")
    else:
        print("num not armstrong")    