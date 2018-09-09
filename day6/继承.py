#class People:经典类
class People(object): #新式类
    def __init__(self,name,age):
        self.name = name  #self.Name = name
        self.age = age
        self.friends = []
        print("init in People")
    def eat(self):
        print("%s is eating..." % self.name)
    def talk(self):
        print("%s is talking..." % self.name)
    def sleep(self):
        print("%s is sleeping..." % self.name)

class Relation(object):
     def __init__(self,n1,n2):
        print("init in relation" )
     def make_friends(self,obj): #w1
         print("%s is making friends with %s" % (self.name,obj.name))
         self.friends.append(obj.name)

class Man(Relation,People):
    #def __init__(self,name,age,money):
        # #People.__init__(self,name,age)     #经典类写法
        # super(Man,self).__init__(name,age)  #新式类写法
        # self.money = money
        # print("%s 一出生就有%s money" %(self.name,self.money))
    def piao(self):
        print("%s is piaoing ..... 20s....done." % self.name)
    def sleep(self):
        People.sleep(self)
        print("man is sleeping")  #子类重写父类

class Woman(People,Relation):
    def get_birth(self):
        print("%s is born a baby...." % self.name)

m1 = Man("NiuHanYang", 22)

