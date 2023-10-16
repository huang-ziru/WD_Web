import os
import re
import sys
import xml.dom.minidom
from xml.dom.minidom import parse
from xml.dom.minidom import Document

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = curPath[:curPath.find("WD\\") + len("WD\\")]
sys.path.extend([rootPath, rootPath])

# Process the current script running address
path1 = os.path.dirname(os.path.abspath(__file__))
command = "pytest " + path1 + " --junit-xml=../report/report1.xml"
os.system(command)

DOMTree = xml.dom.minidom.parse("..\\report\\report1.xml")
collection = DOMTree.documentElement
testsuite = collection.getElementsByTagName("testsuite")
if testsuite[0].getAttribute("failures") != '0':
    command = "pytest --lf " + path1 + " --junit-xml=../report/report2.xml"
    os.system(command)

# Create a document object
doc = Document()
# Create a root node
root = doc.createElement('testsuites')
# Join root node to tree
doc.appendChild(root)
# Create secondary node
testsuite = doc.createElement('testsuite')
testresult = doc.createElement('testresult')
# Using minidom parser to open XML document
filename = path1 + '\..\\report\\report2.xml'
DOMTree = xml.dom.minidom.parse("..\\report\\report1.xml")
collection = DOMTree.documentElement
CaseNames_fail = []
case_list = [{'caseID': '29463', 'caseName': "Administration User Exits:run test- there's code change"},
             {'caseID': '29484', 'caseName': 'Material: BOM exceptions- Submit'}, {'caseID': '29544',
                                                                                   'caseName': 'Equipment-booth, modify/add a machine name which exist in the workstation column'},
             {'caseID': '29638', 'caseName': "Permission: permission-modify can't be removed by current user"},
             {'caseID': '29639',
              'caseName': 'WD: Material, Equipment, Order, Administration-uncommitted data when moving out from detail.'},
             {'caseID': '29668', 'caseName': 'Order Refresh'}, {'caseID': '31064',
                                                                'caseName': 'Equipment-scale, user changes any of scale NON-state related information'},
             {'caseID': '31283', 'caseName': 'audit user exits report'},
             {'caseID': '31310', 'caseName': 'Equipment:Two users edit the same booth at the same time'},
             {'caseID': '31357', 'caseName': 'WD: Material: delete/Export CSV/Add/remove columns BOM exceptions'},
             {'caseID': '31382', 'caseName': 'Report-Order print'},
             {'caseID': '31386', 'caseName': 'Administration User Exits: test tool bar cut, copy and paste.'},
             {'caseID': '31390', 'caseName': 'audit BOM Exceptions report'},
             {'caseID': '31408', 'caseName': "BOM Exceptions: Add a material which 'Ingredient type' is main"},
             {'caseID': '31472', 'caseName': 'Filter testing on order web page'}, {'caseID': '31783',
                                                                                   'caseName': 'W&D ENH: Cleaning rules should apply until the last changse are committed (from CQ00550764)'},
             {'caseID': '32426', 'caseName': 'V8.8.5_CQ00758138:"general, integration and printing" report generate'},
             {'caseID': '36270', 'caseName': 'W&D: user cannot delete a pending BOM Exception'}, {'caseID': '37540',
                                                                                                  'caseName': 'V10Enh-Check the warning message should contain BOM name when delete BOM exceptions'},
             {'caseID': '38281', 'caseName': 'V8.8.5_CQ00758138:"General" audit generate'},
             {'caseID': '40873', 'caseName': 'Permission: not grant any permission'}, {'caseID': '40888',
                                                                                       'caseName': 'Material: add/edit/delete/Export/Add/remove columns for materials in BOM exception'},
             {'caseID': '40891', 'caseName': 'Administration Cleaning Rules:Cleaning rules-data'},
             {'caseID': '40961', 'caseName': 'audit cleaning rules report'},
             {'caseID': '41001', 'caseName': 'Equipment-booth, operations to booth'},
             {'caseID': '41179', 'caseName': 'Permission: grant all permission'},
             {'caseID': '41201', 'caseName': 'Materials: export/filter/highlight default value/search'},
             {'caseID': '41249', 'caseName': 'Inventory Refresh,search,Add/Remove columns and Export'},
             {'caseID': '41331',
              'caseName': 'Equipment-scale, user changes any of scale scale NON-state related information'},
             {'caseID': '41360',
              'caseName': 'Equipment: 2 different users goes to scale management page, 1 user delete a scale another user try to delete the deleted one.'},
             {'caseID': '41361', 'caseName': 'Administration Cleaning Rules:cleaning rules-states'},
             {'caseID': '41378', 'caseName': 'Administration Printing: config label print'},
             {'caseID': '42059', 'caseName': 'create campaign with selected orders'},
             {'caseID': '42062', 'caseName': 'Report-audit orders'},
             {'caseID': '42107', 'caseName': 'audit scale report'},
             {'caseID': '42287', 'caseName': 'Material: delete material'},
             {'caseID': '42288', 'caseName': 'Material: add/Edit/copy BOM-Save'},
             {'caseID': '42290', 'caseName': 'Administration Cleaning Rules:Cleaning rules-actions'},
             {'caseID': '42356', 'caseName': 'Order, two user edit the same order at the same time'},
             {'caseID': '42812', 'caseName': 'audit booth report'},
             {'caseID': '42821', 'caseName': 'Equipment-Booth, create a machine name'},
             {'caseID': '42939', 'caseName': 'Material: modify material- save'}, {'caseID': '42966',
                                                                                  'caseName': 'Equipment: 1 user is editing the booth information, another user try to delete the booth.'},
             {'caseID': '43253', 'caseName': 'audit materials report'}, {'caseID': '43293',
                                                                         'caseName': 'Permission: user holding ?Equipment Change State? permission changes scale state information'},
             {'caseID': '43369', 'caseName': 'Administration Printing: config report print'},
             {'caseID': '43376', 'caseName': 'Administration User Exits:Commit User Exit'},
             {'caseID': '43382', 'caseName': 'Order-management option, add material'},
             {'caseID': '43384', 'caseName': "BOM Exceptions: Add a material which 'Ingredient type' is Excipient"},
             {'caseID': '43411', 'caseName': 'Equipment-scale,  manage scale standardization type list'},
             {'caseID': '43508',
              'caseName': 'Equipment-booth, user holding "Equipment Add+modify" permission, changes any of booth NON-state related information'},
             {'caseID': '45585', 'caseName': 'Order:Notice that campaign status is based in participant order status'},
             {'caseID': '45682', 'caseName': 'Equipment:  swtich scale between booths'},
             {'caseID': '45683', 'caseName': 'Material: modify material - submit'},
             {'caseID': '45684', 'caseName': 'Administration User Exits: '},
             {'caseID': '45751', 'caseName': 'audit campaigns report'},
             {'caseID': '45776', 'caseName': 'Equipment-booth, changes Machine name to a name that already exists'},
             {'caseID': '91464',
              'caseName': 'Equipment-booth, user had no "Equipment change"permission, try to change any of booth state related information'},
             {'caseID': '91537', 'caseName': "BOM Exceptions: Add a material which 'Ingredient type' is Active"},
             {'caseID': '91550', 'caseName': 'Equipment-scale, operations to scale'},
             {'caseID': '809632', 'caseName': 'UC809496_"Help about" shows correctly in Weigh & Dispense web page'}]

