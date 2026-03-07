test_cases = int(input())
for _ in range(test_cases):
    pc, cc = map(int, input().split())
    prices = list(map(int, input().split()))
    coupons = list(map(int, input().split()))

    prices.sort(reverse=True)
    coupons.sort()

    left, right = 0, 0
    total_sums = 0

    while left < cc and right < pc:
        if coupons[left] == 1:
            total_sums += 0
        else:
            temp_list = prices[right : right + coupons[left] - 1]
            total_sums += sum(temp_list)

        right += coupons[left]
        left += 1

    if right < pc:
        total_sums += sum(prices[right:])
    
    print(total_sums)
