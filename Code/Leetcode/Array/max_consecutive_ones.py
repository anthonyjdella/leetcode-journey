from typing import List

############ Question ################
# ❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2
# ❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓
######################################





############ Pseudo Code ################
# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝

# O(N2) 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌
# You can do nested for loops to look at each pair of numbers to get the count, however this is O(n2) since it has nested loops.

# O(N) 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆
# Create variables to track the current count and the maxiumum count. Then check which is greater.

# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝
######################################





class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentCount = 0
        maxCount     = 0
        
        for num in nums:
            if num == 1:
                currentCount += 1
            else:
                currentCount =  0
            maxCount = max(currentCount, maxCount)
        return maxCount
