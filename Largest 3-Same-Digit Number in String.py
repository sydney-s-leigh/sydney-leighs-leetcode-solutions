# Author: Sydney Leigh
# Date: 8/14/2025
# Problem: https://leetcode.com/problems/largest-3-same-digit-number-in-string/
# Notes: 
# You are given a string num representing a large integer. An integer is good if it meets the following conditions:

#     It is a substring of num with length 3.
#     It consists of only one unique digit.

# Return the maximum good integer as a string or an empty string "" if no such integer exists.

# Note:

#     A substring is a contiguous sequence of characters within a string.
#     There may be leading zeroes in num or a good integer.

 

# Example 1:

# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".

# Example 2:

# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.

# Example 3:

# Input: num = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

 

# Constraints:

#     3 <= num.length <= 1000
#     num only consists of digits.

import random

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        
        #Look for three consecutive numbers in reverse 9-0
        for i in range(9, -1, -1):
            y = str(i)
            z = y+y+y
            #print("Checking for " + z)
            #If find is not -1 it means it found the string and we can stop because its the highest
            if num.find(z) != -1:
                return z

        #If all cases 999-000 were not found we return ""    
        return ""

s = Solution()

#For the test case for this solution I want to write a function that generates strings from 3 to 1000 characters
#in length. Then I want to give them to largestGoodInteger() and have it return the substring of largest 3 ints
def testCase():
    #Test our 3 test cases
    print("Case:6777133339")
    print(s.largestGoodInteger("6777133339"))
    print("Case:2300019")
    print(s.largestGoodInteger("2300019"))
    print("Case:42352338")
    print(s.largestGoodInteger("42352338"))

    #Test 10 random numbers 3-1000 digits for 3 consecutive integers from largest to smallest
    for x in range(10):
        randStringLen = random.randrange(3, 1000) #random number between 3 and 1000 for strings to check
        random_string = ''.join(random.choice('0123456789') for _ in range(randStringLen))
        print("Case:" + random_string)
        print(s.largestGoodInteger(random_string))

    
testCase()


# randStringLen = random.randrange(3, 1000)
# random_string = ''.join(random.choice('0123456789') for _ in range(randStringLen))

# for x in range(25):
#     randStringLen = random.randrange(3, 1000)
#     random_string = ''.join(random.choice('0123456789') for _ in range(randStringLen))
#     print("String Length = " + str(len(random_string)) + ":" + random_string + " END")

# i = str(9)

# print(i+i+i)