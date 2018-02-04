# coding=utf-8
__author__ = "sada"
print ("hello world")

x=1
y=2
z=x+y
print (z)

#判断
score=90
if score>=90:
    print ("您真棒")
    print ("优秀")
elif score>=80:
    print ("良好")
elif score>=60:
    print ("及格")


# 循环
for i in range(0,3):
    print (i)
    print ("Index {0} {1}".format(i,"cnblogs"))
print ("end")


# 函数定义
def HelloCNBlogs():
    print ("Hello CNBlogs")
def GetMax(x,y):
    if x>y:
        return x
    else:
        return y


# 类
HelloCNBlogs()
print (GetMax(9,13))

class FirstTest:
    def __init__(self,name):
        self._name=name;
    def SayFirst(self):
        print ("Class Test : Hello {0}".format(self._name))
F=FirstTest("FirstClass")
F.SayFirst()
print ("--------------------------------------------------")


#继承
class SecondTest(FirstTest):
    def __init__(self,name):
        FirstTest.__init__(self,name)
    def SaySecond(self):
        print ("Extend Class Test : {0}".format(self._name))

S=SecondTest("SecondTest")
S.SayFirst()
S.SaySecond()
print ("--------------------------------------------------")