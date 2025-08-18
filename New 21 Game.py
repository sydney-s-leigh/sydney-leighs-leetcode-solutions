# Author: Sydney Leigh
# Date: 08/17/2025
# Problem: https://leetcode.com/problems/new-21-game/description/
# Notes: I failed this problem on 08/17/2025 . 

# Alice plays the following game, loosely based on the card game "21".

# Alice starts with 0 points and draws numbers while she has less than k points. During each draw, 
# she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. 
# Each draw is independent and the outcomes have equal probabilities.

# Alice stops drawing numbers when she gets k or more points.

# Return the probability that Alice has n or fewer points.

# Answers within 10^-5 of the actual answer are considered accepted.

# Example 1:

# Input: n = 10, k = 1, maxPts = 10
# Output: 1.00000
# Explanation: Alice gets a single card, then stops.
#
# We only draw once because any number of points between 1 and 10 exceeds k the probability is 100% 
# that alice has 10(n) or less points because she can only get between 1 and 10 points in this
# scenario

# Example 2:

# Input: n = 6, k = 1, maxPts = 10
# Output: 0.60000
# Explanation: Alice gets a single card, then stops.
# In 6 out of 10 possibilities, she is at or below 6 points.
#
# Again we only draw once because any number of points between 1 and 10 exceeds k, however now we
# calculate the odds that pointsTotal <= n and with just one draw 6/10 result in pointsTotal <= n
# because if we randomly draw a 7,8,9,10 we > 6. So 4 out of 10 cases or 40% of cases result in
# pointsTotal > n and 60% (aka we busted) of cases pointsTotal <= n, so we return .60 

# Example 3:

# Input: n = 21, k = 17, maxPts = 10
# Output: 0.73278
#
# Now we can draw up to 17 times because the min value of a draw is 1. The least amount of draws would be
# 2 because that would mean we draw maxPts (10) twice for a total value of 20 which is < k. Now we need to
# figure out how many scenarios between these 2 and 17 draws give a chance of being less than or equal to n
# for that we enumerate the cases where this is the case and calculate the probability of the cases that
# pointsTotal > n (aka we busted)

# Constraints:

#     0 <= k <= n <= 10^4
#     1 <= maxPts <= 10^4

import random
import math

class Solution(object):
    def new21Game(self, n, k, maxPts):
        """
        :type n: int
        :type k: int
        :type maxPts: int
        :rtype: float
        """        

        # The probability of the draws totaling to less than or equal to n will always be 100% if we can 
        # only draw once and n == maxPts
        if n == maxPts and k == 1:
            return 1.0
        
        # For all other cases...

        probability = 1.0 #Some equation
        #We draw all 1s
        maxDraws = k
        #We draw all maxPts
        minDraws = math.ceil(k/maxPts)

        #Enumerate all the cases where pointsTotal would be < n at the end
        #This is a combinetics/permutations problem
        #Are they setting us up for some NP problem disaster?

        # Example
        # Input: n = 21, k = 17, maxPts = 10 
        # 17 draws of 1
        # 2 draws of 10,10 = 20
        # 2 draws of 10,9 = 19
        # 2 draws of 10,8 = 18
        # 2 draws of 10,7 = 17
        # 2 draws of 9,10
        # 8,10
        # 7,10
        # 3 draws 10,6,1
        # 3 draws 10,1,6
        # 3 draws 10,5,2
        # 3 draws 10,4,3 etc...
        # 4 draws 10,2,2,3
        # 4 draws 10,2,2,4 etc...

        # for x in range(minDraws, maxDraws):
        #     possiblePermutations = 

        # Rolling a dice with sides 2 - 17 twice, this gives
        # 16^2 = 256 outcomes, but we need to subtract all the outcomes where the roll > n

        # 2 draws 1-10 = 10*10 = 100 draw possibilities
        # How many draw possibilities are there where total > k <= n?
        # How many draws are > k?
        # 

        

        #return math.comb(k, maxPts) 

        # print("Min draws =")
        # print(minDraws)



        # alicePoints = 0

        # #This at least gets the point total
        # while(alicePoints < k):
        #     alicePoints += random.randrange(1, maxPts)

        # return alicePoints

s = Solution()

def testCase():
    print(s.new21Game(10, 1, 10))
    print(s.new21Game(6, 1, 10))
    print(s.new21Game(21, 17, 10))

testCase()