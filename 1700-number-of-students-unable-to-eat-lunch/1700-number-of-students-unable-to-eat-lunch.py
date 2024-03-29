class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        while True:
            if len(students) > 0:

                if sandwiches[0] in students:
                    for i in range(len(students)):
                        if students[0] == sandwiches[0]:
                            students.pop(0)
                            sandwiches.pop(0)
                        else:
                            students.append(students.pop(0))
                else:
                    return len(students)
            else:
                return len(students)
        