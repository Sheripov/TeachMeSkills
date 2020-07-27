def my_name(name):
    return f'Hello {name}!'


list_name = []
for i in range(5):
    list_name.append(input('Print name: '))
for j in list_name:
    print(my_name(j))
