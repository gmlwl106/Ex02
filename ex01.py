#list
print("리스트 기본=====================================")
tList = [1,2,"python"]
print(tList)
print(tList[0], tList[1], tList[2])
print(tList[-1], tList[-2])

ttList = tList[1:3]
print(tList[1:3])
print(tList)
print(ttList)

print(tList*2)
print(tList + [3,4,5])
print(len(tList))

print(2 in tList)

print("리스트 삭제=====================================")
#del(tList[0])
#del tList[0]
print(tList)

print("리스트 수정=====================================")
tList[0] = "일"
print(tList)

bList=['apple', 'banana', 10, 20]
bList[2] = bList[2] + 90

print(bList[2])

print("리스트 수정=====================================")
cList = [1, 12, 123, 1234]
cList[0:2] = [10,20]
print(cList)

print("리스트 수정=====================================")
dList = [1, 12, 123, 1234]
dList[1:2] = []
print(dList)

dList[0:2] = []
print(dList)

print("리스트 수정=====================================")
eList = [1, 12, 123, 1234]
#eList[1:2] = "a" #변경
eList[1:1] = "a" #같은 숫자이면 추가
print(eList)

eList[5:] = [12345]
print(eList)

eList[:0] = [12,-1,0]
print(eList)


print("리스트 함수=====================================")
a = [1, 12, 123, "hello", 3.14, 1000]
print(a)

a.append(5)
print(a)

a.insert(3, 1000)
print(a)

a.extend([6,7,8])
print(a)

#제거
a.remove(1000) #앞에것만 지운다
print(a)

a.pop(2)
print(a)

a.pop() #마지막 삭제
print(a)