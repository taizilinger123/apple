
#print("---------dddd")
# print(f.__next__())
# print("=====================")
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
#
# print("=========start loop=========")
# for i in f:
#     print(i)

#code =
'''
 def fib(max):  #10
    n, a, b = 0, 0, 1
    while n < max: #n<10
        #print(b)
        yield  b           #生成器,就是斐波那契改过来的
        a, b = b, a + b
        n = n + 1
    return '------------done---------'

#print(fib(10))
#f=fib(10)
g=fib(6)
while True:
    try:
        x=next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
'''

# py_obj = compile(code,"err.log","exec")
# exec(py_obj)
# exec(code)


# def sayhi(n):
#     print(n)
#     for i in range(n):
#         print(i)
# sayhi(3)
#
# #(lambda  n:print(n))(5)
# calc = lambda n:3 if n<4 else n
# print(calc(5))

#res = filter(lambda n:n>5,range(10))  #过虑
#res = map(lambda n:n*2,range(10))
#res = [lambda i:i*2 for i in range(10)]
# import  _functools
# res = _functools.reduce(lambda x,y:x*y,range(1,10))
# print(res)

# a = frozenset([1,4,333,212,33,33,12,4])
# #print(globals())
#
# def  test():
#     local_var=333
#     print(locals())
#     print(globals())
# test()
# print(globals())
# # print(globals().get('local_var'))
# a = {6:2,8:0,1:4,-5:6,99:11,4:22}
# #print(sorted(a.items()))
# print(sorted(a.items(),key=lambda x:x[1]))
# print(a)
# a=[1,2,3,4,5,6]
# b=['a','b','c','d']
# for i in zip(a,b):
#     print(i)
#import decorator
__import__('decorator')










