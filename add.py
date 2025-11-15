#leetcode 258 add digits
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            s = 0

            while num:
                s += num % 10
                num = num // 10
            num = s
        return num
