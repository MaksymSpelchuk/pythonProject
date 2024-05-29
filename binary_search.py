def binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

'''
arr = [2, 3, 4, 10, 40]
    target = 10
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Елемент знайдено на індексі {result}")
    else:
        print("Елемент не знайдено в масиві")
'''