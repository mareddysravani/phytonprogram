c= raw_input().rstrip()
evenB = oddB = ''
for p, s in enumerate(c):
	if p & 1 == 0:
		evenB += s
	else:
		oddB += s

print(evenB + " " + oddB)
