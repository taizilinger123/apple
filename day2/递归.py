# def calc(n):
#     print(n)
#     return  calc(n+1)
# calc(0)  #999次内存耗光了，死掉了

def calc(n):
    print(n)
    if  int(n/2) >0:
        return calc(int(n/2))
    print("--->",n)
calc(10)

