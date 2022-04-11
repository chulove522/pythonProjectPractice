class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==0:
            return 0
        if x < 4:
            return 1
        left , right = 1,x//2 #取整除 - 返回商的整數部分（向下取整）
        while left <=right:
            mid = left + (right-left)//2
            if mid > x/mid:
                right = mid - 1
            else:
                left = mid + 1
        return left -1