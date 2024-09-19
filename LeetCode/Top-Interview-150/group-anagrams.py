class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = {}

        for string in strs:
            sorted_str = ''.join(sorted(string))

            if sorted_str not in anagram_map:
                anagram_map[sorted_str] = []

            anagram_map[sorted_str].append(string)

        return list(anagram_map.values())
