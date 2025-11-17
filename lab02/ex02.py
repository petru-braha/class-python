# Write a script that calculates how many vowels are in a string.

vowels = "aeiou"
def count_vowels(string):
  count = 0
  for character in string:
    if character in vowels:
      count += 1
  return count

print(count_vowels("aeiou"))
print(count_vowels("gigi"))
print(count_vowels("portocale"))
