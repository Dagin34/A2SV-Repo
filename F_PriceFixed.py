import sys
input = sys.stdin.read
data = input().split()
    
n = int(data[0])
products = []
idx = 1
for _ in range(n):
    a = int(data[idx])
    b = int(data[idx+1])
    products.append([a, b])
    idx += 2
    
products.sort(key=lambda x: x[1])

left = 0
right = n - 1
total_bought = 0
total_cost = 0

while left <= right:
    if total_bought >= products[left][1]:
        total_cost += products[left][0]
        total_bought += products[left][0]
        left += 1
    else:
        needed = products[left][1] - total_bought
        can_take = min(needed, products[right][0])
        
        total_cost += can_take * 2
        total_bought += can_take
        products[right][0] -= can_take
        
        if products[right][0] == 0:
            right -= 1
            
print(total_cost)