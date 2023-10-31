from tkinter import *
from tkinter import Button
from tkinter import messagebox
def guardarresp():
    def llamada():  
        respuesta=respuesta_global.get()
        if (respuesta == "a" or respuesta == "A") or (respuesta == "c" or respuesta == "C"):
            messagebox.showwarning("Respuesta incorrecta", "Resta 20 puntos")
              
        else:
            messagebox.showinfo(message="CORRECTO! Suma 50 puntos", title="Respuesta correcta")
        root.destroy()
        archivo=open("archivos/maestro_pregunta.txt","r",encoding="utf-8")
        linea=archivo.readlines()
        with open("archivos/maestro_pregunta.txt","a",encoding="utf-8") as archivo:
            if(linea!=""):
                id_pregunta=1
                desc_pregunta="¿Qué país no limita con Argentina?"
                rta=respuesta
                estado_pregunta=1
            else:
                id_pregunta=1
                desc_pregunta="¿Qué país no limita con Argentina?"
                rta=respuesta
                estado_pregunta=1   
            nuevalinea=f"{id_pregunta},{desc_pregunta},{rta},{estado_pregunta}\n"
            archivo.writelines(nuevalinea)
    
    root = Tk()
    root.title("Ventana de Inicio de Sesión")
    root.geometry("400x350")
    root.resizable(False, False)
    root.config(bg="white")
# Renombrar la variable global
    respuesta_global = StringVar()

    Label(root, text="¿Qué país no limita con Argentina?", font=("Arial", 18), bg="white").grid(row=0, column=0, sticky="e")
    Label(root, text="a: Paraguay", font=("Arial", 18), bg="white").grid(row=1, column=0, sticky="w")
    Label(root, text="b: Colombia", font=("Arial", 18), bg="white").grid(row=2, column=0, sticky="w")
    Label(root, text="c: Chile", font=("Arial", 18), bg="white").grid(row=3, column=0, sticky="w")

# Utiliza la variable global renombrada en el cuadro de texto
    cuadro_respuesta = Entry(root, textvariable=respuesta_global, bg="white", fg="black", font=("Arial", 14))
    cuadro_respuesta.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    boton_respuesta = Button(root, text="Enviar respuesta", font=("arial", 14), width=20, bg="#77C14E", relief=FLAT, command=lambda:[llamada(),root.destroy()])
    boton_respuesta.grid(row=5, columnspan=2, pady=10)

    root.mainloop()
