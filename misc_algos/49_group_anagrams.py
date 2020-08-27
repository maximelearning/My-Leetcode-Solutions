# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for word in strs:
            key = "".join(sorted(word))
            dictionary[key] = dictionary.get(key, []) + [word]
        return dictionary.values()
