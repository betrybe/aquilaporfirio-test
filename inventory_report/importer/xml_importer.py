from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    def __init__(self):
        print("Xml Importer")

    def import_data(file):
        isTrue = file.endswith(".xml")
        if isTrue:
            with open(file) as file:
                root = ET.parse(file).getroot()
                todos_registros = root.findall("record")
                inventory = []
                for records in todos_registros:
                    file_dict = {}
                    for tag in records:
                        file_dict[tag.tag] = tag.text
                    inventory.append(file_dict)
                return inventory
        else:
            raise ValueError("Arquivo inválido")
