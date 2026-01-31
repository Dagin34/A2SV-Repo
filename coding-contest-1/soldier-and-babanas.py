k, n, w = map(int, input().split())
total_cost = k * (w * (w + 1) // 2)

amount_to_borrow = total_cost - n
print(max(0, amount_to_borrow))