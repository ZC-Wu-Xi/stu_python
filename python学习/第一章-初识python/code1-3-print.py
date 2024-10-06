# print()函数：输出/打印指定内容

# 任务一：打印字符串 我是nya~
# print(我是shio~)  # 报错，因为字符串需要用引号括起来
print("我是shio~")

# 任务二：打印数字2024
print(2024)

# 任务三：打印变量 创建一个变量year，值为2024，打印这个变量的值
year = 2024
print(year)  # 打印变量的值2024

# 任务四：一行中打印多个内容
'''
想要在一行中打印多个内容，可以在print()函数中使用逗号隔开多个内容
变量、数字、字符串都可以
注意使用英文的逗号
'''
print("今年是", year, "年，我要减肥")  # 打印多个内容，默认用空格隔开

# 任务五：打印多个内容，指定分隔符和结尾字符
'''
print()函数的参数：
print(*objects, sep=' ', end='\n', file=none, flush=False)
    *objects:表示可以接受多个字符串，用逗号隔开，也可以接受一个字符串列表
    sep:表示多个字符串之间的分隔符，默认为一个空格
    end:表示结尾的字符，默认为一个换行符
    file:表示输出位置，默认为标准输出，即屏幕
    flush:表示是否立即把内容输出到file中，默认为False
'''
print("hello", "world", sep=" ", end="!")
print("今年是", year, "年，我要减肥", sep="", end="\n\n")  # 打印多个内容，参数间用逗号隔开 指定分隔符为无
print("今年是", year, "年，我要读100本书", sep="", end="\n\n")
print("今年是", year, "年，我要去10个城市旅游", sep="", end="\n\n")

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