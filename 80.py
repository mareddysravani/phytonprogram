r=int(raw_input())
s=[]
while r!=0:
    d=r%10
    if d%2==1:
        s.append(d)
    r=r/10
print str(s[::-1]).replace('[',"").replace(']',"")
