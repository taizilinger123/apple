import  configparser
conf = configparser.ConfigParser()
conf.read("example.ini")

print(conf.defaults())
print(conf['bitbucket.org']['user'])

# for key in conf['bitbucket.org']:
#           print(key)
#print(conf.sections())
sec = conf.remove_section('bitbucket.org')
conf.write(open('example.ini',"w"))