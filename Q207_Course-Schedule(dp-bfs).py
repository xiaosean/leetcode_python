from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dp = [0] * numCourses
        for course, pre_course in prerequisites:
            dp[course] += 1
        # bfs
        q = deque([idx for idx, x in enumerate(dp) if x == 0])
        while q:
            idx = q.popleft()
            for course_idx in range(len(prerequisites)-1, -1, -1):
                course, pre_course = prerequisites[course_idx]
                if idx == pre_course:
                    dp[course] -= 1
                    if dp[course] == 0:
                        q.append(course)
                    del prerequisites[course_idx]
        return not any(dp)