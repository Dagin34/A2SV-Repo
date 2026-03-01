from collections import Counter

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))

    counts = Counter(arr)
    im_the_goat = False #Even tho I am the GOAT of Halloween Heists

    for i in counts:
        if counts[i] % 2 != 0:
            im_the_goat = True
            break
    
    print("YES" if im_the_goat else "NO")