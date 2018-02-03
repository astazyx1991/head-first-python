a = set("reawgfwreq")

print(type(a))



vowels = set("aeiou")
word = "hello"
#并
u = vowels.union(set(word))
print(u)

v = vowels.difference(set(word))
print(v)

w = vowels.intersection(set(word))
print(w)

