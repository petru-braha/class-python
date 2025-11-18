# Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists. Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.

# Fastest possible solution: iterate over all numbers only once
# @param target_count >= 1
# @param lists - non-empty, non-empty sub-lists
# @return empty list for no optimum
def optimal_list(target_count, *lists):
  visited_lists_map = dict()
  ready_lists_map = dict()
  value_lists_map = dict()
  value_indexes_map = dict()
  
  # for each element of each input list  
  for index_input_list in range(0, len(lists)):
    # memorize for each list the its unique elements
    visited_lists_map[index_input_list] = set()

    # memorize for each list the elements that met their frequency requirement
    ready_lists_map[index_input_list] = set()
    
    # each value stores:
    # - value_lists_map[value] = a list of input list indexes
    #   - the frequency of the value is the length of this list
    #   - the first element of this is the first list in which the value exists
    #   - the 2nd element of this - the 2nd list in which the value exists
    # - value_indexes_map[value] = a (helper) dict
    #   - points the input list index to the internal list index
    #   - useful when retrieving other elements from the same list
    list = lists[index_input_list]
    for value in list:
      # initialization, value never seen before
      if value not in value_lists_map:
        value_lists_map[value] = [index_input_list]
        value_indexes_map[value] = {index_input_list: 0}
        # MARK as visited in the current list
        visited_lists_map[index_input_list].add(value)
        continue
          
      list_indexes = value_lists_map[value]
      dict_lists = value_indexes_map[value]

      list_indexes.append(index_input_list)
      frequency = len(list_indexes)

      # if the value was seen before in the same list,
      # increase the frequency, leave dict to point to the first occurence
      if dict_lists.get(index_input_list) != None:
        # observe that index_input_list == last element added
        dict_lists[index_input_list] = frequency - 1

      # MARK as visited in the current list
      visited_lists_map[index_input_list].add(value)
      
      index_potential = frequency - target_count
      if index_potential < 0:
        continue

      # frequency >= target_count
      index_containing_list = list_indexes[index_potential]
      ready_lists_map[index_containing_list].add(value)
      length_ready = len(ready_lists_map[index_containing_list])
      length_original = len(visited_lists_map[index_containing_list])
      if length_ready == length_original:
          return lists[index_containing_list]
  return []

print(optimal_list(2, [1, 2], [5, 6], [1, 3])) # []
print(optimal_list(2, [1, 2], [3, 5], [6, 5], [3, 2])) # [3, 5]
print(optimal_list(3, [1, 2], [3, 5, 1], [3, 5, 2], [1, 2])) # [1, 2]
print(optimal_list(2, [0, 1], [1, 2], [1, 3], [0, 1])) # [0, 1]
