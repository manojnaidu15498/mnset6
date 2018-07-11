s=input()
y=0
z=0
for x in s:
	if x.isdigit():
		y=1
	if x.isalpha():
		z=1
if(y==1)and (z==1):
	print("Yes")
else:
    print("No")
