import gspread
from google.oauth2.service_account import Credentials
from gspread_dataframe import get_as_dataframe
import pandas as pd


def carregar_dados_google():
    # Definir os escopos de acesso
    escopos = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly"
    ]

    # Carregar o arquivo de credenciais 
    creds = Credentials.from_service_account_file("credentials.json", scopes=escopos)
    cliente = gspread.authorize(creds)

    planilha = cliente.open_by_bey("1BVK5U7UVBbnwWLJ7bmr9mv_rIzEXWdhTuu1PzjsMxtU/edit?gid=964581098#gid=964581098")

    aba = planilha.worksheet("COMPARAÇÃO")
    aba_confere_preco = planilha.worksheet("REALIZADO 2026")

    # Transformar os dados da aba diretamente em um DataFrame do Pandas
    df_google = get_as_dataframe(aba)
    df_google_preco = get_as_dataframe(aba_confere_preco)

    # Limpar linhas ou colunas vazias que o Sheets puxa por padrão
    df_google = df_google.dropna(how="all").dropna(axis=1, how="all")
    df_google_preco = df_google_preco.dropna(how="all").dropna(axis=1, how="all")

    print(df_google.head())

    return df_google, df_google_preco