import datetime
# input函数
# input函数用于接收用户输入，返回值为字符串类型
# 语法：input([提示信息])
# 提示信息可选，如果不提供，则默认提示用户输入
# input函数会将用户输入的内容作为字符串返回


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
