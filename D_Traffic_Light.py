import sys
input = sys.stdin.read().split()

test_cases = int(input[0])
curr_input = 1

for _ in range(test_cases):
    n = int(input[curr_input])
    target_color = input[curr_input + 1]
    s = input[curr_input + 2]
    curr_input += 3

    if target_color == 'g':
        print('0')
        continue

    doubled = s + s
    max_wait = 0
    green_indices = [idx for idx, char in enumerate(doubled) if char == 'g']
    green_pointer = 0

    for i in range(n):
        if s[i] == target_color:
            while green_indices[green_pointer] < i:
                green_pointer += 1
            
            wait_time = green_indices[green_pointer] - i
            if wait_time > max_wait:
                max_wait = wait_time
    
    print(str(max_wait))