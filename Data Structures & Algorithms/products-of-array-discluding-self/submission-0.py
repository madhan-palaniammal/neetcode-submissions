class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lproducts = [1] * len(nums)
        rproducts = [1] * len(nums)

        for i in range(1, len(nums)):
            lproducts[i] = nums[i-1] * lproducts[i-1]

        for i in range(len(nums)-2, -1, -1):
            rproducts[i] = nums[i+1] * rproducts[i+1]

        products = []
        for i in range(len(nums)):
            products.append(lproducts[i]*rproducts[i])

        return products