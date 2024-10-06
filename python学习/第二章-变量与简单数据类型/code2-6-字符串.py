# 创建字符串
s1 = 'hello'
print(s1)
s2 = "world"
print(s2)
s3 = '''hello
world'''
print(s3)  # hello
           # world
s4 = "It's a hat"
print(s4)  # It's a hat

s5 = '1234\'\"666'  # 在字符串中使用\转义字符
print(s5)  # 1234'"666

print('------------------------')
# 字符串拼接
print(s1 + s2)  # helloworld
# 字符串与数字不能相加
# print(s1 + 1)  # TypeError: can only concatenate str (not "int") to str

# 字符串与字符串相乘
print(s1 * 5)  # hellohellohellohellohello