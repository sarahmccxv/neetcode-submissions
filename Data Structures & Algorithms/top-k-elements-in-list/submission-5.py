class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_frequency = defaultdict(int)
        for num in nums:
            num_to_frequency[num] += 1
        
        n = len(nums)
        frequency_to_nums = [[] for _ in range(n + 1)]

        for num, frequency in num_to_frequency.items():
            frequency_to_nums[frequency].append(num)
        
        result = []
        for i in range(n, -1, -1):
            nums = frequency_to_nums[i]
            for num in nums:
                result.append(num)
                if len(result) == k:
                    return result