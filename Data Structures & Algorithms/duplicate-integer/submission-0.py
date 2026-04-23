class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        a = set()
        for i in range(len(nums)):
            if nums[i] in a:
                return True
            a.add(nums[i])

        return False

        

        