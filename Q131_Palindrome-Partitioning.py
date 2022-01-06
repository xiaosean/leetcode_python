class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.palindrome_map={}
        def _partition_helper(s):
            for i in range(len(s)):
                l, r = i-1, i+1
                self.palindrome_map[s[i]] = True
                while r < len(s) and s[i] == s[r]:
                    pali_str = s[i:r+1]
                    self.palindrome_map[pali_str] = True
                    r += 1
                while l>=0 and r<len(s) and s[l] == s[r]:
                    pali_str = s[l:r+1]
                    self.palindrome_map[pali_str] = True
                    l -= 1
                    r += 1
        def get_all_subset(s, path=None, res=[]):
            if path is None:
                path = []
            elif not s:
                res += [path]
            for idx in range(len(s)):
                target = s[:idx+1]
                if target in self.palindrome_map:
                    get_all_subset(s[idx+1:], path+[target])
            
            return res
        
        _partition_helper(s)
        return get_all_subset(s)