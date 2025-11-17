# Find The greatest common divisor of multiple numbers read from the console.

def gcd(a, b):
  a = int(a)
  b = int(b)
  if b == 0:
    return a
  return gcd(b, a % b)

numbers_string = input()
numbers = numbers_string.split(" ")
divisor = gcd(numbers[0], numbers[1])

for index in range(2, len(numbers)):
  divisor = gcd(divisor, numbers[index])
print(divisor)
