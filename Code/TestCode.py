class TestCode:
    
    def is_unique(self, string: str):
        dict = {}
        occ = 0

        for char in string:
            if char in dict:
                return False
            dict[char] = occ + 1
        return True

    def is_unique_short(self, string: str):
        return len(set(string)) == len(string)


test = TestCode()
input = "leetcode"
print(test.is_unique(input))
print(test.is_unique_short(input))
