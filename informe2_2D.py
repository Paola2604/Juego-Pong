import tkinter as tk
def devolver_nombre_usuario(codigo_usuario):
    aux = 0
    with open("archivos/maestroUsuarios.txt", "r") as arch:
        linea = arch.readline()
        while linea != "" and aux == 0:
            lista = linea.strip().split(",")
            codigo = int(lista[0])
            if codigo == codigo_usuario:
                nombre = str(lista[1])
                aux = 1
            else:
                linea = arch.readline()
                aux = 0
    return nombre

def colisiones_por_usuario_y_anio():
    codigo_ingresado = int(entry_codigo.get())
    nombre = devolver_nombre_usuario(codigo_ingresado)
    result_label.config(text=f"Nombre: {nombre}")

    matriz = []

    for x in range(13):
        matriz.append(x)
        matriz[x] = []
        for z in range(32):
            matriz[x].append(z)
            matriz[x][z] = 0

    

    with open("archivos/colisiones.txt", "r") as arch:
        linea = arch.readline()
        anio_ingresado =int(entry_anio.get())
        while linea != "":
                lista = linea.strip().split(",")
                codigo = int(lista[0])
                fecha=(lista[2])
                dia, mes, anio = fecha.split("/")
                dia=int(dia)
                mes=int(mes)
                anio=int(anio)
                if codigo_ingresado == codigo:
                    if anio_ingresado == anio:
                        
                        matriz[mes - 1][dia - 1] += 1
                        matriz[mes - 1][31] += 1
                        matriz[12][dia - 1] += 1
                
                linea = arch.readline()
        print(matriz[0][1])

    # Limpiar el frame
    for widget in result_frame.winfo_children():
        widget.grid_forget()

    # Nombres de los meses y "Total"
    month_labels = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre", "Total"]

    # Mostrar los nombres de los meses en la primera columna
    for i, month_name in enumerate(month_labels):
        label = tk.Label(result_frame, text=month_name)
        label.grid(row=0, column=i + 1)

    # Agregar etiquetas para los días
    for day_number in range(1, 32):
        day_label = tk.Label(result_frame, text=f"Día {day_number}")
        day_label.grid(row=day_number, column=0)

    # Mostrar los resultados en las columnas correspondientes
    for x in range(13):
        for z in range(32):
            dia = matriz[x][z]
            label = tk.Label(result_frame, text=f"{dia}")
            label.grid(row=z + 1, column=x + 1)
    labeltotal=tk.Label(result_frame,text="Totales").grid(row=32,column=0)
# Crea la ventana de la aplicación
app = tk.Tk()
app.title("Análisis de Colisiones")

# Etiquetas y campos de entrada
label_codigo = tk.Label(app, text="Código de usuario:")
entry_codigo = tk.Entry(app)
label_anio = tk.Label(app, text="Año de la partida:")
entry_anio = tk.Entry(app)
result_label = tk.Label(app, text="Resultados:")

# Botón para iniciar el análisis
analyze_button = tk.Button(app, text="Analizar", command=colisiones_por_usuario_y_anio)

# Crea un frame (Canvas) para mostrar los resultados
result_frame = tk.Canvas(app)
result_frame.grid(row=4, column=0, columnspan=14)

# Agrega una barra de desplazamiento vertical
scrollbar = tk.Scrollbar(app, orient=tk.VERTICAL, command=result_frame.yview)
scrollbar.grid(row=4, column=14, sticky='ns')
result_frame.config(yscrollcommand=scrollbar.set)

# Ubica los elementos en la ventana
label_codigo.grid(row=0, column=0)
entry_codigo.grid(row=0, column=1)
label_anio.grid(row=0, column=2)
entry_anio.grid(row=0, column=3)
analyze_button.grid(row=0, column=4, columnspan=4)
result_label.grid(row=1, column=0, columnspan=14)

# Inicia la aplicación
app.mainloop()
