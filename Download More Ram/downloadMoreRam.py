for iter in range(int(input())):
	n,kGbRam = map(int,input().split())
	a = list(map(int,input().split()))
	b = list(map(int,input().split()))
	ramCol = [[a[i],b[i]] for i in range(n)]
	ramCol.sort()
	for neededRam,addedRam in ramCol:
		if neededRam>kGbRam:
			break
		kGbRam+=addedRam 
	print(kGbRam)
