class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        total = 1
        for num in nums[-3:][::-1]:
            total*= num
        total2 = nums[0] * nums[1] * nums[-1]
        return max(total,total2)
        