# 任务一：转换为整形int
# 字符串str-->整形int  纯数字的无小数字符串才可以转换
print('转化为字符串')
s = '2024'
print(type(int(s)))  # <class 'int'>
'''
s1 = 'aaa223'
print(type(int(s1)))  # ValueError: invalid literal for int() with base 10: 'aaa223'
s3 = '2.23'
print(type(int(s3)))  # ValueError: invalid literal for int() with base 10: '2.23'
'''
# 浮点数float-->整形int
f = 2.23
print(int(f))  # 2
print(type(int(f)))  # <class 'int'>
# 布尔值bool-->整形int
a, b = True, False
print(int(a), int(b))  # 1 0
print(type(int(a)))  # <class 'int'>

# 任务二：转换为浮点数float
print('转化为浮点数')
# 字符串str-->浮点数float
s = '2.23'
print(float(s))  # 2.23
print(type(float(s)))  # <class 'float'>
# 整形int-->浮点数float
i = 2
print(float(i))  # 2.0
print(type(float(i)))  # <class 'float'>
# 布尔值bool-->浮点数float
a, b = True, False
print(float(a), float(b))  # 1.0 0.0
print(type(float(a)))  # <class 'float'>

# 任务三：转换为布尔值bool
print('转化为布尔值')
# 字符串str-->布尔值bool
s = '2.23'
print(bool(s))  # True
print(type(bool(s)))  # <class 'bool'>
# 整形int-->布尔值bool
i = 0
print(bool(i))  # False
print(type(bool(i)))  # <class 'bool'>
# 浮点数float-->布尔值bool
f = 0.0
print(bool(f))  # False
print(type(bool(f)))  # <class 'bool'>
# 布尔值bool-->布尔值bool
a, b = True, False
print(bool(a), bool(b))  # True False
print(type(bool(a)))  # <class 'bool'>
# 空字符串-->布尔值bool
s = ''
print(bool(s))  # False
print(type(bool(s)))  # <class 'bool'>
# 空列表-->布尔值bool
l = []
print(bool(l))  # False
print(type(bool(l)))  # <class 'bool'>
# 空元组-->布尔值bool
t = ()
print(bool(t))  # False
print(type(bool(t)))  # <class 'bool'>
# 空字典-->布尔值bool
d = {}
print(bool(d))  # False
print(type(bool(d)))  # <class 'bool'>
# ...

# 任务四：转换为字符串str
print('转化为字符串')
# 整形int-->字符串str
i = 2
print(str(i))  # 2
print(type(str(i)))  # <class 'str'>
# 浮点数float-->字符串str
f = 2.23
print(str(f))  # 2.23
print(type(str(f)))  # <class 'str'>
# 布尔值bool-->字符串str
a, b = True, False
print(str(a), str(b))  # True False
print(type(str(a)))  # <class 'str'>
# 空列表-->字符串str
l = []
print(str(l))  # []
# ...

# 任务五：进制的转换
# 注意：在Python中，0b、0o、0x前缀表示二进制、八进制、十六进制
print('进制的转换')
# 其他进制转为十进制
print(int('0x1a', 16))  # 26 十六进制转十进制
print(int('0b11010', 2))  # 26 二进制转十进制
print(int('0o32', 8))  # 26 八进制转十进制

# 十进制转为其他进制
print(oct(26))  # 0o32 十进制转八进制
print(bin(26))  # 0b11010 十进制转二进制
print(hex(26))  # 0x1a 十进制转十六进制
