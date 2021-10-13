from collections import OrderedDict

commodities = OrderedDict()

for _ in range(int(input())):
    item, number = input().rsplit(maxsplit=1)
    commodities[item] = commodities.get(item, 0 ) + int(number)

for item,quantity in commodities.items():
    print(item,quantity)