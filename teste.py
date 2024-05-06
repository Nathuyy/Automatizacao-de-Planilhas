import pandas as pd

# insira caminho aqui
caminho_arquivo = "C:/Users/nathy/Downloads/04 2024 visao_contas_a_pagar.xlsx"

planilha = pd.read_excel(caminho_arquivo)

codigos = {
    'Internet': 1490,
    'Encargos Funcionários - Assist. Médica e Odontol.' : 2136,
    'serviços prestados PJ': 4026,
    'Manutenção e Conservação da Sede': 1473,
    'Antecipação de Lucros' : 8096,
    'Confraternizações' : 80364,
    'Despesas Bancárias' : 2593, 
    'Estágios' : 293,
    'Comissão Vendedores' : 964,
    'Condução' : 2607,
    'Energia Elétrica' : 1392,
    'Encargos Funcionários - FGTS' : 850,
    'Remuneração Funcionários' : 396,
    'Pro Labore' : 80375,
    'Encargos - Rescisões Trabalhistas' : 396,
    'Licença ou Aluguel de Softwares' : 4097,
    'Imposto - ISSQN' : 4167,
    'Contabilidade' : 4070,
    'Telefonia' : 1376,
    'Água' : 1384,
    'Segurança' : 1466
}

def atribuir_codigo(categoria):
    return codigos.get(categoria, None)

planilha['Codigo'] = planilha['Categoria'].apply(atribuir_codigo)

planilha.to_excel('sua_planilha_com_codigos.xlsx', index=False)