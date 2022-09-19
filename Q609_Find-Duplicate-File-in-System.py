class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        seen_data = {}
        for path in paths:
            dir_, *packs = path.split(" ")
            for  file_and_data in packs:
                filename, data = file_and_data.split("(")
                seen_data[data] = seen_data.get(data, []) + ["/".join([dir_, filename])]
        res = []
        for _, filenames in seen_data.items():
            if len(filenames) > 1:
                res += [filenames]
        return res