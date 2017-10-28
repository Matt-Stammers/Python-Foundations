'''
How to sum all the items that appear only once in a list

This can be achieved by any combination of the following. The best solution involves importing collections
'''

import collections
def repeats(arr):
  unique_array = [item for item, count in collections.Counter(arr).items() if count < 2]
  return sum(unique_array)
  
from collections import Counter
def repeats(arr):
    return sum(k for k, v in Counter(arr).items() if v == 1)
    
def repeats(arr):
    return sum(filter(lambda num : arr.count(num) == 1, arr))
    
def repeats(s):
    numbers = set()
    for number in s:
        if number in numbers:
            numbers.remove(number)
        else:
            numbers.add(number)
    return sum(numbers)
    
def repeats(arr):
    return sum([a for a in arr if arr.count(a) == 1])
