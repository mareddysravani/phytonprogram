c,d=map(int,raw_input().split())
def gcd(r,p):
    s=abs(r-p)
    if (r-p)==0:
        return s
    else:
        return gcd(s,min(r,p))
print gcd(r,p)
