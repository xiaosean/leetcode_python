class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        bins_list = [1]*2**k
        for i in range(k, len(s)+1):
            bin_s = s[i-k:i]
            num = int(bin_s, 2)
            bins_list[num] = 0
        return not any(bins_list)