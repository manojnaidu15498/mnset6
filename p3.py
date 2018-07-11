n=int(input())
sum=0
while(n>0):
    z=n%10
    sum=sum+z
    n=n//10
print(sum)
