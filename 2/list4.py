phrase = "don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(4):
    plist.pop()
#按索引删除，返回，默认最后一个
plist.pop()
#取对应的值
plist.remove("'")
#取对象列表
plist.extend([plist.pop(),plist.pop()])
#插入指定位置
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
