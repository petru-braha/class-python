# Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be recursively covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

NOT_PRIMITIVES = ["list", "tuple", "set", "frozenset", "dict", "dict_values"]

def get_data_type(a):
  type_string = str(type(a))
  return type_string[8:len(type_string) - 2]

def is_primitive(a):
  if get_data_type(a) in NOT_PRIMITIVES:
    return False
  return True

# declare the function first and define it below
def compare_dict(a, b):
  pass

def compare_objects(a, b):
  if type(a) != type(b):
    return False
  
  if is_primitive(a):
    return a == b
  
  if len(a) != len(b):
    return False
  
  data_type_a = get_data_type(a)
  if data_type_a == "dict":
    return compare_dict(a, b)
  
  # we know they are of equal length, issuperset returns if they are equal
  if data_type_a.endswith("set"):
    return a.issuperset(b)
  
  for index in range(len(a)):
    if compare_objects(a[index], b[index]) == False:
      return False

def compare_dict(a, b):
  if len(a) != len(b):
    return False
  for key, a_value in a.items():
    b_value = b.get(key)
    if b_value == None:
      return False
    if compare_objects(a_value, b_value) == False:
      return False
  return True

d1 = {
  "x": 1,
  "y": [1, 2, {"a": 3}],
  "z": {"u": {1, 2}}
}

d2 = {
  "x": 1,
  "y": [1, 2, {"a": 3}],
  "z": {"u": {2, 1}}
}

print(compare_dict(d1, d2)) # True


x = {
 "Dacia" : 120,
 "BMW" : 160,
 "Toyota" : 140,
 "Volvo" : 115,
 "Renault" : 120,
 }
for a in enumerate (x):
  print (a)
