# school = "Oldboy edu."    #全局变量
# def change_name(name):
#     global school          #在局部变量里改全局变量
#     school = "Mage Linux" #局部变量
#     print("before change",name,school)
#     name = "Alex li" #这个函数就是这个变量的作用域
#     age = 23
#     print("after change",name)
# name = "alex"
# change_name(name)
# print(name)
# print("school:",school)
# #print("age",age)
# def change_name():
#     global name    #用就被开除了
#     name = "alex"
# change_name()
# print(name)
#--------------------------
school = "Oldboy edu."
names = ["Alex","Jack","Rain"]
def change_name():
    names[0] = "金角大王"
    print("inside func",names)
change_name()
print(names)
