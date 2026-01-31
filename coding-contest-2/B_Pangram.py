number_of_letters = int(input())
pangram = input().lower()

if len(set(pangram)) == 26:
  print("YES")
else:
  print("NO")