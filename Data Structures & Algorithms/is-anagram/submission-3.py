class Solution:
    def histogram(self, s: str) -> List[str]:
        histogram = [0] * 26
        
        for char in s:
            index = ord(char) - ord('a')
            histogram[index] += 1
        
        return histogram

    def isAnagram(self, s: str, t: str) -> bool:
        return self.histogram(s) == self.histogram(t)