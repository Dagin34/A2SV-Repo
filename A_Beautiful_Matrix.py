tests = []

for _ in range(5):
    tests.append(list(map(int, input().split())))

for i in range(5):
    for j in range(5):
        if tests[i][j] == 1:
            row, col = i, j

moves = abs(row - 2) + abs(col - 2)

print(moves)