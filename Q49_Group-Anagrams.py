class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        set_dict = {}
        set_list = []
        for s in strs:
            sort_s = list(s)
            sort_s.sort()
            set_s = str("".join(sort_s))
            set_dict[set_s] = set_dict.get(set_s, []) + [s]
            set_list += [set_s]


        r_list = []
        set_list = list(set(set_list))
        for s in set_list:
            r_list += [[str_ for str_ in set_dict[s]]]
        return r_list