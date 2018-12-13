import math
r,s=map(int,raw_input().split())
s=r * s
if math.sqrt(s).is_integer():
    print ("yes")
else:
    print ("no")
