class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        def dfs(from_, target, val=0):
            if from_ == target:
                return val
            if from_ in visit or from_ not in mapping_table:
                return -1.0
            visit[from_] = True
            for to_, query_val in mapping_table[from_]:
                res_val = dfs(to_, target, val*query_val)
                if res_val != -1.0:
                    mapping_table[from_] = mapping_table.get(from_, []) + [[to_, res_val]]
                    mapping_table[to_] = mapping_table.get(to_, []) + [[from_, 1/res_val]]
                    return res_val
            return -1.0
        mapping_table = {}
        for idx, (from_, to_) in enumerate(equations):
            mapping_table[from_] = mapping_table.get(from_, []) + [[to_, values[idx]]]
            mapping_table[to_] = mapping_table.get(to_, []) + [[from_, 1/values[idx]]]
        
        res = []
        for from_, to_ in queries:
            visit = {}
            if from_ not in mapping_table:
                res += [-1.0]
            else:
                res += [dfs(from_, to_, val=1)]
        return res
                
                
            
        
        
        