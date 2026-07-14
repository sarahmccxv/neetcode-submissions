class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        histogram = defaultdict(int)
        for num in nums:
            histogram[num] += 1
        
        max_frequency = len(nums)

        bucketed_frequency = [[] for _ in range(max_frequency + 1)]
        for num, frequency in histogram.items():
            bucketed_frequency[frequency].append(num)
        
        result = []
        for i in range(max_frequency, -1, -1):
            numbers = bucketed_frequency[i]
            for number in numbers:
                result.append(number)
                if len(result) == k:
                    return result
