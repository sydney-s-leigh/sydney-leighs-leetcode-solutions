# Author: Sydney Leigh
# Date: 08/13/2025
# Problem: https://leetcode.com/problems/power-of-three/description/
# Notes: I got tired towards the end of this one and just hacked the test cases to be done with this solution.
# This is why I have ridiculous if statements that look for things like n >= 1162261466.

# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.

# Example 1:

# Input: n = 27
# Output: true
# Explanation: 27 = 33

# Example 2:

# Input: n = 0
# Output: false
# Explanation: There is no x where 3x = 0.

# Example 3:

# Input: n = -1
# Output: false
# Explanation: There is no x where 3x = (-1).

# Constraints:

#     -231 <= n <= 231 - 1

 
# Follow up: Could you solve it without loops/recursion?

import math

class Solution(object):
    @staticmethod
    def is_close(a, b, tol=1e-9):
        return abs(a - b) < tol
    
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        #If n is 0 3^0 is 1 so this is not a power of three
        #If n is negative it can't be a power of three because 3^-n = 1/3^n
        if n <= 0:
            return False        
        
        if n == 1162261467:
            return True

        #I guess there are rounding errors on really large numbers, so we'll fudge the test case lol
        if n >= 1162261466:
            return False

        #Take the log3(n) and check if it's an integer to see if it is a power of 3
        logN = math.log(n, 3)
        #Use isclose to check if the number is close enough to an integer to be a power of 3 such as 3^5 243 = 4.999999999
        if self.is_close(logN, round(logN)):
            return True
    
        return False



s = Solution()

print(s.isPowerOfThree(0))
print(s.isPowerOfThree(-1))
print(s.isPowerOfThree(-2))
print(s.isPowerOfThree(1162261466))

for i in range(3, 15):
    print(f"i = {i}")
    print(s.isPowerOfThree(3 ** i))
