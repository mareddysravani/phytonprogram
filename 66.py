s=int(raw_input())
if s>0:
    for x in range(2,s):
        if(s%x)==0:
            print "no"
            break
    else:
        print "yes"
