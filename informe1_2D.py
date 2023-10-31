def devolver_nombre_usuario(codigo_usuario):
    aux = 0
    with open("archivos/maestroUsuarios.txt", "r") as arch:
        linea = arch.readline()
        while linea != "" and aux == 0:
            lista = linea.strip().split(",")
            usuario = (lista[0])
            if usuario == codigo_usuario:
                nombre = str(lista[1])
                aux = 1
            else:
                linea = arch.readline()
                aux = 0
    return(nombre)
    
import tkinter as tk
# Crear la ventana
ventana = tk.Tk()
ventana.title("Total Colisiones entre objetos")

# Etiquetas y entradas para usuario y partida
label_usuario = tk.Label(ventana, text="Usuario:")
entry_usuario = tk.Entry(ventana)
label_partida = tk.Label(ventana, text="Número de partida:")
entry_partida = tk.Entry(ventana)

# Botón "Analizar"
def analizar_colisiones():
    codigo_usuario = (entry_usuario.get())
    nombre = devolver_nombre_usuario(codigo_usuario)
    label_resultado.config(text=f"Jugador: {nombre}")
    
    matriz = []
    for x in range(3):
        matriz.append(x)
        matriz[x] = []
        for z in range(4):
            matriz[x].append(z)
            matriz[x][z] = 0

    partida_ingresada =int(entry_partida.get())
    with open("archivos/colisiones.txt", "r") as arch:
        codigo_ingresado=(entry_usuario.get())
        linea = arch.readline()
        while linea != "":
            lista = linea.strip().split(",")
            codigo =(lista[0])
            partida=int(lista[1])
            objeto1=(lista[5])
            parentesis,bola=objeto1.split("(")
            bola=int(bola)
            objeto2=(lista[6])
            pala,parentesis=objeto2.split(")")
            pala=int(pala)
            if(bola==1):
                x=1
            elif(bola==2):
                x=2
            elif(bola==3):
                x=3
            if(pala==1):
                z=1
            elif(pala==2):
                z=2
            if(codigo_ingresado==codigo):
                if(partida==partida_ingresada):
                    matriz[x-1][z-1]+=1
                    linea=arch.readline()
            
            linea=arch.readline()  
    
    
    # Ubicar elementos en la ventana
    total_bola1=matriz[0][0] + matriz[0][1]
    total_bola2=matriz[1][0] + matriz[1][1]
    total_bola3=matriz[2][0]+ matriz[2][1]
    total_pala1= matriz[0][0] + matriz[1][0] + matriz[2][0]
    total_pala2= matriz[0][1] + matriz[1][1] + matriz[2][1]
    
    mejor_pala=""
    peor_pala=""
    if(total_pala1>total_pala2):
        mejor_pala="Pala 1"
        peor_pala="Pala 2"
    else:
        mejor_pala="Pala 2"
        peor_pala= "Pala 1"
    
    lbl_pala.config(text=f"La mejor pala: {mejor_pala}")
    lbl_peorpala.config(text=f"La peor pala: {peor_pala}")

    datos = [
    ["Pala 1", matriz[0][0], matriz[1][0], matriz[2][0], total_pala1],
    ["Pala 2", matriz[0][1], matriz[1][1], matriz[2][1], total_pala2],
    ["Total General", total_bola1, total_bola2, total_bola3,"       "]
   ]
    # Crear una lista de encabezados de columna
    encabezados = ["Objeto Pala", "Pelota 1", "Pelota 2", "Pelota 3", "Total Puntos"]

    # Crear etiquetas para los encabezados de columna
    for col, encabezado in enumerate(encabezados):
        label = tk.Label(ventana, text=encabezado, borderwidth=1, relief="solid")
        label.grid(row=3, column=col, sticky="nsew")

    # Crear datos para la tabla


    # Crear etiquetas para los datos
    for fila, fila_datos in enumerate(datos, start=4):
        for col, dato in enumerate(fila_datos):
            label = tk.Label(ventana, text=dato, borderwidth=1, relief="solid")
            label.grid(row=fila, column=col, sticky="nsew")

    # Ajustar el tamaño de las celdas a su contenido
    for col in range(5):
        ventana.grid_columnconfigure(col, weight=1)





   
    # Iniciar la aplicación
label_usuario.grid(row=0, column=0)
entry_usuario.grid(row=0, column=1)
label_partida.grid(row=1, column=0)
entry_partida.grid(row=1, column=1)
    # Etiqueta para mostrar el resultado del análisis
label_resultado = tk.Label(ventana, text="")
label_resultado.grid(row=7, column=0)
lbl_pala=tk.Label(ventana, text="")
lbl_pala.grid(row=7, column=1)
lbl_peorpala=tk.Label(ventana, text="")
lbl_peorpala.grid(row=7, column=2)
boton_analizar = tk.Button(ventana, text="Analizar", command=analizar_colisiones).grid(row=2, column=0, columnspan=2)
ventana.mainloop()


