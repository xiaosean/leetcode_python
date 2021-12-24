class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # Define the graph
        graph = {}
        for course, must_course in prerequisites:
            graph[course] = graph.get(course, []) + [must_course]
        _traverse = [0] * numCourses
        self._res = []
        
        def traverse_course(course):
            if _traverse[course] == -1:
                return False
            if _traverse[course] == 1:
                return True
            _traverse[course] = -1

            for must_course in graph.get(course, []):
                success = traverse_course(must_course)
                if not success:
                    return False
            _traverse[course] = 1
            self._res += [course]
            return True
        if all([traverse_course(x) for x in range(numCourses)]):
            return self._res
        return []
        