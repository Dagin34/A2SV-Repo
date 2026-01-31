n = int(input())
cards = list(map(int, input().split()))

sereja = 0
dima = 0
turn = 0

while cards:
  if cards[0] > cards[-1]:
    chosen = cards.pop(0) 
  else:
    chosen = cards.pop(-1) 
  
  if turn % 2 == 0:
    sereja += chosen
  else:
    dima += chosen
  turn += 1

print(sereja, dima)