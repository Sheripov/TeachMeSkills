import sys
print(sys.argv)

res = 0

for i in sys.argv:
    if i.isdigit():
        res += int(i)

print(res)