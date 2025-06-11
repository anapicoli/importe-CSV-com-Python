import pandas as pd
import mysql.connector

# conexão com o banco
conn = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="compensasao"
)
cursor = conn.cursor()

# função auxiliar
def inserir_csv(tabela, arquivo):
    df = pd.read_csv(arquivo)
    for _, row in df.iterrows():
        colunas = ", ".join(row.index)
        valores = ", ".join(["%s"] * len(row))
        sql = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
        cursor.execute(sql, tuple(row))
    conn.commit()

# inserir dados
inserir_csv("empresas", "empresas.csv")
inserir_csv("localizacoes", "localizacoes.csv")
inserir_csv("empregos", "empregos.csv")
inserir_csv("habilidades", "habilidades.csv")
inserir_csv("empregoHabilidade", "empregoHabilidade.csv")

cursor.close()
conn.close()