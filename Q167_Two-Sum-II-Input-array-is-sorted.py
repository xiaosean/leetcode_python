class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        last_num = None
        for i in range(n):
            num1 = numbers[i]
            if num1 != last_num:
                for j in range(i+1, n):
                    num2 = numbers[j]
                    sum_ = num1 + num2
                    if sum_ == target:
                        return [i+1, j+1]
                    elif sum_ > target:
                        break
            last_num = num1