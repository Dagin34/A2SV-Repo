def uniqueMorseRepresentations(words: list[str]) -> int:
    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    transformations = []

    for word in words:
        ascii_values = [ord(char.lower()) for char in word]
        new_word = ''.join([morse_code[val - 97] for val in ascii_values])
        transformations.append(new_word)

    return len(set(transformations))

print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))