class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            digits = list(map(int, str(num)))
            digits.sort()
        else:
            digits = list(map(int, str(abs(num))))
            digits.sort(reverse=True)

        if len(digits) > 2 and digits[0] == 0 and num > 0:
            checker = 1
            while digits[checker] == 0:
                checker += 1

            digits[0], digits[checker] = digits[checker], digits[0]

        return int(''.join(str(d) for d in digits)) if num > 0 else 0 - int(''.join(str(d) for d in digits))