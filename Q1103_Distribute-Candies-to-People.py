class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        candy_list = [0] * num_people
        step = 0
        while candies > 0:
            candy_list[step % num_people] += min(step+1, candies)
            candies -= step + 1
            step += 1        
        return candy_list
        