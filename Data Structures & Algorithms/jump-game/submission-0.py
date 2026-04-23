class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = nums[0]
        i = 0
        while jumps:
            if i == (len(nums) - 1):
                return True
            
            i += 1
            jumps = max(jumps - 1, nums[i])

        if i == (len(nums) - 1):
            return True
        return False

