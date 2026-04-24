n = int(input())
target = ['A','S','V']

# S V A
def find(initial, last_word, second_from_last):
    if initial == n:
        return 1

    answer = 0
    for char in target:
        if char == last_word:
            continue
        if second_from_last == "S" and last_word == "V" and char == "A":
            continue

        answer += find(initial + 1, char, last_word)
    
    return answer
    
print(find(0, "", ""))