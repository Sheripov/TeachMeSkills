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
    result: list = list((gold // tmp_min) * str(max(tmp_max)))
    sum = len(result) * output_price[max(tmp_max)]
    for index, value in enumerate(result):
        for j in range(9, 0, -1):
            if (sum - output_price[max(tmp_max)]) + output_price[j] <= gold:
                result[index] = j
                sum = (sum - output_price[max(tmp_max)]) + output_price[j]
                break
    return "".join(map(str, result))


print(numb_price(number, input_price))

