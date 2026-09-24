from processor import processar_dados_vendas
from exporter import exportar_e_formatar_excel
from connectionSheets import carregar_dados_google

def main():
    df_google, df_google_preco = carregar_dados_google()

    df_resultado, data_referencia = processar_dados_vendas(df_google, df_google_preco)
    
    exportar_e_formatar_excel(df_resultado, data_referencia, caminho_saida="output/DESEMPENHO LOJAS - DOCKS.xlsx")

if __name__ == "__main__":
    main()