r1,s1=[int(x) for x in raw_input().split(" ")]
r2,s2=[int(x) for x in raw_input().split(" ")]
timeDiffInMinutes=ads((r1*60+s1)-(r2*60+s2))
print str(timeDiffInMinutes/60)+" "+str(timeDiffInMinutes%60)
