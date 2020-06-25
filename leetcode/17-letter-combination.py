class Solution:
    def letterCombinations(self, digits: str):
        mappings = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        strs = []
        for d in digits:
            first_digit = not strs
            new_strs = []
            for c in mappings[d]:
                if first_digit:
                    new_strs.append(c)
                else:
                    for s in strs:
                        new_strs.append(s + c)
            strs = new_strs
        return strs


if __name__ == '__main__':
    print(Solution().letterCombinations('235'))
