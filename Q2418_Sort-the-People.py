class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = sorted(zip(names, heights), key=lambda x:x[1], reverse=True)
        return [person[0] for person in people]