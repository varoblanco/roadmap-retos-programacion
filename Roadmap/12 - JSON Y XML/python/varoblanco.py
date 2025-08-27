import xml.etree.ElementTree as xml
import os
import json

#Datos de inicio
data = {
    "name": "Alvaro",
    "age": 36,
    "programming": ["Python", "JS"]

}

#Estructura para XML
xml_file = "varoblanco.xml"

def create_xml():

    root = xml.Element("data")

    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value)
    
    tree = xml.ElementTree(root)
    tree.write(xml_file)

create_xml()

with open(xml_file) as xml_data:
    print(xml_data.read())

os.remove(xml_file)

#Estructura para JSON
json_file = "varoblanco.json"

with open(json_file, "w") as json_data:
    json.dump(data,json_data)

with open(json_file) as json_data:
    print(json_data.read())

#os.remove(json_data)


"""EXTRA"""









