test_cases = int(input())

for _ in range(test_cases):
    number_of_kiduses = int(input())
    health = list(map(int, input().split()))
    deadlines = list(map(int, input().split()))

    kidus_stats = sorted(zip(health, deadlines), key=lambda x: x[1])

    min_power = 1
    max_power = max(health) if health else 1
    required_power = max_power

    while min_power <= max_power:
        mid_power = (min_power + max_power) // 2
        if mid_power == 0:
            mid_power = 1
            continue
    
        is_possible = True
        time_passed = 0

        for h, l in kidus_stats:
            attacks_needed = (h + mid_power - 1) // mid_power
            time_passed += attacks_needed

            if time_passed > l:
                is_possible = False
                break
        
        if is_possible:
            required_power = mid_power
            max_power = mid_power - 1
        else:
            min_power = mid_power + 1
    
    print(required_power)