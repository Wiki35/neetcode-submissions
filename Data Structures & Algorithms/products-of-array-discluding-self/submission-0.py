# time O(n), space O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        output = []
        count_zero = nums.count(0)

        if count_zero == 0:
            for x in nums:
                result *= x
            for y in nums:
                output.append(result//y)
            return output
        elif count_zero == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    result *= nums[i]
                else:
                    zero_idx = i
            output = [0 for _ in range(len(nums))]
            output[zero_idx] = result
            return output
        else:
            return [0 for _ in range(len(nums))]