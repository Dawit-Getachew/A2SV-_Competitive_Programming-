class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        Flag = True
        while Flag:
            move = 0
            for i in range(len(students)):
                if students:
                    if students[0] == sandwiches[0]:
                        students.pop(0)
                        sandwiches.pop(0)
                        move += 1
                    else:
                        temp = students.pop(0)
                        students.append(temp)
            if move == 0:
                Flag = False
        return len(students)
                