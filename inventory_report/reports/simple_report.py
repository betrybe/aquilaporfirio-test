from operator import itemgetter
from datetime import datetime
from collections import Counter


class SimpleReport:
    def __init__(self):
        print("Criação do Simple Report.")

    @staticmethod
    def retorna_produto_mais_antigo(list):
        dataAntiga = sorted(list, key=itemgetter("data_de_fabricacao"))[0]
        return dataAntiga["data_de_fabricacao"]

    @staticmethod
    def retorna_validade_mais_proxima(list):
        data_formatada = "%Y-%m-%d"
        return str(
            min(
                datetime.strptime(item["data_de_validade"], data_formatada)
                for item in list
                if datetime.strptime(item["data_de_validade"], data_formatada) 
                > datetime.today()
            ).date()
        )

    @staticmethod
    def quantidade_de_produto_estocado(list):
        todas_empresas = []
        for empresa in list:
            todas_empresas.append(empresa["nome_da_empresa"])

        empresas_comuns = Counter(todas_empresas).most_common()
        return empresas_comuns[0][0]

    @classmethod
    def generate(cls, list):
        produto_antigo = cls.retorna_produto_mais_antigo(list)
        validade_mais_proxima = cls.retorna_validade_mais_proxima(list)
        empresa_com_maior_estoque = cls.quantidade_de_produto_estocado(list)

        simple_report = (
            f"Data de fabricação mais antiga: {produto_antigo}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {empresa_com_maior_estoque}\n"
        )
        return simple_report
