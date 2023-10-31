from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Button
import datetime
import juego
import acumulador

def limpiarCampos():
    minombre.set("")  
    mipassword.set("") 

def ingresar():
    # Función para manejar el ingreso de usuario
    usuario = minombre.get()
    contraseña = mipassword.get()
    # Realizar acciones de autenticación aquí
    with open("archivos/maestroUsuarios.txt","r",encoding="utf-8") as archivo:
        linea=archivo.readline()
        global x
        x=0
        clave=StringVar
        user=StringVar
        while (linea!=""):
            lista=linea.strip().split(",")
            user=(lista[2])
            clave=(lista[3])
            cod=lista[0]
            if(user==usuario) and (clave==contraseña):
                root.destroy()
                partida=acumulador.acumulador()
                y=int(partida)+1
                fecha = datetime.date.today()
                fecha_formateada = fecha.strftime('%d/%m/%Y')
                acumulador.reescribir(y)
                with open("archivos/compartir_usuario.txt","w",encoding="utf-8") as archivo:
                    nuevalinea=f"{cod},{y},{fecha_formateada}"
                    archivo.writelines(nuevalinea)
                juego.main()
                x=1
           
            linea=archivo.readline()
        if(x==0):
            messagebox.showwarning("Datos incorrectos", "Verifique los datos ingresados")
            limpiarCampos()
fecha=datetime.date.today()
    
def ejecutar_modulo2():
    root.destroy()
    try:
        exec(open("registrar_usuario.py").read())  # Ejecuta el contenido de registrar_usuario.py
        
    except FileNotFoundError:
        print("El archivo registrar_usuario.py no se encontró.")
            
# Crear una instancia de la ventana principal
root = Tk()
root.title("Ventana de Inicio de Sesión")
root.geometry("400x350")  # Tamaño de la ventana
root.resizable(False, False)  # Ventana no redimensionable
root.config(bg="white")  # Fondo blanco

# Cargar la imagen
imagen = PhotoImage(file="imagenes/juegopy.png")
imagen_redimensionada = imagen.subsample(4, 4)

# Crear un Label para la imagen
label_imagen = Label(root, image=imagen_redimensionada, bg="white")
label_imagen.pack()

# Crear un Frame para los campos de entrada
frame_entrada = Frame(root, bg="white")
frame_entrada.pack(expand=True, pady=10)

minombre=StringVar()
mipassword=StringVar() 
# Etiqueta y cuadro de texto para el nombre de usuario
Label(frame_entrada, text="Usuario:", font=("Arial", 18), bg="white").grid(row=0, column=0, sticky="e")
cuadro_usuario = Entry(frame_entrada, textvariable=minombre, bg="white", fg="black", font=("Arial", 14))
cuadro_usuario.grid(row=0, column=1, padx=10, pady=10, sticky="w")

# Etiqueta y cuadro de texto para la contraseña
Label(frame_entrada, text="Contraseña:", font=("Arial", 18), bg="white").grid(row=1, column=0, sticky="w")
cuadro_password = Entry(frame_entrada, textvariable=mipassword, bg="white", fg="black", font=("Arial", 14), show="*")
cuadro_password.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Botón de ingreso
boton_ingreso = Button(frame_entrada, text="Ingresar",font=("arial",14), width=20, bg="#77C14E",relief=FLAT, command=ingresar)
boton_ingreso.grid(row=2, columnspan=2, pady=10)

# Etiqueta "¿Sos nuevo?" y "Registrarse" alineadas una al lado de la otra
Label(frame_entrada, text="¿Sos nuevo?", font=("Arial", 14), bg="white").grid(row=3, column=0, sticky="e")
boton_registro = Button(frame_entrada, text="Registrate aquí", font=("Arial", 14, "underline"), fg="blue", bg="white",bd=0, relief=FLAT,command=ejecutar_modulo2)
boton_registro.grid(row=3,column=1, pady=10, sticky="w")
"""registrar=Button(frame_entrada, text="Registrarse", font=("Arial", 14, "underline"), fg="blue", bg="white",style="MyButton.Tbutton").grid(row=3, column=1, sticky="w")"""

# Configurar el espacio en el frame de entrada para que todo se centre verticalmente
frame_entrada.grid_rowconfigure(4, weight=1)
frame_entrada.grid_columnconfigure(0, weight=1)
root.attributes("-topmost", True)
# Iniciar el bucle principal de la aplicación
root.mainloop()
