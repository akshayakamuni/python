a=input("Enter a number")
a=int(a)
sum=0
while a>0:
    q=a%10
    sum=sum*10+q
    a=a//10
print(sum)
