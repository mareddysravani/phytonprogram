ss=raw_input()
b=len(ss)
r=list(ss)
if b%2==0:
    m=b/2 - 1
    r[m]='*'
    a[m+1]='*'
else:
    m=b/2 - 1
    r[m+1]='*'
print "".join(r)
