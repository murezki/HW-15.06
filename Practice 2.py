def modify_array(arr):
    positive_sum = sum(x for x in arr if x > 0)
    negative_sum = sum(x for x in arr if x < 0)
    diff = abs(positive_sum) - abs(negative_sum)
    if diff == 0:
        return arr
    elif diff > 0:
        arr.append(-diff)
    else:
        arr.append(abs(diff))
    return arr


arr = [-3, -2, 1, 2, 3, 4]
print(arr)
positive_sum = sum(x for x in arr if x > 0)
negative_sum = sum(x for x in arr if x < 0)
print(positive_sum)
print(negative_sum)
if abs(positive_sum) > abs(negative_sum):
    print(abs(positive_sum) - abs(negative_sum))
    arr = modify_array(arr)
    print(arr)
elif abs(positive_sum) < abs(negative_sum):
    print(abs(negative_sum) - abs(positive_sum))
    arr = modify_array(arr)
    print(arr)