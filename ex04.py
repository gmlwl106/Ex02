#셋
print("셋 생성=====================================")
a = {1,2,3}
print(a, type(a))
print(len(a))
print(2 in a)
print(2 not in a)

print("셋 메소드=====================================")
a.add(4)
a.add(1)
a.discard(100) #discard 값이 없어도 에러발생x
#a.remove(3) #remove 값이 없으면 에러발생
a.update({2, 1000})
print(a)

print("셋 메소드=====================================")
s1 = set([1,2,3,4,5,6,7,8,9,10])
s2 = set([10,20,30])
print(type(s1), type(s2))

s3 = s1.union(s2)
#s3 = s1 | s2
print(s3)

s4 = s1.intersection(s2)
#s4 = s1 & s2
print(s4)

s5 = s1.difference(s2)
#s5 = s1 - s2
print(s5)