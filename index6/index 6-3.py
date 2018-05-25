# coding:utf8

# 如何解析简单的xml文档
''''''

'''
xml是一种十分常用的标记性语言,
它可以使用统一的方法来描述应用程序的结构化数据

<?xml version="1.0" encoding="UTF-8"?>
<?xml version="1.0"?>
<data> # 元素与子元素,属性
  <country name = "Liechtenstein"> # 属性name
    <rank updated="yes">2</rank>
    <year>2008</year>
    <gbppc>141100</gbppc>
    <neighbor name="Austria" direction="E"/>
    <neighbor name="Switzerland" direction="W"/>
  </country>
</data>

python中如何解析xml文档
'''

'''
解决方案:
使用标准库中的xml.etree.ElementTree,其中的parse函数
可以解析xml文档

from xml.etree.ElementTree
from xml.etree.ElementTree import parse
parse?
f = open('country.xml','r')
et = parse(f)
et
root = et.getroot()
root
et.getiterator
r = et.getiterator()
r
root.tag?
root.tag
root.attrib
root.text
root.text.strip()
root.getchildren()
for child in root:
    print child
root.get()
root.get
root.get()?
root.get?
root.get('name')
for child in root:
    print(child.get('name'))
root.find?
root.find('country')
root.findall('country')
root.iterfind('country')
r1 = root.iterfind('country')
r1.next()
r1.next()
r1.next()
for e in root.iterfind('country'):
    print e.get('name')
root.iter?
list(root.iter())
root.iter('rank')
list(root.iter('rank'))
root.findall('country/*')
root.findall('.//rank')
list(root.findall('.//rank'))
root.findall('.//rank/..')
root.findall('country[@name]')
root.findall('country[@age]')
root.findall('country[@name="Singapore"]')
root.findall('country[rank]')
root.findall('country[year=2008]')
root.findall('country[year='2008']')
root.findall('country[year="2008"]')
root.findall('country[1]')
root.findall('country[2]')
root.findall('country[0]')
root.findall('country[3]')

'''









