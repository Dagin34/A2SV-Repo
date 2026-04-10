def is_vowel(char):
    return char in "aeiou"

s = str(input().strip())
t = str(input().strip())

if len(s) != len(t) or not s or not t: 
    print("No")
    exit()

for i in range(len(s)):
    if is_vowel(s[i]) != is_vowel(t[i]):
        print("No")
        exit()

print("Yes")


# def has_vowel(ss):
#     vowels = consonants = 0
#     for char in ss:
#         if char in 'aeiouAEIOU': vowels += 1
#         else: consonants += 1

#     return vowels, consonants

# s = str(input().strip())
# t = str(input().strip())

# s_vowels, s_cons = has_vowel(s)
# t_vowels, t_cons = has_vowel(t)

# if len(s) != len(t) or not s or not t: 
#     print("No")
#     exit()

# if (s_vowels == t_vowels) and (s_cons == t_cons): print("Yes")
# else: print("No")