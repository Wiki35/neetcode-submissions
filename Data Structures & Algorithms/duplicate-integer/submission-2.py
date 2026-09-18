# time O(n logn), space O(1) or O(n)

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for x in range(1, len(nums)):
            if nums[x] == nums[x-1]:
                return True
        return False