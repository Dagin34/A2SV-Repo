import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    
    brand_sum = defaultdict(int)
    
    for _ in range(k):
        b, c = map(int, input().split())
        brand_sum[b] += c
    
    # take only top n values using heap
    values = list(brand_sum.values())
    
    if len(values) <= n:
        print(sum(values))
    else:
        print(sum(heapq.nlargest(n, values)))