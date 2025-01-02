class Solution:
    def romanToInt(self, s: str) -> int:
        index = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = prev = 0

        for char in s:
            current = index[char]
            
            if current > prev:
                total += current - (2 * prev)
            else:
                total += current

            prev = current

        return total
