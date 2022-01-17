if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    newArr= tuple(integer_list)
    print(hash(newArr))
