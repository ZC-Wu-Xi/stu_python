# 1. 初识 python

### 1-1 第一个程序

```python
# 打印数字(块注释)
print(11)  # 行内注释 与代码同行，#前面至少有两个空格

# 打印字符 不区分单双引号
print("hello world")
print('hello world')
```

### 1-2 注释

- 作用：方便阅读代码时，能够快速的了解代码的功能，不会被执行。
- 分类：
  - 块注释
  - 行内注释
  - 多行注释
- 使用规范：
  1. 注释不是越多越好，对于一目了然的代码，不需要添加注释
  2. 对于复杂的操作，应该在操作开始前写上若干行注释
  3. 对于不是一目了然的代码，应在其行尾添加注释
  4. 绝不要描述代码，假设阅读代码的人比你更懂Python，他只是不知道你的代码要做什么

```python
# 块注释
# 我是一行注释
print(111)

# 行内注释
print(111)  # 我是行内注释  与代码同行，建议前面至少有两个空格

# 多行注释 不区分单双引号
"""
我是多行注释
我是多行注释
"""

'''
我也是多行注释
我也是多行注释
'''
```

**块注释：**

- 以`#`开始，一直到本行结束都是注释
- 为了保证代码的可读性，**`#`后面建议先添加一个空格**，然后再编写相应的说明文字(PEP8)
- 注释不会运行
- 代码是给机器执行用的，注释是给人看的，方便阅读代码时，能够快速的了解代码的功能

**行内注释：**

- 以#开始，一直到本行结束都是注释
- **与代码写在同一行**
- **`#`前面至少有两个空格**

**多行注释：**

- 如果希望编写的注释信息很多，一行无法显示，就可以使用多行注释
- 要在python程序中使用多行注释，可以用**一对连续的三个引号**（单引号和双引号都可以)

### 1-3 print()

`print()`函数：`print(*objects, sep=' ', end='\n', file=none, flush=False)`

- `*objects`:表示可以接受多个字符串，用逗号隔开，也可以接受一个字符串列表
- `sep`:表示多个字符串之间的分隔符，默认为一个空格
- `end`:表示结尾的字符，默认为一个换行符
- `file`:表示输出位置，默认为标准输出，即屏幕
- `flush`:表示是否立即把内容输出到file中，默认为False

#### 简单的打印

```python
# 任务一：打印字符串 我是nya~
# print(我是shio~)  # 报错，因为字符串需要用引号括起来
print("我是shio~")

# 任务二：打印数字2024
print(2024)

# 任务三：打印变量 创建一个变量year，值为2024，打印这个变量的值
year = 2024
print(year)  # 打印变量的值2024
```

#### 多个内容的打印

```python
# 任务四：一行中打印多个内容
'''
想要在一行中打印多个内容，可以在print()函数中使用逗号隔开多个内容
变量、数字、字符串都可以
注意使用英文的逗号
'''
print("今年是", year, "年，我要减肥")  # 打印多个内容，默认用空格隔开

# 任务五：打印多个内容，指定分隔符和结尾字符
print("hello", "world", sep=" ", end="!")
print("今年是", year, "年，我要减肥", sep="", end="\n\n")  # 打印多个内容，参数间用逗号隔开 指定分隔符为无
print("今年是", year, "年，我要读100本书", sep="", end="\n\n")
print("今年是", year, "年，我要去10个城市旅游", sep="", end="\n\n")
```

#### 格式化输出打印

> 1. `%`格式化操作符方式格式化打印
> 2. `format()`指定格式输出打印

```python
# 任务六：格式化输出
year = 2024
month = 2
day = 20
week = '一'
weather = '晴'
temp = 19.5
# 使用%格式化输出
print("今天是%d年%2d月%d日，星期%s，天气%s，温度%.1f℃。" % (year, month, day, week, weather, temp))
print("今天是%d年%02d月%d日，星期%s，天气%s，温度%.1f℃。" % (year, month, day, week, weather, temp))
# 使用format()函数格式化输出
print("今天是{}年{}月{}日，星期{}，天气{}，温度{}℃。".format(year, month, day, week, weather, temp))
# format指定格式输出  # {0}表示第一个参数，{1:02d}表示第二个参数，保留两位数，不足两位前面补0，..., {5:.1f}表示第六个参数，保留一位小数
print("今天是{0}年{1:02d}月{2}日，星期{3}，天气{4}，温度{5:.1f}℃。"
      .format(year, month, day, week, weather, temp))
```

控制台:

```shell
今天是2024年 2月20日，星期一，天气晴，温度19.5℃。
今天是2024年02月20日，星期一，天气晴，温度19.5℃。
今天是2024年2月20日，星期一，天气晴，温度19.5℃。
今天是2024年02月20日，星期一，天气晴，温度19.5℃。
```

**`%`格式化操作符方式格式化打印：**

`print("格式化字符串" % (变量1， 变量2...))`

- 如果希望输出文字信息的同时，一起输出数据，就需要使用到格式化操作符
- `%`被称为格式化操作符，专门用于处理字符串中的格式
  - 包含`%`的字符串，被称为格式化字符串
  - `%`和不同的`字符`连用，不同类型的数据需要使用不同的格式化字符

| 格式化字符 | 含义                                                         |
| ---------- | ------------------------------------------------------------ |
| `%s`       | 字符串                                                       |
| `%d`       | 有符号十进制整数，`%06d`表示输出整数显示的位数`6`，不足的地方使用`0`补全 |
| `%f`       | 浮点数，`%2f` 表示小数点后只显示两位                         |
| `%%`       | 输出`%                                                       |

**`format()`指定格式输出打印：**

`format()`指定格式输出，使用{}进行占位，也可以进行格式限制

- 如：`{1:02d}`表示第二个参数保留两位数，不足两位前面补0

### 1-4 input()

input函数

- `input()`函数用于接收用户输入，**返回值为字符串类型**
- 语法：`input([提示信息])`
- `提示信息`可选，如果不提供，则默认提示用户输入
- input函数会将用户输入的内容作为字符串返回s

```python
import datetime
# 任务1：创建变量name,保存用户输入的名字;打印变量name
name = input("请输入您的名字：")  # input函数会将用户输入的内容作为字符串返回
type(name)  # <class 'str'> input()返回值为字符串类型
print("您的名字是：", name)

# 任务2：
# 创建变量age,保存用户输入的年龄；打印用户的出生年份
age = int(input("请输入您的年龄："))
type(age)  # <class 'int'> input()返回值为字符串类型，需要使用int()函数将字符串转换为整数
birth_year = datetime.datetime.now().year - age
print("您的出生年份是：", birth_year)
```

### 1-5 案例：个人名片

```python
# 在控制台依次提示用户输入：姓名、公司、职位、电话、邮箱
name = input("请输入姓名：")
company = input("请输入公司：")
job = input("请输入职位：")
phone = input("请输入电话：")
email = input("请输入邮箱：")
# 打印分隔线
print("------------------------------------------------")
# 打印个人名片
print("姓名：", name)
print("公司：%s" % company)
print("职位：", job)
print("电话：", phone)
print("邮箱：", email)
# 打印分隔线
print("------------------------------------------------")
```

