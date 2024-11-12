def apply_all_func(int_list, *functions):
    result = dict()
    for func in functions:
        meaning = func(int_list)
        result[func.__name__] = meaning
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
