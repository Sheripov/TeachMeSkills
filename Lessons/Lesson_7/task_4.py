def print_list(*args):
    return sum(args), max(args)


print(print_list(2, 3, 3, 3, 7))
