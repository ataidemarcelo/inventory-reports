import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def ler_arquivo_csv(caminho_para_arquivo: str) -> list[dict]:
        with open(caminho_para_arquivo, "r") as file:
            reader = csv.DictReader(file)
            lista_de_produtos = []
            for linha in reader:
                lista_de_produtos.append(linha)
        return lista_de_produtos

    @staticmethod
    def ler_arquivo_json(caminho_para_arquivo: str) -> list[dict]:
        with open(caminho_para_arquivo, "r") as file:
            lista_de_produtos = json.load(file)
        return lista_de_produtos

    @staticmethod
    def ler_arquivo_xml(caminho_para_arquivo: str) -> list[dict]:
        tree = ET.parse(caminho_para_arquivo)
        root = tree.getroot()
        lista_de_produtos = []

        for produto in root.findall("record"):
            produto_dict = {}
            for campo in produto:
                produto_dict[campo.tag] = campo.text
            lista_de_produtos.append(produto_dict)

        return lista_de_produtos

    @staticmethod
    def ler_arquivo(caminho_para_arquivo: str) -> list[dict]:
        if ".csv" in caminho_para_arquivo:
            lista_de_produtos = Inventory.ler_arquivo_csv(caminho_para_arquivo)
        elif ".json" in caminho_para_arquivo:
            lista_de_produtos = Inventory.ler_arquivo_json(
                caminho_para_arquivo)
        elif ".xml" in caminho_para_arquivo:
            lista_de_produtos = Inventory.ler_arquivo_xml(caminho_para_arquivo)
        else:
            raise ValueError(
                "Tipo de arquivo inválido.Precisa ser 'CSV', 'XML' ou 'JSON'"
            )

        return lista_de_produtos

    @staticmethod
    def import_data(caminho_para_arquivo: str, tipo_de_relatorio: str) -> str:
        lista_com_tipos_de_relatorios_permitidos = ["simples", "completo"]
        if tipo_de_relatorio not in lista_com_tipos_de_relatorios_permitidos:
            raise ValueError(
                f"O tipo: '{tipo_de_relatorio}' é inválido para relatórios."
                "Use somente: 'simples' ou 'completo'"
            )

        lista_de_produtos = Inventory.ler_arquivo(caminho_para_arquivo)

        if tipo_de_relatorio == "simples":
            relatorio = SimpleReport.generate(lista_de_produtos)
        elif tipo_de_relatorio == "completo":
            relatorio = CompleteReport.generate(lista_de_produtos)

        return relatorio
