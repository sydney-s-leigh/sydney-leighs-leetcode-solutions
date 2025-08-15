# Author: Sydney Leigh
# Date: 08/15/2025
# Problem: https://leetcode.com/problems/power-of-four/description/
# Notes: 

# Given an integer n, return true if it is a power of four. Otherwise, return false.

# An integer n is a power of four, if there exists an integer x such that n == 4^x.

# Example 1:

# Input: n = 16
# Output: true

# Example 2:

# Input: n = 5
# Output: false

# Example 3:

# Input: n = 1
# Output: true

# Constraints:

#     -2^31 <= n <= 2^31 - 1

 
# Follow up: Could you solve it without loops/recursion?

import math

class Solution(object):
    @staticmethod
    def is_close(a, b, tol=1e-9):
        return abs(a - b) < tol
    
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        #If n is 0 4^0 is 1 so this is not a power of four
        #If n is negative it can't be a power of four because 4^-n = 1/4^n
        if n < 4:
            return False        
        
        #4^x = (2^x * 2^x)
        #x = 1024
        #(2^y * 2^y) = 1024
        #y * y = 1024 = y^2 = sqrt(1024) = 32
        #1024 in binary is 0100 0000 0000
        #Pattern realized that if we convert this to a binary and there is only one bit set
        # to 1 for the entire string of bits and the number of 0s is even then it must 
        # be a power of 4
        power = n
        binaryValue = str(bin(power)[2:])
        #print(binaryValue)

        #print("How many 1s do we have?")
        oneCount = binaryValue.count("1")

        #print(oneCount)

        if oneCount == 1:
            #Count trailing 0's and see if they are odd or even, if even it's a power of 4
            #Find where 1 is:
            onePosition = binaryValue.find("1")
            zeros = binaryValue[onePosition+1:]
            #print(zeros)
            zerosLen = len(zeros)
            #print("There are " + str(zerosLen) + " zeros.")

            if (zerosLen % 2) == 0:
                #print("Number of zeros is even! This is a power of four!")
                return True
            #else:
            #    print("Number of zeros is odd. This is not a power of four.")
    
        return False

s = Solution()

def testCase():
    for i in range(32):
        num = 4 ** i
        print("Doing 4^" + str(i) + "(" + str(num) + "): ")
        print(s.isPowerOfFour(num))

testCase()

# checkNumber = 64
# print("Is " + str(checkNumber) + " a power of 4?")
# print(s.isPowerOfFour(checkNumber))