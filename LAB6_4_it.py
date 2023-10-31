import random


def generate_list():
    b = []
    for k in range(22):
        b.append(random.randint(-40, 50))
    return b


def min_in_array(lst):
    i = 0
    lst_min = lst[0]
    while i < len(lst):
        if lst[i] < lst_min:
            lst_min = lst[i]
        i += 1
    return lst_min


def first_positive_index(lst):
    i = 0
    while i < len(lst):
        if lst[i] > 0:
            return i
        else:
            i += 1
    return None


def last_positive_index(lst):
    i = len(lst) - 1
    while i >= 0:
        if lst[i] > 0:
            return i
        else:
            i -= 1
    return None


def sum_between(lst, i, j):
    if i is None or j is None:
        return 0
    else:
        s = 0
        while i < j - 1:
            s += lst[i + 1]
            i += 1
        return s


def replace_nulls(lst):
    i = 0
    while i < len(lst):
        if lst[i] == 0:
            lst.insert(0, lst.pop(i))
        i += 1
    return lst


if __name__ == '__main__':
    a = generate_list()
    print(a)
    print('Мінімальний елемент: ', min_in_array(a))
    print("Сума: ", sum_between(a, first_positive_index(a), last_positive_index(a)))
    print(replace_nulls(a))
