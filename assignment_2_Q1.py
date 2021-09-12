def last_val(n): return n[-1]

def sort_list_(tuples_val):
  return sorted(tuples_val, key=last_val)

Sample_List =[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sort_list_(Sample_List))