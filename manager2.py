from multiprocessing import Process, Manager
import os

def f(d, l):
    d[os.getpid()] = os.getpid()
    # d[1] = '1'
    # d['2'] = 2
    # d[0.25] = None

    l.append(os.getpid())
    print(l)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()  #{} #生成一个字典，可在多个进程间共享和传递

        l = manager.list(range(5)) #生成一个列表，可在多个进程间共享和传递
        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            p_list.append(p)
        for res in p_list:  #等待结果
            res.join()

        print(d)
        print(l)