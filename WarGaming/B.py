number = int(input())
input_price = list(map(int, input().split(" ")))


def numb_price(gold: int, price: list):
    number_price = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    output_price = dict(zip(number_price, price))
    tmp_min = min(price)
    tmp_max = []
    tmp = []

    for key in output_price:
        if output_price[key] == 0:
            pass
        else:
            if (gold // output_price[key]) * str(key) == '':
                pass
            else:
                tmp.append((gold // output_price[key]) * str(key))
            if output_price[key] == tmp_min:
                tmp_max.append(key)
    if tmp_min == 0 or gold == 0:
        pass
    else:
        if (gold // tmp_min) < 1:
            return 1
        tmp.append(int((gold // tmp_min) * str(max(tmp_max))))
        return max(map(int, tmp))


print(numb_price(number, input_price))
