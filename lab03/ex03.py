# Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)

def contingent_sets(a, b):
  first_set = set(a)
  second_set = set(b)

  difference0 = first_set - second_set
  difference1 = second_set - first_set

  intersection = first_set - difference0

  for element in second_set:
    first_set.add(element)
  return (intersection, first_set, difference0, difference1)

print(contingent_sets([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
