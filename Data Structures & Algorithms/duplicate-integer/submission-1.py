class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []
        for i in range(len(nums)):
            if nums[i] in seen:
                seen.append(nums[i])
            seen.append(nums[i])
        if len(seen) > len(nums):
            return True
        else:
            return False