from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        count = 0
        length = len(nums)
        if length == 1:
            return 1
        for i in range(length):
            if i < length - 1:
                if nums[i] == nums[i + 1]:
                    print(nums[i],'the same')
                    nums[i]= -200
                i += 1
            else:
                print("the last one",(nums[i]))
                if nums[i]==nums[i-1]:
                    nums.remove(nums[i])

        while count < len(nums):
            if nums[count] == -200:
                nums.remove(nums[count])
                count -=1
            count+=1
        #
        # while -200 in nums:
        #     nums.remove(-200)

        print(nums)
        print(len(nums))
        return (len(nums))


s = Solution()
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])