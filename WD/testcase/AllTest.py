import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("WD\\")+len("WD\\")]
sys.path.extend([rootPath, rootPath])
from xml.dom.minidom import parse

# Process the current script running address
path1 = os.path.dirname(os.path.abspath(__file__))
command = "pytest " + path1 + " --junit-xml=../report/report1.xml"
os.system(command)
import xml.dom.minidom
DOMTree = xml.dom.minidom.parse("..\\report\\report1.xml")
collection = DOMTree.documentElement
testsuite = collection.getElementsByTagName("testsuite")
if testsuite[0].getAttribute("failures") != '0':
    command = "pytest --lf " + path1 + " --junit-xml=../report/report2.xml"
    os.system(command)





