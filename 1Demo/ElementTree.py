# -*- coding: cp936 -*-
import sys
import string
import xml.etree.ElementTree as ET

def readXml():
    #string = ET.fromstring(string) #����ָ���ַ���
    xmlfile = ET.parse('country_data.xml') #����ָ���ļ�
    ET.dump(xmlfile) #��ʾXML��
    root = xmlfile.getroot() #��ȡxml�����ʹ��getroot()����
    print type(xmlfile) #<class 'xml.etree.ElementTree.ElementTree'>
    print type(root) #<class 'xml.etree.ElementTree.Element'>
    #print xmlfile.getchildren()  #ElementTree����get�ӽڵ�
    country = root.findall('country') #�Ӹ��ڵ㿪ʼ����get�ӽڵ�
    for subItem in country :
        print subItem.get('name')
        print subItem.text
        print subItem.tag
    subEle1 = root.find('country') #���ĳ���ӽڵ�
    print subEle1.get('rank')
    print ET.dump(root.find('country')) #��ʾ�ӽڵ���


def createXml():
    root = ET.Element('goods') #Element�࣬ʹ�ù��캯�������Ϊ��ǩ����
    shirt = ET.SubElement(root,'shirt')
    name = ET.SubElement(root,'name')
    size = ET.SubElement(root,'size')
    shirt.attrib["quality"] = "A" #Ԫ��������Ϊ�ֵ�ṹ����������
    shirt.text = 'black' #text���ԣ�����Ԫ�ص�����
    tree = ET.ElementTree(root) #ʹ��ElementTree��������һ��������ʹ�ù��캯�������Ϊ���ڵ���󣬲���ֵ��tree����
    tree.write(sys.stdout) #ʹ��tree��write��������XML�ĵ��������׼���
    tree.write('x.xml')
 
createXml()
readXml()