# class Solution:
def findWords(words: list[str]) -> list[str]:
    final = []
    row1 = set([char for char in 'qwertyuiop'])
    row2 = set([char for char in 'asdfghjkl'])
    row3 = set([char for char in 'zxcvbnm'])

    for word in words:
        temp_word = set([char.lower() for char in word])

        if temp_word.issubset(row1) and not temp_word.issubset(row2) and not temp_word.issubset(row3):
            final.append(word)
        elif not temp_word.issubset(row1) and temp_word.issubset(row2) and not temp_word.issubset(row3):
            final.append(word)
        elif not temp_word.issubset(row1) and not temp_word.issubset(row2) and temp_word.issubset(row3):
            final.append(word)
    
    return final

print(findWords(["Hello","Alaska","Dad","Peace"]))