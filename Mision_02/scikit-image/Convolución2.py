import numpy as np
import matplotlib.pyplot as plt

# Definición de las señales x y h
x = np.array([1, 2, 3, 4, 5])
h = np.array([-1, 5, 3, -2, 1])

# Cálculo de la convolución
y = np.convolve(x, h)

# Impresión de la salida
print('Salida')
print(y)

# Graficación de las señales
plt.figure(figsize=(12, 6))

# Graficación de la señal x
plt.subplot(3, 1, 1)
plt.stem(x)
plt.title('Señal x')
plt.xlabel('Índice')
plt.ylabel('Amplitud')

# Graficación de la señal h
plt.subplot(3, 1, 2)
plt.stem(h)
plt.title('Señal h')
plt.xlabel('Índice')
plt.ylabel('Amplitud')

# Graficación de la señal y (resultado de la convolución)
plt.subplot(3, 1, 3)
plt.stem(y)
plt.title('Resultado de la convolución (y = x * h)')
plt.xlabel('Índice')
plt.ylabel('Amplitud')

# Ajustar el espacio entre subgráficos
plt.tight_layout()

# Mostrar la gráfica
plt.show()
