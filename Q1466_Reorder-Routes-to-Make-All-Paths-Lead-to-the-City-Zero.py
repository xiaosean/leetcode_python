class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # bfs solution
        # Create adjancy matrix
        # start from location {0} and traverse the path
        # if no path:
        #   flip the city path

        mat = {}
        visit = [0] * n
        for from_, to_ in connections:
            mat[from_] = mat.get(from_, []) + [(to_, False)]
            mat[to_] = mat.get(to_, []) + [(from_, True)]
        cnt = 0
        cur, nex = [0], []
        while cur:
            for node in cur:
                if visit[node]:
                    continue
                visit[node] = True 
                for near_node, arrive in mat[node]:
                    nex += [near_node]
                    if not arrive and not visit[near_node]:
                        cnt += 1
            cur, nex = set(nex), []
        return cnt                
                    