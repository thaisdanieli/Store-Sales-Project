'''
O que faz: Lê as planilhas da pasta, faz a filtragem, agrupa os dados por loja, 
calcula as diferenças, o crescimento percentual (como o que você mostrou no print), 
PMV, etc.
Retorno: Ele devolve para você um DataFrame do Pandas pronto e calculado.
'''

import os
import glob
import pandas as pd 

def processar_dados_vendas():
    # 1. Caminho da pasta onde estão os arquivos Excel
    pasta_arquivos = "data"

    # Busca todos os arquivos .xlsx que começam com "Vendas -"
    arquivos = glob.glob(os.path.join(pasta_arquivos, "Vendas - *.xlsx"))

    lista_dfs = []

    for caminho_completo in arquivos:
        # Pega apenas o nome do arquivo com a extensão (ex: "Vendas - Brotas - 10-2025.xlsx")
        nome_arquivo = os.path.basename(caminho_completo)

        # Esse método separa: nome do arquivo + extensão
        # Remove a extensão .xlsx (ex: "Vendas - Brotas - 10-2025")
        nome_base = os.path.splitext(nome_arquivo)[0]

        # Divide o nome pelo separador " - "
        partes = nome_base.split(" - ")
        loja = partes[1]    # "Brotas", "Cravinhos", etc.
        periodo = partes[2] # "10-2025", "10-2026", etc.

        # Lê a planilha atual
        df_temp = pd.read_excel(caminho_completo)

        # Adiciona as colunas identificadoras extraídas do nome do arquivo
        df_temp['Loja'] = loja
        df_temp['Periodo'] = periodo

        lista_dfs.append(df_temp)

    # 2. Consolida todas as planilhas em um único DataFrame
    df_consolidado = pd.concat(lista_dfs, ignore_index=True)

    print("Dados consolidados com sucesso! Visualização das primeiras linhas:")
    print(df_consolidado.head())

    # 3. Salva a base consolidada para você guardar ou abrir no Excel
    df_consolidado.to_excel("Vendas_Consolidadas_Todas_Lojas.xlsx", index=False)

    coluna_valor = "Valor L ($)"

    # Total vendido por Loja e por Ano
    # Pegue o DataFrame consolidado, agrupe pela Loja e pelo Ano, pegue a coluna de valor, some os valores de cada grupo e transforme Loja e Ano novamente em colunas.
    vendas_resumo = df_consolidado.groupby(['Loja', 'Periodo'])[coluna_valor].sum().reset_index()
    print("\n--- Total de Vendas por Loja e Ano ---")
    print(vendas_resumo)

    # Coloque as Lojas nas linhas, os Anos nas colunas, coloque o Valor dentro da tabela e, quando houver vários valores, some-os.
    # Comparativo Ano contra Ano (Pivot Table)
    tabela_comparativa = df_consolidado.pivot_table(
        index='Loja',
        columns='Periodo',
        values=coluna_valor,
        aggfunc='sum'       # aggfunc significa função de agregação.
    )

    column0 = tabela_comparativa.columns[0]
    column1 = tabela_comparativa.columns[1]

    # Calcula o crescimento percentual entre 2025 e 2026
    tabela_comparativa['% META 3D'] = (
        (tabela_comparativa[column1] - tabela_comparativa[column0]) / tabela_comparativa[column0]
    ) 

    print(f"\n--- Comparativo {column0} vs {column1} com Crescimento ---")
    print(tabela_comparativa)

    return tabela_comparativa, periodo

    