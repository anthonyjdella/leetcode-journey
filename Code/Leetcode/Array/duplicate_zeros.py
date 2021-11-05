from typing import List

############ Question ################
# ❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓
# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

# Example 1:
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

# Example 2:
# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]
######################################







############ Pseudo Code ################
# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝

# O(N2) 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌

# O(N) Time
# O(N) Space 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆
# Although this problem wants to modify the original list, that doesn't mean we can't create another list and return the original. Use list comprehension to create a dynamic list of 0's. Then loop through the array and if the number from the original list is not 0, then assign that value to the new list. Else if the number in the original array is zero, skip an increment. Then assign the values of the new list to overwrite the original list.
# Two pointers are needed to increment. One is for the original list, the other is for the new list.

# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝
######################################








class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        # Create a dynamic list the same size of the input arr
        arr2 = [0 for _ in range(len(arr))]
        # Keep track of two pointers, one for the original list and one for the new list
        i, j = 0, 0
        # You can loop through either the original list or the new list, but the increment needs to be the faster of the two (j), since it moves faster (2) than i (1).
        while j < len(arr2):
            num = arr[i]
            if num != 0:
                arr2[j] = num
                # Increment the original list
                i += 1
                # Increment the new list
                j += 1
            else:
                # Increment the original list
                i += 1
                # If the number is 0, increment the new list by two, since our output needs two zeros.
                j += 2 
        # Loop through the original list and re-assign values from the newly created list into the original. This type of assignment is O(1) because it just reasigns a variable pointer. If you use the insert() function, that would be O(N) since it loops through the list.
        for i in range(len(arr)):
            arr[i] = arr2[i]
