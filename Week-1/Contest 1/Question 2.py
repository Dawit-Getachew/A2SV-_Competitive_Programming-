row = 4
for i in range(5):
	for k in range(i):
		print("*",end = " ")
	for k in range(2*(row - i)):
		print(" ",end = " ")
	for k in range(i):
		print("*",end = " ")
	print()