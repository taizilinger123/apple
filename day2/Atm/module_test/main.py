import sys,os
print(sys.path)
x=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)
import  module_alex

say_hello()
#from  module_alex  import name,logger
#name='alex'
#print(name)
#logger()
'''
name='alex'
def say_hello():
    print('hello alex')

def logger():  #logger--->'pass'
    pass

def running():
    pass
'''
# def logger():    #logger---->'print'
#     print('in the main')
#
# logger()
# logger_alex()
