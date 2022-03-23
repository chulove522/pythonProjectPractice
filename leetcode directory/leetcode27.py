from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        ans = 0
        for i in nums:
            if i == val:
                count +=1
        ans = count
        while count > 0:
            nums.remove(val)
            print("nums now",nums)
            count -= 1
        print(len(nums))
        return(len(nums))

s = Solution()
#s.removeElement([0,1,2,10,2,3,0,4,10,2,1,4,5,74,10,5,6,5,2,3,5,4,10],10)
s.removeElement([0,1,2,2,3,0,4,2],2)