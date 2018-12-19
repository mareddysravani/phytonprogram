x=int(raw_input())
r1=1
r2=1
i=2
if x<=0:
  print("positive number")
elif x==1:
  print 1,
else:
  print r1,
  print r2,
  while i<x:
      r3=r1+r2
      print r3,
      r1=r2
      r2=r3
      i=i+1
