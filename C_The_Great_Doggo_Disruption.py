n = int(input())
s = input()

if n == 1:
    print("Yes")
    exit()

seen_colors = set()
possible = False

for char in s:
    if char in seen_colors:
        possible = True
        break
    seen_colors.add(char)

print("Yes" if possible else "No")