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
        
# Anhs answer (below) using while loop instead of recursion.
#         ans = 0
#         for num in nums:
#             numDigits = self.countDigit(num)
#             if numDigits % 2 == 0:
#                 ans += 1
                
        
#     def countDigit(self, num):
#         count = 0
#         while num > 0:  # 19 -> 1
#             num //= 10 # 0
#             count += 1 # 2
            
#         return count