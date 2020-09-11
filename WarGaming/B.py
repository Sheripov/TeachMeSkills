number = int(input())
input_price = list(map(int, input().split(" ")))


def numb_price(gold: int, price: list):
    number_price = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    output_price = dict(zip(number_price, input_price))
    tmp_min = min(price)
    tmp_max = []
    for key in output_price:
        if output_price[key] == tmp_min:
            tmp_max.append(key)
    try:
        if (gold // tmp_min) < 1:
            return -1
    except ZeroDivisionError:
        return -1
    return (gold // tmp_min) * str(max(tmp_max))


print(numb_price(number, input_price))
