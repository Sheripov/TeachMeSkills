def print_list(*args):
    result_sum = 0
    for i, v in enumerate(args):
        print(i, v)
        result_sum += i * v
    return result_sum


print(print_list(2))
