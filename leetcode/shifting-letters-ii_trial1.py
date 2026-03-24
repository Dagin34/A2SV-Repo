class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for l, r, d in shifts:
            if d == 1:
                diff[l] += 1
                diff[r + 1] -= 1
            else:
                diff[l] -= 1
                diff[r + 1] += 1

        for i in range(1, n):
            diff[i] += diff[i - 1]

        result = []
        for i in range(n):
            shift = diff[i] % 26
            new_char = (ord(s[i]) - ord('a') + shift) % 26
            result.append(chr(new_char + ord('a')))

        return "".join(result)