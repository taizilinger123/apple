class  Dog:
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s: wang  wang wang!" % self.name)

d1 = Dog("陈超峰")

d1.bulk()
