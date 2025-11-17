# Write a script that receives two strings and prints the number of occurrences of the first string in the second.

def count_needle_occurences(needle, haystack):
  count = 0
  
  for index_haystack in range(0, len(haystack)):
    if index_haystack + len(needle) > len(haystack):
      break

    if needle[0] != haystack[index_haystack]:
      continue

    # the first character matched
    index_needle = 1
    while index_needle < len(needle):
      if needle[index_needle] != haystack[index_haystack + index_needle]:
        break
      index_needle += 1
    
    if index_needle == len(needle):
      count += 1
  return count

first_string = input("first string: ")
second_string = input("second string: ")

print(count_needle_occurences(first_string, second_string))
