# Write a function to return a list of the first n numbers in the Fibonacci string.

def fibonacci_list(n):
  if n == 0:
    return [0]
  
  f0 = 1
  f1 = 1
  list = [0, f0, f1]
  for index in range (3, n):
    current = f1 + f0
    f0 = f1
    f1 = current
    list.append(current)
  return list

print(fibonacci_list(5))
print(fibonacci_list(12))
print(fibonacci_list(24))
