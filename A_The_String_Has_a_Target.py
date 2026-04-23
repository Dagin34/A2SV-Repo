import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()

    min_char = min(s)
    last_pos = s.rfind(min_char)
    print(s[last_pos] + s[:last_pos] + s[last_pos + 1:])