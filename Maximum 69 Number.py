# Author: Sydney Leigh
# Date: 8/16/2025
# Problem: https://leetcode.com/problems/maximum-69-number/description/
# Notes: 

# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.

# Example 2:

# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.

# Example 3:

# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.

 

# Constraints:

#     1 <= num <= 10^4
#     num consists of only 6 and 9 digits.

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """

        numString = str(num)
        returnNumString = ""

        for x in range(len(numString)):
            print("X = " + str(x))
            if numString[x:(x+1)] == "6":
                returnNumString = numString[:x] + "9" + numString[(x+1):]
                break;

        if returnNumString == "":
            returnNumString = numString

        return int(returnNumString)


s = Solution()

def testCase():

    print(s.maximum69Number("9669"))
    print(s.maximum69Number("9996"))
    print(s.maximum69Number("9999"))
    print(s.maximum69Number("66669"))

testCase()

# number = 6999

# numAsString = str(number)

# print("Number = " + numAsString)
# print("First number = " + numAsString[0:1])
# newNumString = ""
# print("NewNumString = " + newNumString)
# newNumString = numAsString[:0] + "9" + numAsString[1:]
# print("New Number = " + newNumString)

#print(numAsList)