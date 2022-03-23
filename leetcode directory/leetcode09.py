class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        :type x: int
        :rtype: bool
        """
        y = str(x)
        #for i in range(len(y)):
        print(y , ' and ' , y[::-1])
        if y != y[::-1]:
            return False
        return True


palin = Solution()
print(palin.isPalindrome(1231321))
