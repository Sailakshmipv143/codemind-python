string=input().split()
vowel_count=[sum(char.lower()in 'aeiou'for char in word)for word in string]
max_vowels=max(vowel_count)
word_count=vowel_count.count(max_vowels)
print(word_count)