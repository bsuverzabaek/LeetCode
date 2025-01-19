class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrack(digits, index, current, result, dic):
            if index == len(digits):
                result.append(current)
                return

            letters = dic[digits[index]]

            for letter in letters:
                backtrack(digits, index + 1, current + letter, result, dic)

        result = []
        if digits == "":
            return result

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        backtrack(digits, 0, "", result, dic)
        return result
