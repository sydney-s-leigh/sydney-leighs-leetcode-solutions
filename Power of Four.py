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

class Solution(object):  
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        #If n is 0 4^0 is 1 so this is not a power of four
        #If n is negative it can't be a power of four because 4^-n = 1/4^n
        # 4^0 = 1 so 1 is the only number below 4 that is a power of 4
        # otherwise, 4 is the first power were 4^1 = 4
        if n == 1:
            return True
        elif n < 4:
            return False
        
        #4^x = (2^x * 2^x)
        #x = 1024
        #(2^y * 2^y) = 1024
        #y * y = 1024 = y^2 = sqrt(1024) = 32
        #1024 in binary is 0100 0000 0000
        #Pattern realized that if we convert n to a binary and there is only one bit set
        # to 1 for the entire string of bits and the number of 0s is even then it must 
        # be a power of 4
        power = n
        binaryValue = str(bin(power)[2:])
        oneCount = binaryValue.count("1")

        if oneCount == 1:
            #Count trailing 0's and see if they are odd or even, if even it's a power of 4
            #Find where 1 is:
            onePosition = binaryValue.find("1")
            #Get the substring of all the 0s off after the 1
            zeros = binaryValue[onePosition+1:]
            #Count number of zeros after the 1
            zerosLen = len(zeros)

            #If the length is divisible by 2 then it's an even number of 0s
            if (zerosLen % 2) == 0:
                #1 followed by even number of 0s is a binary number that is a power of 4
                return True
    
        #Number is not a power of four so we return False
        return False

s = Solution()

def testCase():
    for i in range(32):
        num = 4 ** i
        print("Doing 4^" + str(i) + "(" + str(num) + "): ")
        print(s.isPowerOfFour(num))

testCase()

checkNumber = 1
print("Is " + str(checkNumber) + " a power of 4?")
print(s.isPowerOfFour(checkNumber))