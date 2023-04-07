from datetime import datetime


class SimpleReport:

    @staticmethod
    def retorna_data_fabricacao_mais_antiga(produtos: list[dict]) -> str:
        data_fab_mais_antiga = produtos[0]["data_de_fabricacao"]

        for produto in produtos:
            if produto["data_de_fabricacao"] < data_fab_mais_antiga:
                data_fab_mais_antiga = produto["data_de_fabricacao"]

        return data_fab_mais_antiga

    @staticmethod
    def retorna_data_validade_mais_proxima(produtos: list[dict]) -> str:
        data_atual = datetime.today()
        lista_de_validades = []

        for produto in produtos:
            data_validade = datetime.strptime(
                produto["data_de_validade"], "%Y-%m-%d")

            if data_validade > data_atual:
                lista_de_validades.append(produto["data_de_validade"])

        validade_mais_proxima = min(lista_de_validades)

        return validade_mais_proxima

    @staticmethod
    def retorna_empresa_com_mais_produtos(produtos: list[dict]) -> str:
        lista_de_contagem_de_produtos_por_empresa = {}

        for produto in produtos:
            nome_da_empresa = produto['nome_da_empresa']

            if nome_da_empresa in lista_de_contagem_de_produtos_por_empresa:
                lista_de_contagem_de_produtos_por_empresa[nome_da_empresa] += 1
            else:
                lista_de_contagem_de_produtos_por_empresa[nome_da_empresa] = 1

        empresa_com_mais_produtos = None
        qtd_maior = 0

        for empresa, qtd in lista_de_contagem_de_produtos_por_empresa.items():
            if qtd > qtd_maior:
                empresa_com_mais_produtos = empresa
                qtd_maior = qtd

        return empresa_com_mais_produtos

    @staticmethod
    def generate(produtos: list[dict]) -> str:
        fabricacao = SimpleReport.retorna_data_fabricacao_mais_antiga(produtos)
        validade = SimpleReport.retorna_data_validade_mais_proxima(produtos)
        empresa = SimpleReport.retorna_empresa_com_mais_produtos(produtos)

        return (
            f'Data de fabricação mais antiga: {fabricacao}\n'
            f'Data de validade mais próxima: {validade}\n'
            f'Empresa com mais produtos: {empresa}'
        )
