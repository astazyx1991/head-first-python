
fruits = {}

if 'apple' in fruits:
    filter['apple'] += 1
else:
    filter['apple'] = 0

if 'origin' not in fruits:
    fruits['origin'] = 0
fruits['origin'] += 1

fruits.setdefault('others', 0)

