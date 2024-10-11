# 逻辑运算符
# | 运算符 | 逻辑表达式 | 描述                                                         |
# | ------ | ---------- | ------------------------------------------------------------ |
# | `and`  | ` x and y` | 只有×和y 的值都为 True，才会返回 True否则只要×或者y有一个值为 False，就返回False |
# | `or`   | `x or y`   | 只要×或者y有一个值为True，就返 回 True 只有×和y的值都为 False， 才会返回False |
# | `not`  | `not x`    | 如果×为 True，返回 False 如果× 为 False，返回True            |

# and 运算符，只要有一个为False，结果就是False
# python中and运算符 两个值如果前面的值是false就返回前面的值，前面的值为false后面的值为true就返回后面的值
print(1 and 2)  # 2 True and True
print(1 and 0)  # 0 True and False
print(0 and 1)  # 0 False and True
print(0 and 0)  # 0 False and False
print(True and False)  # False
print('' and 'hi')  # ''
print('hi' and 'hello')  # hello

# or 运算符，只要有一个为True，结果就是True
# python中or运算符 两个值如果前面的值是true就返回前面的值，前面的值为false后面的值为true就返回后面的值
print(1 or 2)  # 1 True or True
print(1 or 0)  # 1 True or False
print(0 or 1)  # 1 False or True
print(0 or 0)  # 0 False or False
print(True or False)  # True
print('' or 'hi')  # hi
print('hi' or 'hello')  # hi


# not 运算符，取反
print(not True)  # False
print(not False)  # True
print(not 1)  # False
print(not 0)  # True
print(not '')  # True
print(not 'hi')  # False

# 优先级 not > and > or
print(True and False and not False)  # False 即 True and False and True