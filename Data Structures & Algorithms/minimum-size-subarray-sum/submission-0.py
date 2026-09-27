class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        min_length = float("inf")
        total = 0
        for right in range (n):
            total += nums[right]
            while total >= target:
                length = right - left + 1
                min_length = min(length, min_length)

                total-=nums[left]
                left+=1
        if min_length == float("inf"):
            return 0
        return min_length
                




        