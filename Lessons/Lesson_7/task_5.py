def print_list(a, *args, **kwargs):
    print(args)
    print(kwargs)
    # eturn sum(args), max(args)


print(print_list(a=123, 3432, 3242))
