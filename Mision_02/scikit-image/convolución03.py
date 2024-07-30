import numpy as np
import plotly.graph_objects as go

# Definición de las señales x y h
x = np.array([1, 2, 3, 4, 5])
h = np.array([-1, 5, 3, -2, 1])

# Cálculo de la convolución
y = np.convolve(x, h)

# Crear el gráfico de la señal x
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=np.arange(len(x)),
    y=x,
    mode='lines+markers',
    name='Señal x'
))

# Crear el gráfico de la señal h
fig.add_trace(go.Scatter(
    x=np.arange(len(h)),
    y=h,
    mode='lines+markers',
    name='Señal h'
))

# Crear el gráfico de la señal y (resultado de la convolución)
fig.add_trace(go.Scatter(
    x=np.arange(len(y)),
    y=y,
    mode='lines+markers',
    name='Resultado de la convolución (y = x * h)'
))

# Actualizar el layout del gráfico
fig.update_layout(
    title='Gráfico de la convolución de señales',
    xaxis_title='Índice',
    yaxis_title='Amplitud',
    legend_title='Señales',
    template='plotly'
)

# Mostrar el gráfico
fig.show()
