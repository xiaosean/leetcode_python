class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # union find
        parents = {i: i for i in range(len(accounts))}
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            parents[find(x)] = find(y)            
        
        owner = {}
        for i, (name, *mails) in enumerate(accounts):
            for mail in mails:
                if mail in owner:
                    owner[mail] = union(owner[mail], i)    
                owner[mail] = i 
        res = defaultdict(list)
        for mail, owner_id in owner.items():
            res[find(owner_id)] += [mail]
        return [[accounts[k][0]]+sorted(res[k]) for k in res]