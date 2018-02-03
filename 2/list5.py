#假复制
first = [1,2,3,4,5,6]
print(first)
second = first
print(second)

second.append(6)
print(second)
print(first)


#真复制
third = second.copy()

print(third)

second.append(10)
print(second)
print(third)



