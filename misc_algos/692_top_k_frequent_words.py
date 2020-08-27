# https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_to_freq = {}
        for word in sorted(words):
            word_to_freq[word] = word_to_freq.get(word, 0) + 1
        words = sorted(word_to_freq.keys(),
                       key=lambda key: word_to_freq[key], reverse=True)
        return words[:k]
