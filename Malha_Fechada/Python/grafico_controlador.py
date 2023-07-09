import pandas as pd
import plotly.express as px
import numpy as np


def divide(x):
    return x / 1000


def porcento(x):
    return (x * 100) / 1023


headers = ["Temperatura (°C)", "Tempo (s)", "Saida para relé (% da rede)", "SetPoint"]
df = pd.read_csv("data03_07_P35_I0-005_T60.csv", names=headers)

df["SetPoint"] = 60.0
df["Tempo (s)"] = df["Tempo (s)"].map(divide)

df["Saida para relé (% da rede)"] = df["Saida para relé (% da rede)"].map(porcento)

indices = np.where(df["Temperatura (°C)"].to_numpy() >= 60 * 0.98)

fig = px.line(
    df,
    y=["Temperatura (°C)", "Saida para relé (% da rede)", "SetPoint"],
    x="Tempo (s)",
    title="Gráfico Controlador PI Kp = 35/ Ki = 0,005 - Setpoint 60°C",
)

fig.add_vline(df["Tempo (s)"].to_numpy()[indices[0][0]])

fig.update_yaxes(title_text="Temperatura (°C)")
fig.show()


print(
    "Tempo para critério de acomodação de 2% = ",
    df["Tempo (s)"].to_numpy()[indices[0][0]],
)
