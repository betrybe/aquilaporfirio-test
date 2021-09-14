from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xml.etree.ElementTree as ET
import csv
import json


class Inventory:

    @staticmethod
    def arquivo_xml(file):
        root = ET.parse(file).getroot()
        """ Identifica as chaves arquivo do XML. """
        todos_registros = root.findall("record")
        inventory = []
        for records in todos_registros:
            file_dict = {}
            for tag in records:
                file_dict[tag.tag] = tag.text
            inventory.append(file_dict)
        return inventory

    @staticmethod
    def arquivo_csv(path):
        with open(path) as file:
            converter_aquivo_csv = csv.DictReader(file, delimiter=",")
            inventory = [row for row in converter_aquivo_csv]
        return inventory

    @staticmethod
    def arquivo_json(path):
        with open(path) as file:
            inventory = json.load(file)
        return inventory

    @classmethod
    def verifica_caminho(cls, path):
        if path.endswith(".csv"):
            itens = cls.arquivo_csv(path)
        elif path.endswith(".json"):
            itens = cls.arquivo_json(path)
        else:
            itens = cls.arquivo_xml(path)
        return itens

    @classmethod
    def import_data(cls, path, type):
        inventory = cls.verifica_caminho(path)
        if type == "simples":
            return SimpleReport.generate(inventory)

        if type == "completo":
            return CompleteReport.generate(inventory)
            