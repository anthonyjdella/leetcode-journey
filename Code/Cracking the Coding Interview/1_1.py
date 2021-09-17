class Solution:

    def unique_char(self, string: str):
        for char in string: 
            print(char)
            for next_char in string[char + 1]:
                print(next_char)
                if next_char == char:
                    return False
        return True
    
# test = Solution()
# test_string = "hello"
# print(test.unique_char(test_string))


class Solution2:

    def is_unique(self, input: str):
        output = {}
        count = 0

        for char in input:
            if char in output:
                return False
            else:
                output[char] = count + 1
        return True
    
    def is_unique_pythonic(self, string):
        return len(set(string)) == len(string)

# test = Solution2()
# print(test.is_unique("leetcode"))
# print(test.is_unique_pythonic("leetcode"))
