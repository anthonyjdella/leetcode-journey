from typing import List

############ Question ################
# ❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# ❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓
######################################







############ Pseudo Code ################
# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝

# O(N2) 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌
# Loop through the list, then calculate the square of each number. Then loop through the results and sort the numbers.

# O(N) 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆
# Have a pointer at the start of the list, and a pointer at the end of the list. Then square both values. Compare the values of at both pointers, the larger value will be placed at the end of a new list. Then the pointer which is the greater of the two (or the value that was put into the new list) will move its pointer the opposite direction.

# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝
######################################








class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        