# lib = __import__('lib.aa') #lib
#
# obj = lib.aa.C()
# print(obj.name)
#
# instance = getattr(lib.aa,"C")  #反射
# obj = instance()
# print(obj.name)
import importlib
aa = importlib.import_module('lib.aa') #官方建议用这个
obj = aa.C()
assert type(obj.name) is int
if type(obj.name) is not int:
    exit("must be in")
print(obj.name /2)
# assert type(obj.name) is str
# print("ddddd")
