# 53. Maximum Subarray
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max = now = nums[0]
        for i in nums[1:]:
            if now + i < i: # 如果拖後腿，越加越小
                now = i
            else:
                now = now + i
            if now > max:
                max = now

        return max


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
