class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Space complexity O(amount)
        # Time complexity O(amount * the number of coins)
        # bfs strategy from zero to amount
    
        if amount == 0:
            return 0
        traverse_map = [False] * (amount + 1)
        queue, next_queue = [0], []
        cnt = 0
        while queue:
            cnt += 1
            for num in queue:
                if traverse_map[num]:
                    continue
                traverse_map[num] = True
                for coin in coins:
                    next_num = num + coin
                    if next_num == amount:
                        return cnt
                    elif next_num < amount:
                        next_queue += [next_num]
            queue, next_queue = next_queue, []
        return -1
        # Pseudo
        # queue = [0]
        # cnt = 0
        # while queue:
        #   cnt += 1
        #   for num in queue
        #       for each coins:
        #           next_pos = num + coin
        #           if next_pos == amount:
        #               return cnt
        #           push the next position for next round queue
        #   queue, next_queue = next_queue, []
        # No possible solutino
        # return -1