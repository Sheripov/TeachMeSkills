x = int(input("Input number a: "))
y = int(input("Input number b: "))
print(f"|{x}| - |{y}|")
print(f"------------- = {(abs(x) - abs(y)) / (1 + abs(x * y))}")
print(f"1 + |{x}*{y}|")
