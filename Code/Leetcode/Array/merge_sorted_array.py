from typing import List

############ Question ################
# ❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓❓
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
######################################







############ Pseudo Code ################
# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝

# O(N2) 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌 🐌

# O(N + M) Time 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆 🐆
# O(1) Space 🚀 🚀 🚀 🚀 🚀 🚀 🚀 🚀 🚀 🚀 🚀 🚀 🚀
# Important thing to note: the question states that you need to do this in place, to the original nums1 list. Take note of m and n, as they are the lengths of the first part of nums1 and the 0s in the remaining part of nums1. [1,2,3,0,0,0] and [2,5,6] will become [1,2,2,3,5,6]. Look at this question backwards. It is best to do loop backwards from the end of the list to the start. So compare the end number in nums1 to the end number in nums2. In this case, 3 and 6. If 6 is greater than 3, then place 6 at the end of nums1, i.e. [1,2,3,0,0,6]. Then move your nums2 pointer over to the left. And repeat.

# 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝 📝
######################################








class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        '''
        nums1 = [1,2,3,0,0,0]
        nums2 = [2,5,6]
        m = 3
        n = 3
        len(nums1) = m + n
        '''

        while m > 0 and n > 0:
            if nums2[n-1] > nums1[m-1]:     #if end of nums2 is bigger than end of nums1, put it on the last item of nums1
                nums1[m+n-1] = nums2[n-1]
                n-=1
            else:
                nums1[m+n-1] = nums1[m-1]
                m-=1
        nums1[:n] = nums2[:n]
