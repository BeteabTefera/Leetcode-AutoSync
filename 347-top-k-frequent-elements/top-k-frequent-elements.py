class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 1 or len(nums) == k:
            return nums

        dic = {}
        for i in nums:  # O(N) frequency counting without .count()
            dic[i] = dic.get(i, 0) + 1

        # Sort the numbers (keys) based on their frequencies (values) in descending order
        maxitems = sorted(dic.keys(), key=lambda x: dic[x], reverse=True)

        return maxitems[:k]