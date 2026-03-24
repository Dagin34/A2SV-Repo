tests = int(input())

for _ in range(tests):
    s = input()
    working_keys = set()

    i = 0
    n = len(s)
    while i < n:
        char = s[i]
        count = 0
        while i < n and s[i] == char:
            count += 1
            i += 1
        if count % 2 != 0:
            working_keys.add(char)

    print(''.join(sorted(list(working_keys))))