class Solution:
    def histogram_tuple(self, s: str) -> tuple[int]:
        histogram = [0] * 26

        for char in s:
            index = ord(char) - ord('a')
            histogram[index] += 1
        
        return tuple(histogram)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)

        for s in strs:
            key = self.histogram_tuple(s)
            anagram_groups[key].append(s)
        
        return list(anagram_groups.values())

