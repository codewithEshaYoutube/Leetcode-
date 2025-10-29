
class Solution:
    def countStudents(self, students, sandwiches):
        count_0=students.count(0)
        count_1=students.count(1)

        for s in sandwiches:
            if s==0:
                if count_0==0:
                    return count_1
                count_0-=1
            else:
                if count_1==0:
                    return count_0
                count_1-=1
        return 0

