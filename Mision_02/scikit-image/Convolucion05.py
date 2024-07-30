import numpy as np
import plotly.graph_objects as go

# Definir dos pulsos cuadrados
def pulse_square(start, end, length, value=1):
    pulse = np.zeros(length)
    pulse[start:end] = value
    return pulse

# Parámetros para los pulsos cuadrados
pulse_length = 10  # Longitud de la señal
pulse_width = 5    # Ancho del pulso

# Crear los pulsos cuadrados
x_start, x_end = 0, pulse_width
x_pulse = pulse_square(x_start, x_end, pulse_length)

h_start, h_end = 0, pulse_width
h_pulse = pulse_square(h_start, h_end, pulse_length)

# Calcular la convolución
y = np.convolve(x_pulse, h_pulse, mode='full')

# Crear los gráficos para la animación
frames = []
for i in range(len(y)):
    convolution_progress = np.zeros(len(y))
    convolution_progress[:i+1] = y[:i+1]

    frame_data = [
        go.Scatter(
            x=np.arange(pulse_length),
            y=x_pulse,
            mode='lines',
            fill='tozeroy',
            name='Señal x',
            line=dict(color='blue')
        ),
        go.Scatter(
            x=np.arange(pulse_length),
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
        go.Scatter(x=np.arange(pulse_length), y=x_pulse, mode='lines', fill='tozeroy', name='Señal x', line=dict(color='blue')),
        go.Scatter(x=np.arange(pulse_length), y=h_pulse, mode='lines', fill='tozeroy', name='Señal h', line=dict(color='red')),
        go.Scatter(x=np.arange(len(y)), y=[None]*len(y), mode='lines', name='Resultado de la convolución', line=dict(color='green')),
        go.Scatter(x=np.arange(len(y)), y=np.zeros(len(y)), mode='lines', name='Convolución en progreso', line=dict(dash='dash', color='orange'))
    ],
    layout=go.Layout(
        title='Convolución de dos pulsos cuadrados',
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
