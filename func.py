def new_list(lst):
    max_index = 0
    max_elem = lst[0]
    for i in range(len(lst)):
        if lst[i] > max_elem:
            max_elem = lst[i]
            max_index = i
    for i in range(max_index + 1, len(lst)):
        lst[i] -= 1


numbers = [3, 5, 2, 7, 4, 6]
new_list(numbers)
print(numbers)
