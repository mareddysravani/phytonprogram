y,z=map(int,raw_input().split())
if(y>z):
    min=y
else:
    min=z
while(1):
    if(min%y==0 and min%z==0):
        print(min)
        break
    min=min+1
