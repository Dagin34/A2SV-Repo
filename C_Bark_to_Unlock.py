password = input()
n = int(input())

words = []
for _ in range(n):
  words.append(input())

found = False
starts_with = False
ends_with = False

for word in words:
  if word == password:
    found = True
    
  if word[1] == password[0]:
    ends_with = True
  
  if word[0] == password[1]:
    starts_with = True
        
if found or (ends_with and starts_with):
  print("YES")
else:
  print("NO")