from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter

importer = {
    'csv': CsvImporter,
    'json': JsonImporter,
    'xml': XmlImporter}