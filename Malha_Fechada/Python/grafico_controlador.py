import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go


def divide(x):
    return x / 1000


def porcento(x):
    return (x * 100) / 1023


headers = ["Temperatura (°C)", "Tempo (s)", "Saida para relé (% da rede)", "SetPoint"]
df = pd.read_csv("data05_06_CProporcional30.csv", names=headers)

df["SetPoint"] = 80.0
df["Tempo (s)"] = df["Tempo (s)"].map(divide)

df["Saida para relé (% da rede)"] = df["Saida para relé (% da rede)"].map(porcento)

indices = np.where(df["Temperatura (°C)"].to_numpy() >= 80 * 0.98)

fig = px.line(
    df,
    y=["Temperatura (°C)", "Saida para relé (% da rede)", "SetPoint"],
    x="Tempo (s)",
    title="Gráfico Controlador P Kp = 30 - Setpoint 80°C",
)

fig.add_trace(
 go.Scatter(
 x=[df["Tempo (s)"][indices[0][0]], df["Tempo (s)"][indices[0][0]]],
  y=[0, df["Saida para relé (% da rede)"].max()],
    mode="lines",
     line=dict(color="black", width=2, dash="dash"),
      name="Tempo acomodação (2%)",
   )
 )

fig.update_yaxes(title_text="Temperatura (°C)")

fig.update_layout(font_size=20, legend_font_size=15)

fig.show()


print(
    "Tempo para critério de acomodação de 2% = ",
    df["Tempo (s)"].to_numpy()[indices[0][0]],
)
