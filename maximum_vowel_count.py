string=input().split()
vowel_count=[sum(char.lower() in'aeiou'for char in word)for word in string]
max_vowels=max(vowel_count)
print(max_vowels)