r=int(raw_input())
count=0
if r>1:
    for i in range(2,r):
        if r%i==0:
            count=count+1
if count>1:
    print ("yes")
else:
    print ("no")
