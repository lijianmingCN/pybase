# -*- coding: cp936 -*-
import sys
import string
import xml.etree.ElementTree as ET

def readXml():
    #string = ET.fromstring(string) #加载指定字符串
    xmlfile = ET.parse('country_data.xml') #加载指定文件
    ET.dump(xmlfile) #显示XML树
    root = xmlfile.getroot() #获取xml根结点使用getroot()方法
    print type(xmlfile) #<class 'xml.etree.ElementTree.ElementTree'>
    print type(root) #<class 'xml.etree.ElementTree.Element'>
    #print xmlfile.getchildren()  #ElementTree不能get子节点
    country = root.findall('country') #从父节点开始才能get子节点
    for subItem in country :
        print subItem.get('name')
        print subItem.text
        print subItem.tag
    subEle1 = root.find('country') #获得某个子节点
    print subEle1.get('rank')
    print ET.dump(root.find('country')) #显示子节点树


def createXml():
    root = ET.Element('goods') #Element类，使用构造函数，入参为标签名字
    shirt = ET.SubElement(root,'shirt')
    name = ET.SubElement(root,'name')
    size = ET.SubElement(root,'size')
    shirt.attrib["quality"] = "A" #元素属性作为字典结构来保存数据
    shirt.text = 'black' #text属性，设置元素的内容
    tree = ET.ElementTree(root) #使用ElementTree方法构建一个树对象，使用构造函数，入参为根节点对象，并赋值给tree对象
    tree.write(sys.stdout) #使用tree的write方法，将XML文档输出到标准输出
    tree.write('x.xml')
 
createXml()
readXml()