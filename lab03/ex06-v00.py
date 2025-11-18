# Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists. Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.

LIST_OF_INPUT_INDEX = 0
DICT_INPUT_ORDER = 1

# we check the frequency of the other processed values
# checks if the neighbours for a give value (in a given list) have frequencies greater of equal than the target
def check_neighbours(target_count, hash_map, index_containing_list, processed_elements):
  for processed in processed_elements:
    list_indexes = hash_map[processed][LIST_OF_INPUT_INDEX]
    dict_lists = hash_map[processed][DICT_INPUT_ORDER]

    index_internal_processed = dict_lists[index_containing_list]
    element_frequency = len(list_indexes) - index_internal_processed

    if (element_frequency < target_count):
      return False
  return True

# visits all the input lists with valid frequency for the given value
# ideally for a given value this function iterates once
def check_frequency(target_count, hash_map, value, processed_elements):
  """
  returns the index of a optimal list, or -1 otherwise 
  """
  frequency = len(hash_map[value][LIST_OF_INPUT_INDEX])
  for index_internal_list in range(frequency - target_count + 1):
    index_containing_list = hash_map[value][LIST_OF_INPUT_INDEX][index_internal_list]

    if check_neighbours(target_count, hash_map, index_containing_list, processed_elements) == True:
      return index_containing_list
  return -1

# Assumes target_count >= 1
def optimal_list(target_count, *lists):
  """
  returns empty list if no optimum was found
  """
  hash_map = dict()
  if target_count == 1:
    return lists[0]
  
  # for each element of each input list  
  for index_input_list in range(0, len(lists)):
    list = lists[index_input_list]
    processed_elements = []
    
    # each value will store its containing input lists
    # hash_map[value] stores a tuple of:
    # - a list of input list indexes
    #   - the frequency of the value is the length of this list
    #   - the first element of the list is the first list in wich the element appeared
    #   - the second element - the second containing list and so on ...
    # - a (helper) dict pointing the input list index to the internal list index
    #   - useful when retrieving other elements from the same list in constant time
    for value in list:
      if value not in hash_map:
        # initialization of the record
        hash_map[value] = [[index_input_list], {index_input_list: 0}]
        continue

      list_indexes = hash_map[value][LIST_OF_INPUT_INDEX]
      dict_lists = hash_map[value][DICT_INPUT_ORDER]

      # update of the record
      list_indexes.append(index_input_list)
      # observe that index_input_list == last element added
      frequency = len(list_indexes)
      dict_lists[index_input_list] = frequency - 1

      idx = check_frequency(target_count, hash_map, value, processed_elements)
      if idx != -1:
        return lists[idx]

      processed_elements.append(value)
  return []

print(optimal_list(2, [1, 2], [5, 6], [1, 3])) # [1, 2]
print(optimal_list(2, [1, 2], [3, 5], [6, 5], [3, 2])) # [3, 5]
print(optimal_list(3, [1, 2], [3, 5, 1], [3, 5, 2], [1, 2])) # [1, 2]

# do not consider first valid: 3 [1, 2] [2, 3] [2, 3]