n=int(raw_input())
count=0
if n>0:
    for j in range(1,n+1):
        if n%j==0:
            print j,
