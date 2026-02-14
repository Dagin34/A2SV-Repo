test_cases = int(input())

for _ in range(test_cases):
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    relays = []
    for i in range(n):
        if b[i] < p:
            relays.append((b[i], a[i]))
        
    relays.sort()

    total_cost = p
    places_notified = 1

    for (cost, limit) in relays:
        if places_notified >= n:
            break

        can = min(n - places_notified, limit)
        total_cost += can * cost
        places_notified += can

    if places_notified < n:
        total_cost += (n - places_notified) * p

    print(total_cost)