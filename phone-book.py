# Read the number of testcases
n = int(input())

contact_dict = {}
for _ in range(n):
  # Taking name and number and splitting them into two variables
  entry = input().split()
  contact_dict[entry[0]] = entry[1]

while True:
  try:
    query = input()
    if not query:
      break
        
    if query in contact_dict:
      print(f"{query}={contact_dict[query]}")
    else:
      print("Not found")
  # CPH kept throwing an end of file error
  except EOFError:
    break