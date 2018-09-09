def bulk(self):
     print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..." %self.name,food)

d = Dog("陈超")
choice = input(">>:").strip() #strip去掉两边的空格

if hasattr(d,choice):
   getattr(d,choice)
else:
    # setattr(d, choice, None)
    # #print(d.age)
    # v = getattr(d,choice)
    # print(v)

    setattr(d,choice,bulk)  #d.talk = bulk
    func = getattr(d,choice)
    func(d)