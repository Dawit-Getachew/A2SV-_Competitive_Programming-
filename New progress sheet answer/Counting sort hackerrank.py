def countingSort(arr):
    # Write your code here
    newArr=[0]*100
    for i in arr:
        newArr[i]+=1
    return newArr