p=raw_input()
"""if all(n in '01' for n in q):
    print "yes"
else:
    print "no"
    """
if not(p.translate(None,'01')):
    print "yes"
else:
    print "no"
