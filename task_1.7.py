def list(list1, list2):
    return [j[i]
    for i in range(len(list2))
    for j in [list1, list2]]
      
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list(list1, list2))