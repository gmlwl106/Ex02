#딕션어리

print("딕션어리 생성===========================")
a={}

a["r38"] = "빅데이타"
a["r32"] = "c언어"

print(a)

print("딕션어리 생성===========================")
d = {"야구":5, "축구":11, "농구":9}
print(d)

d["배구"] = 6
print(d)

del(d["축구"])
print(d)

print("딕션어리 생성===========================")
d = {"야구":5, "축구":11, "농구":9}
print(type(d), d)
print(len(d))
print("야구" in d)
print("배구" in d)
print("배구" not in d)

print(d.get("축구"))

del(d["야구"])
print(d)

d = {}
print(d)

d = {"야구":5, "축구":11, "농구":9}
keys = d.keys()
print(keys)
print(type(keys))

for key in keys:
    print(key, d[key])
    print("{0}:{1}".format(key, d[key]))