import numpy as np
import plotly.graph_objects as go

# Definición de las señales x y h
x = np.array([1, 2, 3, 4, 5])  # Señal x
h = np.array([-1, 5, 3, -2, 1])  # Señal h

# Crear pulsos cuadrados a partir de las señales x y h
def create_square_pulse(signal, length):
    pulse = np.zeros(length)
    start = 0
    for value in signal:
        pulse[start:start + length // len(signal)] = value
        start += length // len(signal)
    return pulse

# Parámetros
length = 50  # Longitud total de las señales para representar los pulsos cuadrados

# Crear los pulsos cuadrados
x_pulse = create_square_pulse(x, length)
h_pulse = create_square_pulse(h, length)

# Calcular la convolución
y = np.convolve(x_pulse, h_pulse)

# Crear los gráficos para la animación
frames = []
for i in range(len(y)):
    convolution_progress = np.zeros(len(y))
    convolution_progress[:i+1] = y[:i+1]

    frame_data = [
        go.Scatter(
            x=np.arange(length),
            y=x_pulse,
            mode='lines',
            fill='tozeroy',
            name='Señal x',
            line=dict(color='blue')
        ),
        go.Scatter(
            x=np.arange(length),
            y=h_pulse,
            mode='lines',
            fill='tozeroy',
            name='Señal h',
            line=dict(color='red')
        ),
        go.Scatter(
            x=np.arange(len(y)),
            y=convolution_progress,
            mode='lines',
            fill='tozeroy',
            name='Resultado de la convolución',
            line=dict(color='green')
        ),
        go.Scatter(
            x=np.arange(len(y)),
            y=np.convolve(x_pulse, np.pad(h_pulse, (0, len(x_pulse) - 1), mode='constant')[:len(y)], mode='full'),
            mode='lines',
            name='Convolución en progreso',
            line=dict(dash='dash', color='orange')
        )
    ]

    frames.append(go.Frame(data=frame_data))

# Configurar la figura para la animación
fig = go.Figure(
    data=[
        go.Scatter(x=np.arange(length), y=x_pulse, mode='lines', fill='tozeroy', name='Señal x', line=dict(color='blue')),
        go.Scatter(x=np.arange(length), y=h_pulse, mode='lines', fill='tozeroy', name='Señal h', line=dict(color='red')),
        go.Scatter(x=np.arange(len(y)), y=[None]*len(y), mode='lines', name='Resultado de la convolución', line=dict(color='green')),
        go.Scatter(x=np.arange(len(y)), y=np.zeros(len(y)), mode='lines', name='Convolución en progreso', line=dict(dash='dash', color='orange'))
    ],
    layout=go.Layout(
        title='Convolución de señales',
        xaxis=dict(title='Índice', range=[-1, len(y)]),
        yaxis=dict(title='Amplitud', range=[-1, max(np.max(x_pulse), np.max(h_pulse), np.max(y))]),
        updatemenus=[dict(
            type='buttons',
            showactive=True,
            buttons=[
                dict(label='Play', method='animate', args=[None, {'frame': {'duration': 300, 'redraw': True}, 'fromcurrent': True}]),
                dict(label='Pause', method='animate', args=[[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}]),
                dict(label='Reset', method='animate', args=[[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}, 'fromcurrent': True}])
            ]
        )]
    ),
    frames=frames
)

# Mostrar la figura
fig.show()
