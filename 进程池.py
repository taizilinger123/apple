from  multiprocessing import Process, Pool,freeze_support
import time
import os

def Foo(i):
    time.sleep(2)
    print("in process",os.getpid())
    return i + 100

def Bar(arg):
    print('-->exec done:', arg,os.getpid())

if __name__ == '__main__':
        #freeze_support()

        pool = Pool(processes=5) #允许进程池同时放入5个进程
        print("主进程",os.getpid())
        for i in range(10):
            pool.apply_async(func=Foo, args=(i,), callback=Bar) #并行 #callback=回调
            #pool.apply(func=Foo, args=(i,))  #串行
            #pool.apply_async(func=Foo, args=(i,)) #并行
        print('end')
        pool.close() #一定要先关闭进程池再join
        pool.join()  # 进程池中进程执行完毕后再关闭，如果注释，那么程序直接关闭。