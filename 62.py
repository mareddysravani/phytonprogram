p=raw_input()
"""if all(n in '12' for n in q):
    print "yes"
else:
    print ("no")
    """
if not(p.translate(None,'12')):
    print ("yes")
else:
    print 9"no")
