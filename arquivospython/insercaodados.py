import pandas as pd
import mysql.connector

# conexão com o banco
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="compensasao"
)
cursor = conn.cursor()

# função auxiliar
def inserir_csv(tabela, arquivo):
    df = pd.read_csv(arquivo)
    for _, row in df.iterrows():
        colunas = ", ".join(row.index)
        valores = ", ".join(["%s"] * len(row))
        sql = f"INSERT IGNORE INTO {tabela} ({colunas}) VALUES ({valores})"
        cursor.execute(sql, tuple(row))
    conn.commit()

# inserir dados
inserir_csv("empresas", "C:/Users/2DT/Documents/Projetos/importe-CSV-com-Python/csv/empresas.csv")
inserir_csv("localizacoes", "C:/Users/2DT/Documents/Projetos/importe-CSV-com-Python/csv/localizacoes.csv")
inserir_csv("empregos", "C:/Users/2DT/Documents/Projetos/importe-CSV-com-Python/csv/empregos.csv")
inserir_csv("habilidades", "C:/Users/2DT/Documents/Projetos/importe-CSV-com-Python/csv/habilidades.csv")
inserir_csv("empregoHabilidade", "C:/Users/2DT/Documents/Projetos/importe-CSV-com-Python/csv/empregoHabilidade.csv")

print("Concluído!")

cursor.close()
conn.close()