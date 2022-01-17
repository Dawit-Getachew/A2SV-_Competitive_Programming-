if __name__ == '__main__':
    n = int(input())
    arr =set(map(int, input().split()))
    abe=sorted(set(arr))
    print(abe[len(arr)-2])
        
