import pandas as pd

try:
    df = pd.read_csv("C:/Users/2DT/Documents/Projetos/importe-CSV-com-Python/csv/empregoHabilidade.csv")
    print(df.head())  # Mostra as 5 primeiras linhas
    df = pd.read_csv("C:/Users/2DT/Documents/Projetos/importe-CSV-com-Python/csv/empregos.csv")
    print(df.head())
    df = pd.read_csv("C:/Users/2DT/Documents/Projetos/importe-CSV-com-Python/csv/empresas.csv")
    print(df.head())
    df = pd.read_csv("C:/Users/2DT/Documents/Projetos/importe-CSV-com-Python/csv/habilidades.csv")
    print(df.head())
    df = pd.read_csv("C:/Users/2DT/Documents/Projetos/importe-CSV-com-Python/csv/localizacoes.csv")
    print(df.head())

    print("CSV's carregado com sucesso!")
    
except Exception as erro:
    print(f"Erro ao carregar CSV's: {erro}")