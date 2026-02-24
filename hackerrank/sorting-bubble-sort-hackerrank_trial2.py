def countSwaps(a):
    swaps = 0
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[j] < a[i]:
                a[i], a[j] = a[j], a[i]
                swaps += 1
    
    return swaps, a

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    swaps, a = countSwaps(a)
    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')