failed_caseid = []
passed_caseid = []
if os.path.exists(filename) is True:
    DOMTree2 = xml.dom.minidom.parse(filename)
    collection2 = DOMTree2.documentElement
    testsuites = collection2.getElementsByTagName("testsuite")
    testcases = collection2.getElementsByTagName("testcase")
    for testcase in testcases:
        classname = testcase.getAttribute("classname")
        # casename1 = testcase.getAttribute("name")
        case_id = classname.split('.')[0]
        failure = testcase.getElementsByTagName('failure')
        if failure != []:
            message = failure[0].getAttribute('message')
            casepoint = doc.createElement('testcase')
            casepoint.setAttribute('result', 'Failed')
            if case_id not in failed_caseid:
                # print(case_id)
                failed_caseid.append(case_id)
                casepoint.setAttribute('case_id', case_id)
                for caseDict in case_list:
                    if caseDict['caseID'] == re.sub(r'\D', "", case_id):
                        casename = caseDict['caseName']
                        # print(casename)
                        casepoint.setAttribute('case_name', casename)
                        casepoint.setAttribute('message', message)
                        vsts_id = 'VSTS' + re.sub(r'\D', "", case_id)
                        casepoint.setAttribute('VSTS_id', vsts_id)
                        testresult.appendChild(casepoint)
                        if casename not in CaseNames_fail:
                            CaseNames_fail.append(casename)
else:
    testsuites = collection.getElementsByTagName("testsuite")
testcases = collection.getElementsByTagName("testcase")
for testcase in testcases:
    classname = testcase.getAttribute("classname")
    case_id = classname.split('.')[0]
    if (case_id not in failed_caseid) and (case_id not in passed_caseid):
        passed_caseid.append(case_id)
        for caseDict in case_list:
            if caseDict['caseID'] == re.sub(r'\D', "", case_id):
                casename = caseDict['caseName']
                if casename not in CaseNames_fail:
                    casepoint = doc.createElement('testcase')
                    casepoint.setAttribute('result', 'PASS')
                    casepoint.setAttribute('case_id', case_id)
                    casepoint.setAttribute('case_name', casename)
                    vsts_id = 'VSTS' + re.sub(r'\D', "", case_id)
                    casepoint.setAttribute('VSTS_id', vsts_id)
                    testresult.appendChild(casepoint)
                    testsuite.appendChild(testresult)
                    root.appendChild(testsuite)
testsuites = collection.getElementsByTagName("testsuite")
# total_test = testsuites[0].getAttribute("tests")
error = testsuites[0].getAttribute("errors")
skipped = testsuites[0].getAttribute("skipped")
time = testsuites[0].getAttribute("time")
num_passed = len(passed_caseid)
num_failed = len(failed_caseid)
total_test = num_passed + num_failed
testsuite.setAttribute('errors', error)
testsuite.setAttribute('Failed', str(num_failed))
testsuite.setAttribute('skipped', skipped)
testsuite.setAttribute('Passed', str(num_passed))
testsuite.setAttribute('total', str(total_test))
testsuite.setAttribute('time', time)

# 存成xml文件
fp = open('..\\report\\test.xml', 'w', encoding='utf-8')
doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding='utf-8')
fp.close()
