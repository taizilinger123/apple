class A:  #深度优先D---->B----->A----->C
    def __init__(self):
        print("A")

class B(A):
    pass
    # def __init__(self):
    #     print("B")

class C(A):
    def __init__(self):
        print("C")


class D(B,C):  #广度优先D--->B---->C---->A
    pass
    # def __init__(self):
    #     print("D")

obj = D()