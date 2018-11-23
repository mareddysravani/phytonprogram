z=int(raw_input())
if z>0:
    for x in range(2,z):
        if(z%x)==0:
            print "no"
            break
    else:
        print "yes"
