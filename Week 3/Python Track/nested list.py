if __name__ == '__main__':
    student={}
    for _ in range(int(input())):
            name = input()
            grade = float(input())
            student[name]= grade;
    stud = list(sorted(set(student.values())))
    names=[]
    for i,j in student.items():
        if j==stud[1]:
            names.append(i)
    names.sort()
    for i in names:
        print(i)
            
