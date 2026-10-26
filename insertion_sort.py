def insertion_sort_decreasing(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift smaller elements to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j = j - 1

        # Place the key in its correct position
        arr[j + 1] = key
        
    return arr    