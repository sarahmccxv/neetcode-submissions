class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        histogram = {}

        for char in s:
            histogram[char] = histogram.get(char, 0) + 1
        
        for char in t:
            if char not in histogram or histogram[char] == 0:
                return False
            
            histogram[char] = histogram[char] - 1
        
        return True