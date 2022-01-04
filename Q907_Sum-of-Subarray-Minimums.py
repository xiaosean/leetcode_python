class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:        
        arr = [0] + arr # make sure append one value keep the stack is not empty
        n = len(arr)
        stack = [0]
        res = [0]*n
        for i in range(n):
            while arr[i] < arr[stack[-1]]:
                stack.pop()
            last_min_idx = stack[-1]
            stack += [i]
            # similar dp idea and add current to last_min_idx diff value
            res[i] = res[last_min_idx] + (i-last_min_idx)*arr[i]
        return sum(res) % (10**9 + 7)
                