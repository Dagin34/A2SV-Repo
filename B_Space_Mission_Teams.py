N, D = map(int, input().split())
P = list(map(int, input().split()))

P.sort()
teams = 0
left, right = 0, N-1

while left <= right:
    skill = P[right] 
    while skill <= D and left < right:
        skill += P[right]
        left += 1
    
    if skill > D:
        teams += 1
    
    right -= 1

print(teams)