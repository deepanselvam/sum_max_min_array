def sum_of_max_and_min(arr):
    if not arr:
        return -1
    min_val = max_val = arr[0]  
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            max_val = arr[i]
        elif arr[i] < min_val:
            min_val = arr[i]

    return max_val+ min_val
A = list(map(int,input().split())) #applies int to each string element in the input
result = sum_of_max_and_min(A)
print(result)
