# 创建字符串
s = "hello world"
print(s[0])  # h
print(s[4])  # o
print(s[-1])  # d
# 字符串切片 包头不包尾
print('字符串切片')
print(s[0:4])  # hell 从索引0开始，到索引4结束，不包括索引4
print(s[1:4])  # ello 从索引1开始，到索引4结束，不包括索引4
print(s[:4])  # hell 从索引0开始，到索引4结束，不包括索引4
print(s[6:])  # world 从索引6开始，到字符串结束
print(s[:])  # hello world 从索引0开始，到字符串结束
# 步长
print('步长')
print(s[0:11])  # hello world 默认第三个值为1  从索引0开始，到索引10结束，每隔1个取一个字符
print(s[0:11:1])  # hello world 从索引0开始，到索引10结束，每隔2个取一个字符
print(s[0:11:2])  # hlowrd 从索引0开始，到索引10结束，每隔2个取一个字符
print(s[::2])  # hlowrd 从索引0开始，每隔2个取一个字符 到字符串结束

# 字符串反转
s2 = '1234567'
print(s2[-1:-10:-1])  # 7654321
print(s2[::-1])  # 7654321