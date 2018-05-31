import xml.dom.minidom as xml
import xml.etree.ElementTree as ET
import os
class xmls:

    def __init__(self,para = None):

        return

    def writeXML(self, filename, dic):

        path = os.getcwd() + '\\' + filename

        doc = xml.Document()
        root = doc.createElement("transformParm")

        doc.appendChild(root)

        for lue in dic.keys():
            nodeName = doc.createElement(lue)
            nodeName.appendChild(doc.createTextNode(str(dic[lue])))
            root.appendChild(nodeName)

        f = open(path, 'w')
        doc.writexml(f, indent='\t', addindent='\t', newl='\n', encoding="utf-8")


