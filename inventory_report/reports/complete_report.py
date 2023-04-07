from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def retorna_qtd_de_produtos_estocados(produtos: list[dict]) -> list[dict]:
        lista_com_qtd_de_produtos_por_empresa = {}

        for produto in produtos:
            nome_da_empresa = produto['nome_da_empresa']

            if nome_da_empresa in lista_com_qtd_de_produtos_por_empresa:
                lista_com_qtd_de_produtos_por_empresa[nome_da_empresa] += 1
            else:
                lista_com_qtd_de_produtos_por_empresa[nome_da_empresa] = 1

        return lista_com_qtd_de_produtos_por_empresa

    @staticmethod
    def generate(produtos: list[dict]) -> str:
        fabricacao = SimpleReport.retorna_data_fabricacao_mais_antiga(produtos)
        validade = SimpleReport.retorna_data_validade_mais_proxima(produtos)
        empresa = SimpleReport.retorna_empresa_com_mais_produtos(produtos)
        lista_qtds = CompleteReport.retorna_qtd_de_produtos_estocados(produtos)

        relatorio = (
            f'Data de fabricação mais antiga: {fabricacao}\n'
            f'Data de validade mais próxima: {validade}\n'
            f'Empresa com mais produtos: {empresa}\n'
            "Produtos estocados por empresa:\n"
        )

        for empresa, qtd in lista_qtds.items():
            relatorio += f"- {empresa}: {qtd}\n"

        return relatorio
