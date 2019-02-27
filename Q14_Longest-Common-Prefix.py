class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ""
        min_length = min([len(s) for s in strs])
        for i in range(min_length, 0, -1):
            same_prefix = strs[0][:i]
            if all([x.startswith(same_prefix) for x in strs]):
                return same_prefix
        return ""