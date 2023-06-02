def minimum(arr):
    min_value = arr[0]
    for i in arr:
        if min_value > i:
            min_value = i
    return min_value


def maximum(arr):
    max_value = arr[0]
    for i in arr:
        if max_value < i:
            max_value = i
    return max_value
