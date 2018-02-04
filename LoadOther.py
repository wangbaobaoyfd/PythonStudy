# coding=utf-8

# 引入其他文件的类
# 第一种引入方法
# import FirstWork
# 第二种引入方法
from FirstWork import SecondTest

S=FirstWork.SecondTest("LoadOtherClass")
S.SayFirst()
S.SaySecond()