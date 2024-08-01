class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0
        for data in details:
            age = int(data[11:13])
            if age > 60:
                cnt += 1
        return cnt