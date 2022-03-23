# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        num = 0
        array = list(s)
        passloop = False
        print(array)
        for i in range(len(array)):
            if passloop == False:
                value =  array[i]
                print(value)
                if i < len(array)-1:
                    next_value = array[i+1]
                    print('value is '.format(value))
                    if dict.get(value,0) - dict.get(next_value,0) >= 0:
                        num = num + int(dict.get(value,0))
                        print(num)
                    else:
                        num = num + int(dict.get(next_value)) - int(dict.get(value))
                        print(num)
                        passloop = True
                else:
                    num = num + int(dict.get(value))
            else:
                passloop = False
        return num


roman = Solution()
print(roman.romanToInt("MCMXCIV"))
