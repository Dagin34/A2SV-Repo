num_of_cases = int(input())

data_base = {}
for _ in range(num_of_cases):
  name = input()
  
  if name not in data_base:
    print('OK')
    data_base[name] = 1

  else:
    count = data_base[name]
    new_name = f'{name}{count}'

    data_base[name] += 1
    data_base[new_name] = 1

    print(new_name)