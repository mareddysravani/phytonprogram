import math
def sort(values):
  for r in range(len(values)):
    for s in range(r,len(values)):
      if(values[r]>values[s]):
        temp=values[r]
        values[s]=temp
n=int(raw_input())
values=[int(x) for x in raw_input().split("")
sort(values)
medianIndex=int(math.floor(len(values)/2))
print(values[medianIndex])
