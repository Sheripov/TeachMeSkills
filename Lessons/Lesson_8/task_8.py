from datetime import datetime


def decorat(func):
    def isdigit(*args):
        x = args[0]
        start_time = datetime.now()
        try:
            x = int(x)
            print(datetime.now() - start_time)
            return f'result: {x}'
        except ValueError:
            return "error input"
    return isdigit


@decorat
def sm_to_m(x):
    return x * 10


print(sm_to_m('10'))
