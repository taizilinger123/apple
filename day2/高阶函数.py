var result = subtract(multiply(add(1,2),3),4);  #函数式编程
def add(a,b,f):    #高阶函数
    return f(a)+f(b)
res = add(3,-6,abs)
print(res)

{
    'backend':'www.oldboy.org',
    'record':{
        'server':'100.1.7.9',
        'weight':20,
        'maxconn':30
    }
}
>>> b = '''
... {
...     'backend':'www.oldboy.org',
...     'record':{
...         'server':'100.1.7.9',
...         'weight':20,
...         'maxconn':30
...     }
... }'''
>>> b
" \n{\n    'backend':'www.oldboy.org',\n    'record':{\n        'server':'100.1.
7.9',\n        'weight':20,\n        'maxconn':30\n    }\n}"
>>> b[1]
'\n'

>>> eval(b)
{'record': {'server': '100.1.7.9', 'weight': 20, 'maxconn': 30}, 'backend': 'www
.oldboy.org'}

>>> b=eval(b)
>>> b
{'record': {'server': '100.1.7.9', 'weight': 20, 'maxconn': 30}, 'backend': 'www
.oldboy.org'}
>>> b['record']
{'server': '100.1.7.9', 'weight': 20, 'maxconn': 30}












