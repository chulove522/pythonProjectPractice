
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        string1 = haystack
        string2 = needle
        start_index = string1.find(string2)
        return start_index

s = Solution()
print(s.strStr("hello",'ll'))