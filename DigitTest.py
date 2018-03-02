# coding=utf-8

# 常量
import const
const.value=5
print(const.value)
# 在输出第一次输出const.value(结果是5)以后，就报错了。那是因为一个常量再一次被赋值了，所以就会报错。
#const.value=6


# 复合型
# complex()函数可以使用参数real + imag*j方式创建一个复数。也可以转换一个字符串的数字为复数；或者转换一个数字为复数。
# 如果第一个参数是字符串，第二个参数不用填写，会解释这个字符串且返回复数；不过，第二个参数不能输入字符串方式，否则会出错。
# real和imag参数可以输入数字，如果imag参数没有输入，默认它就是零值，这个函数就相当于int()或float()的功能。
# 如果real和imag参数都输入零，这个函数就返回0j。有了这个函数，就可以很方便地把一个列表转换为复数的形式。
# 注意：当想从一个字符串的复数形式转换复数时，需要注意的是在字符串中间不能出现空格，
# 比如写成complex(‘1+2j’)，而不是写成complex(‘1 +2j’)， 否则会返回ValueError异常。
print(complex(1))
print(complex('3+89j'))
array = [1, 2, 3, 5]
for i in array:
    print(complex(i))


# 字符串
dan='dan'
print(dan)
print("dan: {0}".format(dan))
#单引号中使用双引号，双引号会被当做字符串输出，但双引号中不可以这样使用双引号
dan1='Our "young"'
print("dan1: {0}".format(dan1))
# 三引号字符串："""hello"""或'''hello''' 注：三引号包含的字符串可由多行组成，一般可表示大段的叙述性字符串。在使用时基本没有差别，
# 但双引号和三引号（"""..."""）中可以包含单引号，三引号('''...''')可以包含双引号，而不需要转义
# 如果前面是三个单引号，后面也是三个单引号，需要前后对称，且三单引号或者三双引号的字符串输出时可以保持原格式
dan2='''Our
young
cool'''
print("dan2: {0}".format(dan2))
dan3="""Our
young
cool"""
print("dan3:  {0}".format(dan3))

# 转义
comment='I\'m young'
print(comment)
description="Our \nyoung"
print(description)


