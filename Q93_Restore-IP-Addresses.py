class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if s == "":
            return []
        
        def dfs(nums, path=None, result=[]):
            if path is None:
                path = []
            if len(path) == 4: 
                if not nums:
                    result += [path]
                return
            for i in range(min(len(nums), 3)):
                num = nums[:i+1]
                int_num = int(num)
                if int_num > 255 or (i>0 and num[0]=="0"):
                    continue
                dfs(nums[i+1:], path + [num], result)
            return result
        
        addrs = dfs(s)
        return [".".join(addr) for addr in addrs]