def insertionSort1(n, arr):
    i = n-1
    val = arr[i]
    while(i>0 and val<arr[i-1]):
        arr[i] = arr[i-1]
        print(*arr)
        i-=1
    arr[i] = val
    print(*arr)
    