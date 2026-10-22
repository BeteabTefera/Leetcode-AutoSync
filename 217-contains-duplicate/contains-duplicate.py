class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        #edge case
        if nums == []:
            return False
        # solution 1
        nums.sort() # in place sorting

        for i in range(len(nums) - 1):
            if nums[i] == nums [i+1]:
                return True        
        return False