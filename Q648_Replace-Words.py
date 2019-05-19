class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        r_s = []
        for word in sentence.split():
            r_s += [word]
            for key in dict:
                if word.startswith(key):
                    r_s.pop() 
                    r_s += [key]
                    break
        return " ".join(r_s)