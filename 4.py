num1 = int(raw_input()) 
num2 = int(raw_input()) 
num3 = int(raw_input()) 

if (num1 > num2) and (num1 > num3):
 biggest = num1
elif (num2 > num1) and (num2 > num3):
 biggest = num2
else:
 biggest = num3
print(biggest)
