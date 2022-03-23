from typing import List
# 先處理過再整理，不然暴力法程式會超時
# 若是清單不同的糖果多於一半直接回傳maxcandy
# 如果清單不同的糖果少於一半，回傳清單不同的糖果數目


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        maxcandy = int(len(candyType)/2)
        candycount = 0
        index = 0
        skipone = False

        candyType.sort()
        length = len(candyType)
        for i in range(length):
             if i<length-1:
                 if candyType[i] != candyType[i+1]:
                     print(candyType[i])
                     candycount = candycount + 1
             else:
                 print("thelast;",candyType[i])
                 candycount = candycount + 1

        if(candycount >= maxcandy):
            print("ans = " , maxcandy)
            return maxcandy

        else:
            print("ans = " , candycount)
            return candycount


s = Solution()
s.distributeCandies([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,8,9])
s.distributeCandies([1,1,2,2,3,3])