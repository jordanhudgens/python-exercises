from functools import reduce

def get_sum(list):
    return reduce((lambda total, element: total + element), list)


total = get_sum([1, 2, 3, 4, 5, 6])

print(total)
