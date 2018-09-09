# def   test(x,y,z=2):
#     print(x)
#     print(y)
# test(1,2)
#args:接受N个位置参数，转换成元组的方式
# def test(*args):  #定义多个实参
#     print(args)
# test(1,2,3,4,5,5)   #位置参数
# test(*[1,2,4,5,5]) #args=tuple([1,2,3,4,5])
#
# def test1(x,*args):
#     print(x)
#     print(args)
# test1(1,2,3,4,5,6,7)   #元组
# #**kwargs:接受N个关键字参数，转换成字典的方式
# def test2(**kwargs):  #字典
#     print(kwargs)
#     print(kwargs['name'])
#     print(kwargs['age'])
#     print(kwargs['sex'])
# test2(name='alex',age=8,sex='F')
# #test2(**{'name':'alex','age':8})
# def test3(name,**kwargs):
#     print(name)
#     print(kwargs)
# test3('alex',age=18,sex='m')
# def test4(name,age=18,**kwargs):
#     print(name)
#     print(age)
#     print(kwargs)
# test4('alex',4,sex='m',hobby='tesla',)
# test4('alex',age=4,sex='m',hobby='tesla',)
# #test4('alex',sex='m',hobby='tesla',age=3)
def test4(name,age=18,*args,**kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)
    logger("TEST4")
#test4('alex',age=34,sex='m',hobby='tesla')  #报错
def logger(source):
    print("from %s" % source)
test4('alex',age=34,sex='m',hobby='tesla')