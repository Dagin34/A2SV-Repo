string_len = int(input())
text = str(input())

genome = 'ACTG'
operation_count = float('inf')

for i in range(string_len - 3):
    current_operations = 0

    for j in range(4):
        char_text = text[i+j]
        char_genome = genome[j]

        difference = abs(ord(char_text) - ord(char_genome))
        # This is because the alphabet loops back after reaching Z
        current_operations += (min(difference, 26 - difference))

    if current_operations < operation_count:
        operation_count = current_operations

print(operation_count)