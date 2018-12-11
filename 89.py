def sort(values):
	for y range(len(values)):		
		for z in range(y,len(values)):			
			if (values[y] > values[z]):
				temp = values[y]
				values[y] = values[z]
				values[z] = temp
h= raw_input().rstrip()
yList = list(h)
sort(yList)
print "".join(yList)
