string=input().split()
vowel_count=[sum(char.lower() in'aeiou' for char in word)for word in string]
min_vowels=min(vowel_count)
print(min_vowels)