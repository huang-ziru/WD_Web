import os
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
# proDir = os.path.dirname(os.path.realpath(__file__))  与上面一行代码作用一样
configPath = os.path.join(proDir, "config.ini")
path = os.path.abspath(configPath)
print(configPath)
print(path)

conf = configparser.ConfigParser()
# 下面3种路径方式都可以
conf.read(path)
# conf.read(configPath)
# conf.read("D:/python2.7/practises/practise/configs.txt")

browser_name = conf.get('Browser', 'browser')
servername = conf.get('login', 'servername')
username = conf.get('login', 'username')
password = conf.get('login', 'password')

