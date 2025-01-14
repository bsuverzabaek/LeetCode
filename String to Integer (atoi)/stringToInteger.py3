class Solution:
    def myAtoi(self, s: str) -> int:
        index, total, sign = 0, 0, 1
        if len(s) == 0:
            return 0

        while index < len(s) and s[index] == " ":
            index += 1

        if index == len(s):
            return 0

        if s[index] == "-" or s[index] == "+":
            sign = 1 if s[index] == "+" else -1
            index += 1

        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            
            if digit < 0 or digit > 9:
                break

            if total > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31

            total = total * 10 + digit
            index += 1

        return total * sign
