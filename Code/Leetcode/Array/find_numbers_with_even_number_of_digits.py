from typing import List

############ Question ################
# ❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓
# Given an array nums of integers, return how many of them contain an even number of digits.

# Example 1:
# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.

# Example 2:
# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.
# ❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓
######################################





############ Pseudo Code ################
# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝

# O(N M) 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌
# Look at each number in the list then see how many digits it has.
# If possible, use built in APIs.

# Find the number of digits by dividing by zero and then counting the number of iterations.
# // in python will round down.
# The following 3 solutions are O (n m) because first loop is dependent on the size of the array (n). The recursion/while loop is dependent on the size of the length of digits for each number (m). Therefore, it is not O(n2) because there are 2 different dependencies.

# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝
######################################






# Following had runtime of 35.7% on leetcode
class Solution:
    iterations = 1

    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if (self.count_iterations(num) % 2 == 0):
                count += 1
            self.clear_iterations()
        return count
            
    def count_iterations(self, num: int) -> int:
        quotient = num // 10
        if quotient != 0:
            self.iterations += 1
            self.count_iterations(quotient)
        return self.iterations
    
    def clear_iterations(self):
        self.iterations = 1


# Following had runtime 65.5% on leetcode
# Anhs answer using while loop instead of recursion.
#         ans = 0
#         for num in nums:
#             numDigits = self.countDigit(num)
#             if numDigits % 2 == 0:
#                 ans += 1
#         return ans
# 
#     def countDigit(self, num):
#         count = 0
#         while num > 0:  # 19 -> 1
#             num //= 10 # 0
#             count += 1 # 2
            
#         return count


# Following had runtime of 51.8% on leetcode
# Solution after revisiting this problem 1 month later
        # total_count = 0
        
        # for i, num in enumerate(nums):
        #     count = 1
        #     quotient = nums[i] // 10

        #     while quotient > 0:
        #         if quotient // 10 != 0:
        #             count += 1
        #             quotient = quotient // 10
        #         else:
        #             quotient = 0
        #             count += 1
        #     if count % 2 == 0:
        #         total_count +=1
        # return total_count





############ Solutions from Online ################
# ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️

# Using Built-in API
# Easiest way, using built in API. Check the length of each number, but in order to do that it needs to be converted to string first.
class Answer:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        
        for num in nums:
            if (len(str(num)) % 2 == 0):
                result +=1

        return result

# Using List Comprehension
# List comprehension creates a new list using the values from an existing list
class ListComprehension:
    def findNumbers(self, nums: List[int]) -> int:
        return len([num for num in nums if len(str(num) % 2 == 0)])

# ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️ ℹ️
######################################
