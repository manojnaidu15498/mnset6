n=int(input())
k=int(input())
l=list()
i=0
for i in range(n):
    x=int(input())
    l.append(x)
    i=i+1
if k in l:
    print('yes')
else:
    print('no')
