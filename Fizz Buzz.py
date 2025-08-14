# Author: Sydney Leigh
# Date: 08/13/2025
# Problem: https://leetcode.com/problems/fizz-buzz/description/
# Notes: This is the first leetcode problem I ever solved.

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = [str(i) for i in range(1, n + 1)]

        for y in range(len(answer)):
            num = int(answer[y])
            if (num % 3 == 0) and (num % 5 == 0):
                answer[y] = "FizzBuzz"
            elif num % 3 == 0:
                answer[y] = "Fizz"
            elif num % 5 == 0:
                answer[y] = "Buzz"
    
        return answer
    
s = Solution()


print(s.fizzBuzz(3))  
print(s.fizzBuzz(5))
print(s.fizzBuzz(15))   
print(s.fizzBuzz(7))