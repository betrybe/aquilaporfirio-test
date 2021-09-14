from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self):
        print("Criação do Complete Report")

    @staticmethod
    def produtos_estocados_por_empresa(list):
        todas_empresas = []
        for empresa in list:
            todas_empresas.append(empresa["nome_da_empresa"])

            empresas_comuns = Counter(todas_empresas)

            estoque_por_empresa = "\nProdutos estocados por empresa:\n"

        for nome_empresa, quantidade in empresas_comuns.items():
            estoque_por_empresa += f"- {nome_empresa}: {quantidade}\n"
        return estoque_por_empresa

    @classmethod
    def generate(cls, list):
        simple_report = super().generate(list)
        complete_report = cls.produtos_estocados_por_empresa(list)
        return simple_report + complete_report
