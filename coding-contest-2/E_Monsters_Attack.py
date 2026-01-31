number_of_test_cases = int(input())
results = []

for _ in range(number_of_test_cases):
  num_of_monsters, num_of_bullets = map(int, input().split(' '))
  
  healths = list(map(int, input().split(' ')))
  positions = list(map(int, input().split(' ')))
  
  dist_health = {}
  for i in range(num_of_monsters):
    distance = abs(positions[i])
    dist_health[distance] = dist_health.get(distance, 0) + healths[i]
      
  sorted_distances = sorted(dist_health.keys())
  
  can_survive = True
  bullets_accrued = 0
  last_time = 0
  
  for distance in sorted_distances:
    total_bullets_available = distance * num_of_bullets
    
    bullets_accrued += dist_health[distance]
    
    if bullets_accrued > total_bullets_available:
      can_survive = False
      break
  
  results.append("YES" if can_survive else "NO")

print('\n'.join(results))