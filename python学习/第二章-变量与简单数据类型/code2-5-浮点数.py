# 浮点数的计算
n1 = 1.1
n2 = 2.2
print(n1 + n2)  # 3.30000000000000004

# 四舍五入方式进行保留精度
n3 = round(n1 + n2, 1)  # 保留一位小数
print(n3)  # 3.3

import math
print(math.floor(n3))  # 向下取整  3
print(math.ceil(n3))  # 向上取整  4