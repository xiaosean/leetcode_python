class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        idx = 0
        remaining = 0
        while idx < len(data):
            num = data[idx]
            num_bin = bin(num)[2:].zfill(8)
            idx += 1
            if not remaining:
                if num_bin.startswith("0"):
                    continue
                elif num_bin.startswith("110"):
                    remaining = 1
                elif num_bin.startswith("1110"):
                    remaining = 2
                elif num_bin.startswith("11110"):
                    remaining = 3
                else: 
                    return False
            else:
                if not num_bin.startswith("10"):
                    return False
                remaining -= 1
        return remaining==0