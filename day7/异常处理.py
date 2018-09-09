def bulk(self):
     print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..." %self.name,food)

# d = Dog("陈超")
# choice = input(">>:").strip() #strip去掉两边的空格
# getattr(d,choice)

names = ['alex','jack']
data = {}

try:
    #names[3]
    #data['name']
    open("tes.txt")
    a = 1
    #print(a)
except (KeyError,IndexError) as e: #抓住2个以上的错误
    print("没有这个key",e)
except IndexError as e: #可以看到报错IndexError
    print("列表操作错误",e)
except Exception as e:#抓住所有的错误,不建议用,放在最后
    print("未知错误",e)
else:                  #没有错误才走else
    print("一切正常")
finally:               #不管有没有错，都执行
    print("不管有没有错，都执行")