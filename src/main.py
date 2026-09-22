from processor import processar_dados_vendas
from exporter import exportar_e_formatar_excel

def main():
    
    df_resultado, data_referencia = processar_dados_vendas()
    exportar_e_formatar_excel(df_resultado, data_referencia, caminho_saida="output/relatorio_vendas.xlsx")

if __name__ == "__main__":
    main()