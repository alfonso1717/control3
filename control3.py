import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data_base.csv")

df['Horas_estudio'] = pd.to_numeric(df['Horas_estudio'], errors='coerce')
df['Nota'] = pd.to_numeric(df['Nota'], errors='coerce')

st.write("""
# Análisis de horas de estudio
## Relación entre dedicación y rendimiento académico
""")

with st.sidebar:
    st.write("## Ajustes")
    bins_usuario = st.slider("Selecciona número de bins:", 1, 15, 5)
    st.write("Bins elegidos:", bins_usuario)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

axes[0].hist(df["Horas_estudio"], bins=bins_usuario)
axes[0].set_title("Distribución de horas de estudio")
axes[0].set_xlabel("Horas de estudio")
axes[0].set_ylabel("Frecuencia")

aprobado = df[df["Nota"] >= 40]
reprobado = df[df["Nota"] < 40]

cant_aprobado = len(aprobado)
cant_reprobado = len(reprobado)

axes[1].bar(["Aprobados", "Reprobados"], [cant_aprobado, cant_reprobado], color="green")
axes[1].set_title("Comparación de resultados")
axes[1].set_xlabel("Categoría")
axes[1].set_ylabel("Cantidad")

st.pyplot(fig)

st.write("## Vista de los datos cargados")
st.table(df)