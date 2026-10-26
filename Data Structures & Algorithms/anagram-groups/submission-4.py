class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # edge case of having a list mapping charCount to List
        for s in strs:
            count = [0] * 26 # a......z
            for c in s:
                count[ord(c) - ord('a')] += 1 #a=80 | 80-80 = 0 mapping to a -> 1
            res[tuple(count)].append(s)
        res = list(res.values())
        return res