# 闰年判断：
year = int(input("请输入一个年份："))
if (not year % 4 and year % 100) or not year % 400:
    print('%d是闰年' % year)
else:
    print('%d不是闰年' % year)