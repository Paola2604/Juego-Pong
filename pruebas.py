import tkinter as tk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Crear una ventana de Tkinter
ventana = tk.Tk()
ventana.title("Gráfico 3D con Tkinter")

# Crear un marco para el gráfico
marco_grafico = tk.Frame(ventana)
marco_grafico.pack()

# Crear una función para dibujar el gráfico 3D
def dibujar_grafico():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Aquí puedes personalizar y agregar tus propios datos 3D
    x = [1, 2, 3, 4, 5]
    y = [10, 11, 12, 13, 14]
    z = [20, 21, 22, 23, 24]

    ax.scatter(x, y, z)

    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.set_zlabel('Eje Z')

    plt.show()

# Crear un botón para dibujar el gráfico
boton_dibujar = tk.Button(marco_grafico, text="Dibujar Gráfico 3D", command=dibujar_grafico)
boton_dibujar.pack()

# Iniciar la aplicación
ventana.mainloop()
