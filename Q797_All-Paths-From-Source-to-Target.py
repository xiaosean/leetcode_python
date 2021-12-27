class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        n = len(graph)
        def dfs(start, target, path=None, res=[]):
            if path is None:
                path = []
            if start == target:
                res += [path + [target]]
                return res
            for node in graph[start]:
                dfs(node, target, path=path+[start])
            return res
        return dfs(0, n-1)