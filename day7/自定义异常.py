class AlexError(Exception):
    def __init__(self, msg):
        self.message = msg

    # def __str__(self): #可以不写
    #     return 'sdfsf'

try:
    # name = []
    # name[3]
    raise AlexError('数据库连不上')
except AlexError as e:
    print(e)