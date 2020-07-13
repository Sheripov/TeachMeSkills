# while True:
#     name = []
#     inp = input()
#     if inp == 'q':
#         break
#     name.append(inp)
# for i in name:
#     print(i)
#     #if i.startswith('p'):
#
pupils = [
    {
        'firstname': 'Masha',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
    },
    {
        'firstname': 'Vasya',
        'Group': 42,
        'physics': 3,
        'informatics': 8,
        'history': 1,
    },
    {
        'firstname': 'Dasha',
        'Group': 42,
        'physics': 5,
        'informatics': 2,
        'history': 2,
    },
]
for i in pupils:
    # avg = (i['physics'] + i['informatics'] + i['history']) / 3
    # if avg > 4:
    #     print(i)
    avg = 0
    count = 0
    for j in i.keys():
        if j not in ['firstname', 'Group']:
            avg += i[j]
            count += 1
    avg = avg / count
    if avg > 4:
        print(i)
