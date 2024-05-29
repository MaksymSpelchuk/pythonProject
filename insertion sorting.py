def insertion_sort(list):
    for ind in range(1, len(list)):
        current_value = list[ind]
        position = ind - 1
        while position >= 0 and current_value < list[position]:
            list[position + 1] = list[position]
            position -= 1
        list[position + 1] = current_value

'''
list = [12, 11, 13, 5, 6]
print("Невідсортований масив:", list)
insertion_sort(list)
print("Відсортований масив:", list)
'''


