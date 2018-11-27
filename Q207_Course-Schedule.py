class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        prereq_table = {}
        def conflict_check(stack, prereq_list):
            if len(prereq_list) == 0:
                return False

            for prereq in prereq_list:
                if prereq in stack or conflict_check(stack+[prereq], prereq_table.get(prereq, [])):
                    return True
#                 next time we don't check again
                prereq_table[prereq] = []
            return False
#       record each course link
        for pre, course in prerequisites:
            prereq_table[course] = prereq_table.get(course, []) + [pre]

        for i in range(numCourses):
            if conflict_check([], prereq_table.get(i, [])):
                return False
        return True
