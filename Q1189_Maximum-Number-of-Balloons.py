class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text = text.lower()
        balloon_key = ["b", "a", "l", "o", "n"]
        balloon_counts = dict(zip(balloon_key, [0]*len(balloon_key)))
        # print(balloon_counts)
        for char in text:
            if char in balloon_key:
                balloon_counts[char] += 1
        for mutiply_char in ["l", "o"]:
            balloon_counts[mutiply_char] = balloon_counts[mutiply_char] // 2
        # print(balloon_counts)
        return min(balloon_counts.values())