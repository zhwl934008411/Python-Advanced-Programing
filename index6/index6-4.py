# coding:utf8
import csv
from xml.etree.ElementTree import Element, ElementTree, tostring
from e2 import pretty
# 如何构建xml文档
''''''
'''
将pingan2.csv文件转化为xml文件,
pingan2.csv:
  Date,open
  2018-05-23,8.88
pingan2.xml:
  <Data>
    <Row>
      <Date>2018-05-23</Date>
      <Open>8.88</Open>
    </Row>
  </Data>
'''
'''
解决方案
使用标准库中的xml.etree.ElementTree,构建ElementTree,使用
write方法写入文件
'''
'''
e.Element('Data')
e.tag
e.set('name','abc')
e.attrib()
e.get('name')
tostring(e)
e.text = '123'
tostring(e)
e.append?
e2 = Element('Row')
e3 = Element('Open')
e3.text = '8.80'
tostring(e3)
e2.append(e3)
tostring(e2)
e.text = None
e.append(e2)
tostring(e)
et = ElemetTree(e)
et = ElementTree(e)
et.write?
et.write('demo.xml')
cat demo.xml
history
'''


def csvToxml(fname):
    with open(fname, 'rb') as rf:
        reader = csv.reader(rf)
        headers = reader.next()
        headers = ['a','b','c','d','a','b','c','d','a','b','c','d']
        print(headers)
        root = Element('Data')

        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            
            for tag, text in zip(headers, row):
                e = Element(tag)
                e.text = text
                #tostring(e)
                print(e.text)
                eRow.append(e)
            #tostring(eRow)
        #tostring(root)
        # et = ElementTree(root)
        # et.write(fname2)
    pretty(root)
    return ElementTree(root)


et = csvToxml('pingan6.csv')
et.write('pingan3.xml')
