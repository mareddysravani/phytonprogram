def isIsogram(b):
	charMap = {}
	for r in s:
		if r in charMap:
			return False
		else:
			charMap[r] = 1
	return True
s= raw_input().rstrip()
print("Yes" if isIsogram(b) else "No")
