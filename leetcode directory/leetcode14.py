# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
# x = "Hello World!"
# print(x)
# print(x[0:1])  => H

import math
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if len(strs) <=0:
            return ans
        else:
            return self.divideandconquer(strs , 0 ,len(strs)-1)

    def compare(self , longestcpleft, longestcpright) -> str:
        loopcount = min(len(longestcpleft), len(longestcpright))  #左右誰短
        for i in range(loopcount):
            if longestcpleft[i] == longestcpright[i]:
                continue
            else:
                return longestcpleft[0:i]
        return longestcpleft[0:loopcount]

    def divideandconquer(self, strs: List[str], left, right) -> str:
        if left == right:
            return strs[left]
        else:
            mid = int((left+right)/2)
            longestcpleft = self.divideandconquer(strs, left, mid)
            longestcpright = self.divideandconquer(strs, mid + 1, right)
            print("mid:",mid, " left:" , longestcpleft, " right: ",longestcpright)
            return self.compare(longestcpleft, longestcpright)

#14
strs = ["flower","flow","flight"]
class Solution02:
    def longestCommonPrefix(self, strs):
        min = len(strs[0])
        index = 0
        for i in strs:
            if len(i) < min:
                index = strs.index(i)
                min = len(i)
        ans = strs[index]
        print("選出那個長度最短的人" , ans)
        #選出那個長度最短的人
        initial = ""
        for j in range(len(ans)):
            for string_ in strs:
                if ans[j] != string_[j]:
                    print("now ans=" , initial)
                    return initial
            else:
                initial+=ans[j]
        return initial

s = Solution()
s2 = Solution02()
print(s.longestCommonPrefix(["f1a", "f1b", "f3c" , "f3d" , "f4e" , "f4f" , "f2g" ,"f2h"]))
#print(s2.longestCommonPrefix(["flower", "flow", "flight" , "flo" , "flopopdw"]))