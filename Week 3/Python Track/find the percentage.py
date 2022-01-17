if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split(" ")
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum=0
    map(lambda x: sum+x, student_marks[query_name])
    for x in student_marks[query_name]:
        sum+=x
    average = sum/3
    print("{:.2f}".format(average))
