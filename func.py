def new_list(lst):
    max_index = lst.index(max(lst))
    for i in range(max_index + 1, len(lst)):
        lst[i] -= 1


numbers = [3, 5, 2, 7, 4, 6]
new_list(numbers)
print(numbers)
