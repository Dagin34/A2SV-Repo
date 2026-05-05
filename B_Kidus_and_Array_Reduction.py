test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))

    stack = []

    for i in range(n - 1, -1, -1):
        while stack and stack[-1] < a[i]:
            stack.pop()
        stack.append(a[i])
    
    print(len(stack))