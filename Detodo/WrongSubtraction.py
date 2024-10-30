num = [int(a) for a in input().split(" ")]
ram = num[0]
for i in range(num[1]):
    if ram % 10 == 0:
        ram = int(ram/10)
    else:
        ram = ram - 1
print(ram)
    