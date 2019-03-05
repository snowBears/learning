# _*_ coding:utf-8 _*_
# def fun (x):
#     print(x)
# s = input("请输入字符：")
# print(fun(s))

# a = "6"
# b = "7"
# c = a + b
# print(c)

# str = """今天好p
# 今天好难，
# 井好。
# """
# print(str)


classmate = ["snow", "hello", "sun"]
classmate.append("moon")
classmate.insert(1, "star")
classmate.pop(3)
classmate[2] = 1
print(classmate)


print(classmate[2:])
# r = []
# n = 3
# for i  in range(n):
#     r.append(classmate[i])
# print(r)



# sum = 0
# n = 1
# while  n < 100:
#     sum = sum + n
#     n = n +2
# print(sum)
#

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# 切片
def trim(s):
    i = 1
    j = 1
    while i < len(s):
       if s[:i] == "":
           i += 1
       else:
           i -= 1
           break
    while j < len(s):
        if s[-j:] == "":
            j += 1
        else:
            j -= 1
            break
    return s[i:len(s)-j]
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

# 迭代，for循环
for i in "abf":
    print(i)

from collections import Iterable
print(isinstance("123", Iterable))

for i, j in enumerate(["A", "b", "v"]):
    print(i, j)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 列表生成式
print([x*x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in "ACD" for n in "XYW"])

# 生成器
g =  (x*x for x in range(1,11))
for n in g:
    print(n)