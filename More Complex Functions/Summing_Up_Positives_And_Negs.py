# my version

def count_positives_sum_negatives(arr):
    pos = len([i for i in arr if i > 0])
    neg = sum([i for i in arr if i < 0])
    if arr == []:
        return []
    elif [pos,neg] == [0, 0]:
        return [0, 0]
    else:
        return [pos,neg]
