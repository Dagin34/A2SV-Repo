import sys 

input_data = sys.stdin.read().split()

ptr = 0
t = int(input_data[ptr])
ptr += 1

results = []
for _ in range(t):
    n = int(input_data[ptr])
    k = int(input_data[ptr + 1])
    ptr += 2
    brand_totals = {}
    
    for _ in range(k):
        b = int(input_data[ptr])
        c = int(input_data[ptr + 1])
        ptr += 2
        
        if b in brand_totals:
            brand_totals[b] += c
        else:
            brand_totals[b] = c
    
    profits = list(brand_totals.values())
    profits.sort(reverse=True)
    
    total_earned = sum(profits[:n])
    results.append(str(total_earned))

print("\n".join(results))