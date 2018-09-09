#import json
import pickle
def sayhi(name):
    #print("hello,",name)
    print("hello2,", name)
f = open("test.text","rb")
#data = eval(f.read())
#data = json.loads(f.read())
data = pickle.loads(f.read())
print(data["func"]("Alex"))