def count_substring(string, sub_string):
    count = 0
    start = 0
    while start < len(string):
        position = string.find(sub_string, start)
        if position != -1:
            count+=1
            start = position+1
        else:
            break
    return count
