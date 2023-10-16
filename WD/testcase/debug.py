import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("WD\\")+len("WD\\")]
print(rootPath+"resource\\picture\\aspenLogo.png")