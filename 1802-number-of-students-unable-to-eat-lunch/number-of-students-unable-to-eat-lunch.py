from collections import deque

class Solution:
    def countStudents(self, students, sandwiches):
        students = deque(students)
        sandwiches = deque(sandwiches)

        count = 0  # tracks rotations without progress

        while students and count < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0
            else:
                students.append(students.popleft())
                count += 1

        return len(students)
