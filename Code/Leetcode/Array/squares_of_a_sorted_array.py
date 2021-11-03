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

# This needs 3 pointers. One pointer for the start of the list, one pointer for the end of the list, and one pointer for the result list. The pointer for the result list is independent of the start and end pointer from the input list.
# When you iterate over the result list, you need to keep track of it through an iterator variable which is going from the end to the start of a new list.

# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝
######################################








class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        i = len(nums) - 1
        result = [0 for num in nums]
        
        while end >= start:
            startSquared = nums[start] * nums[start]
            endSquared = nums[end] * nums[end]
            
            if (startSquared > endSquared):
                result[i] = startSquared
                start += 1
            else:
                result[i] = endSquared
                end -= 1
            i -= 1

        return result


# My original solution is o(n^2) because the insert operation is o(n). Instead of using insert, I can create an "empty" list and override the values instead. 
# This is not o(n m) because even though you may think insert is used on the result set, that result list will be the same length as the input list. So, they are dependent on eachother, meaning that this isn't o (n m), but rather o(n^2).
#         result = []
#         beg = 0
#         end = len(nums) - 1       

#         for num in nums:
#             squareBeg = nums[beg] * nums[beg]
#             squareEnd = nums[end] * nums[end]

#             if squareBeg >= squareEnd:
#                 result.insert(0, squareBeg)
#                 beg+=1
#             else:
#                 result.insert(0, squareEnd)
#                 end-=1

#         return result


# anh's solution using list comprehension to create a static array where the values are overridden, this will make the solution o(n) since we are not using the insert operation which is o(n). use the while loop since, we dont need to go through each element, we only need to do so when both pointers are at the same position.
#         result = [0 for _ in nums]
#         left = 0
#         right = len(nums) - 1
#         i = len(nums) - 1

#         while left <= right:
#             squareLeft = nums[left] * nums[left]
#             squareRight = nums[right] * nums[right]

#             if squareLeft >= squareRight:
#                 result[i] = squareLeft
#                 left += 1
#             else:
#                 result[i] = squareRight
#                 right -= 1 
#             i -= 1

#         return result    
