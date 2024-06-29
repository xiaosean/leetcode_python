class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # DFS-solution
        child_nodes = defaultdict(list)
        ancestors = [[] for _ in range(n)]

        for parent, child in edges:
            child_nodes[parent] += [child]
        
        def dfs(parent, current_node):
            for node in child_nodes[current_node]:
                if ancestors[node] and parent == ancestors[node][-1]:
                    continue
                ancestors[node] += [parent]
                dfs(parent, node)
        for i in range(n):
            dfs(i, i)
        return ancestors
