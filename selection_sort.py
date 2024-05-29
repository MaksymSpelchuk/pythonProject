def selection_sort(num_list):
    n = len(num_list)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if num_list[j] < num_list[min_index]:
                min_index = j
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]

'''
num_list = [12, 11, 13, 5, 6]
print("Невідсортований масив:",num_list)
selection_sort(num_list)
print("Відсортований масив:", num_list)
'''