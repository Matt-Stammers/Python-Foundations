# my first version

def count_positives_sum_negatives(arr):
    pos = len([i for i in arr if i > 0])
    neg = sum([i for i in arr if i < 0])
    if arr == []:
        return []
    elif [pos,neg] == [0, 0]:
        return [0, 0]
    else:
        return [pos,neg]
    
# best way to do it

def count_positives_sum_negatives(arr):
    if not arr: return []
    pos = 0
    neg = 0
    for x in arr:
      if x > 0:
          pos += 1
      if x < 0:
          neg += x
    return [pos, neg]

# Clever one liner

def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []

# some other ways

def count_positives_sum_negatives(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

def count_positives_sum_negatives(arr):
  output = []
  if arr:
    output.append(sum([1 for x in arr if x > 0]))
    output.append(sum([x for x in arr if x < 0]))
  return output

def count_positives_sum_negatives(arr):
    #your code here
    res = []
    if arr:
        i = 0
        j = 0
        for num in arr:
            if num > 0:
                i = i+1
            else:
                j = num+j
        res = [i,j]  
    return res
