class Solution:

    def __init__(self, nums: List[int]):
        self.origin_list = nums.copy()
        self.nums = nums
        # self.random_list = itertools.permutations(self.origin_list)

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.origin_list.copy()
        return self.nums


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        random.shuffle(self.nums)
        # print("random.shuffle(self.origin_list) = ", random.shuffle(self.origin_list))
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()