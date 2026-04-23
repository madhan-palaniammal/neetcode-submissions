class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max(
            nums[0],
            self.help_rob(nums[1:]), 
            self.help_rob(nums[:-1])
        )

    def help_rob(self, nums):
        if not len(nums):
            return 0

        far = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            curr = max(far + nums[i], prev)
            far, prev = prev, curr

        return prev
            
