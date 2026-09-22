'''
O que faz: Recebe o DataFrame pronto vindo do processor.py, joga os dados para dentro do Excel 
(usando openpyxl), aplica as cores dos cabeçalhos, negritos, larguras de colunas, 
formatação de porcentagem (0.00%) e bordas. É aqui também que você pode programar a função 
de salvar na pasta de saída e até o envio por e-mail.

'''
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils.dataframe import dataframe_to_rows

def exportar_e_formatar_excel(arquivo, data: str, caminho_saida):
    wb = Workbook()
    ws = wb.active
    ws.title = "DESEMPENHO LOJAS - DOCKS"

    # Garante que as linhas de grade apareçam na planilha
    ws.views.sheetView[0].showGridLines = True

    # 1. Escreve um cabeçalho superior informativo com a data recebida
    ws['A1'] = f"ANO: {data[-4:]}"
    ws['A1'].font = Font(name="Calibri",size=14, bold=True, color="1F497D")

    ws['A2'] = f"PERÍODO DE REFERÊNCIA: {data}"
    ws['A2'].font = Font(name="Calibri", size=11, italic=True)

    # Deixa uma linha em branco e joga os dados do DataFrame a partir da linha 4
    ws.append([]) # Linha 3 vazia

    # Converte o DataFrame do Pandas para linhas e adiciona na planilha
    for _, row in enumerate(dataframe_to_rows(arquivo, index=False, header=True), start=4):
        ws.append(row)

    # Estilização do cabeçalho da tabela (Linha 4)
    header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")

    for col_num in range(1, len(arquivo.columns) + 1):
        cell = ws.cell(row=4, column=col_num)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")

    # Estilização das linhas de dados, formatação de porcentagem e cores condicionais
    # Identifica dinamicamente as colunas "% META  3D" e "% LW 3D"
    colunas_alvo = ["% META 3D", "% LW 3D"]
    indices_alvo = []

    # Identifica dinamicamente as colunas de valores/anos (ex: '10-2025', '10-2026') 
    # Qualquer coluna que não seja texto descritivo nem porcentagem (ou que contenha hífens de data)
    




    for col_num, col_name in enumerate(arquivo.columns, start=1):
        if str(col_name).strip() in [c.strip() for c in colunas_alvo]:
            indices_alvo.append(col_num)

    # Fontes para as cores condicionais
    fonte_azul = Font(name="Calibri", size=11, color="0000FF", bold=True) # Azul para > 0%
    fonte_vermelho = Font(name="Calibri", size=11, color="FF0000", bold=True)

    # Percorre as linhas de dados (a partir da linha 5)
    for row in ws.iter_rows(min_row=5, max_row=ws.max_row, min_col=1, max_col=len(arquivo.columns)):
        for cell in row:
            # Aplica fonte padrão para as demais células
            cell.font = Font(name="Calibri", size=11)

            # Se a coluna atual estiver na lista de alvos (% META 3D ou % LW 3D)
            if cell.column in indices_alvo:
                cell.number_format = '0.0%'

                if isinstance(cell.value, (int, float)):
                    if cell.value <0:
                        cell.font = fonte_vermelho
                    else:
                        cell.font = fonte_azul

    # Ajuste automático da largura das colunas
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = max(max_len + 4, 12)

    # Salva o arquivo final
    wb.save(caminho_saida)
    print(f"Relatório formatado e salvo com sucesso em: {caminho_saida}")