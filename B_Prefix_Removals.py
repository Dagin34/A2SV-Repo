
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    
    freq = [0] * 26
    for c in s:
        freq[ord(c) - ord('a')] += 1
    
    for i, c in enumerate(s):
        freq[ord(c) - ord('a')] -= 1
        if freq[ord(c) - ord('a')] == 0:
            print(s[i:])
            break