class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1 
                elif three_sum > 0:
                    r -= 1
                else:
                    triplets.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l += 1
                    r -= 1


        return list(triplets)

