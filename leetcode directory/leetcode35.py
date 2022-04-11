# 35. Search Insert Position
# # Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.
from typing import List


class Solution:
    index = 0
    leave = False

    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     temp = 0
    #     if Solution.leave == True:
    #         return Solution.index
    #     half = int(len(nums) / 2)
    #     print(nums, "half =",nums[half])
    #     if half == 0:
    #         print("有特殊狀況")
    #         # print(Solution.index)
    #         if target > nums[0]:
    #             print("bigger")
    #             Solution.leave = True
    #             return 1
    #         elif target < nums[0]:
    #             print("smaller")
    #             Solution.leave = True
    #             return 0
    #         else:
    #             print("except")
    #
    #     if target < nums[half]:
    #         temp = Solution.searchInsert(self , nums[0:half], target)
    #         Solution.index += temp
    #         return temp
    #     elif target > nums[half]:
    #         temp = Solution.searchInsert(self , nums[half:], target) + half
    #         Solution.index += temp
    #         return temp
    #     elif target == nums[half]:
    #         return Solution.index + half
    #     else:
    #         print("except")
    #         return -1
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return low
s = Solution()
#print("答案是", s.searchInsert([1,2,3,4,5,6,7,8,8,10], 9))
print("--答案是--", s.searchInsert([1,3,5,6], 7))