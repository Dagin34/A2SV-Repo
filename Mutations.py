def mutate_string(string, position, character):
  return str(string[:position] + character + string[position+1:])

if __name__ == '__main__':
  string = input()
  position, char = input().split()
  s_new = mutate_string(string, int(position), char)
  print(s_new)