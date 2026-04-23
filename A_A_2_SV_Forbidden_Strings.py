n = int(input())
target = ['A','S','V']

def find(initial, word, word2):
    if initial == n:
        return 1

    answer = 0
    for char in target:
        if char == word:
            continue
        if word2 == "S" and word == "V" and char == "A":
            continue

        answer += find(initial + 1, char, word)
    
    return answer
    
print(find(0, "", ""))