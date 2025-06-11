import pandas as pd
import numpy as np

# dataset original
df = pd.read_csv("global_ai_job_market.csv")

# renomear e selecionar colunas úteis
df = df.rename(columns={
    "job_title": "nmEmprego",
    "experience_level": "nivelExp",
    "salary_in_usd": "salarioDol",
    "company_name": "nmEmpresa",
    "company_location": "nmPais",
    "company_industry": "setorIndustria",
    "skills": "habilidades"
})

# id automático
df["idEmpresa"] = df.groupby(["nmEmpresa", "setorIndustria"]).ngroup() + 1
df["idLoc"] = df.groupby(["nmPais"]).ngroup() + 1
df["idEmprego"] = df.index + 1

# separação de tabelas
empresas = df[["idEmpresa", "nmEmpresa", "setorIndustria"]].drop_duplicates()
localizacoes = df[["idLoc", "nmPais"]].drop_duplicates()
localizacoes["nmCidade"] = "Desconhecida"  # Se não houver cidades

empregos = df[["idEmprego", "nmEmprego", "nivelExp", "salarioDol", "idEmpresa", "idLoc"]]

# habilidades (N:N)
habilidade_dict = {}
empregoHabilidade = []
idHabilidade = 1

for idx, row in df.iterrows():
    if pd.isna(row["habilidades"]):
        continue
    habilidades = [h.strip().capitalize() for h in row["habilidades"].split(",")]
    for h in habilidades:
        if h not in habilidade_dict:
            habilidade_dict[h] = idHabilidade
            idHabilidade += 1
        empregoHabilidade.append({
            "id": len(empregoHabilidade) + 1,
            "idEmprego": row["idEmprego"],
            "idHabilidade": habilidade_dict[h]
        })

habilidades_df = pd.DataFrame(list(habilidade_dict.items()), columns=["nmHabilidade", "idHabilidade"])
habilidades_df = habilidades_df[["idHabilidade", "nmHabilidade"]]
empregoHabilidade_df = pd.DataFrame(empregoHabilidade)

# salvar CSV
empresas.to_csv("empresas.csv", index=False)
localizacoes.to_csv("localizacoes.csv", index=False)
empregos.to_csv("empregos.csv", index=False)
habilidades_df.to_csv("habilidades.csv", index=False)
empregoHabilidade_df.to_csv("empregoHabilidade.csv", index=False)