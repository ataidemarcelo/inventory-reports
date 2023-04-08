from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        'Produto 01',
        'Empresa 01',
        '20/10/2022',
        '24/10/2022',
        '0001',
        'instrucoes_de_armazenamento',
    )

    assert product.id == 1
    assert product.nome_do_produto == 'Produto 01'
    assert product.nome_da_empresa == 'Empresa 01'
    assert product.data_de_fabricacao == '20/10/2022'
    assert product.data_de_validade == '24/10/2022'
    assert product.numero_de_serie == '0001'
    assert product.instrucoes_de_armazenamento == 'instrucoes_de_armazenamento'
