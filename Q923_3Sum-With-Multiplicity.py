class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        cnt = 0
        arr.sort()
        lr_table = {}
        for idx, num in enumerate(arr):
            if num not in lr_table:
                lr_table[num] = [idx, idx]
            else:
                lr_table[num][1] = idx
        for idx, num in enumerate(arr):
            l, r = idx-1, idx+1
            while l >= 0 and r < len(arr):
                sum_ = num + arr[l] + arr[r]
                if sum_ == target:
                    cnt += (l-lr_table[arr[l]][0]+1)*(lr_table[arr[r]][1]-r+1)
                    l = lr_table[arr[l]][0] - 1
                    r = lr_table[arr[r]][1] + 1
                elif sum_ > target:
                    l = lr_table[arr[l]][0] - 1
                else:
                    r = lr_table[arr[r]][1] + 1
        return cnt % (10**9+7)
                    
                    