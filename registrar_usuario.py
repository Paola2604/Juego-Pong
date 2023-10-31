from tkinter import *
from tkinter import messagebox

#-------------funcion registrar usuario------------------------------
def registrar():
    nombreus=nombre.get()
    apellidous=apellido.get()
    username=usuario.get()
    clave=password.get()
    nya=nombreus + " "+ apellidous
    with open("archivos/maestroUsuarios.txt","r",encoding="utf-8") as archivo:
        linea=archivo.readline()
        global x,bandera
        x=0
        bandera=0
        while (linea!=""):
            lista=linea.strip().split(",")
            if(username==lista[2]):
                messagebox.showwarning("Error", "El nombre de usuario ya existe")
                bandera=1
            x+=1
            print(linea)
            linea=archivo.readline()
    id=x+1
    lineas=f"{id},{nya},{username},{clave}\n"
    print(lineas)
    if(bandera==0):
        archivo1=open("archivos/maestroUsuarios.txt","a",encoding="utf-8")
        archivo1.write(lineas)
def cancelar():
    root.destroy()
#--------------- VENTANA PRINCIPAL ----------------------------
root = Tk()
root.title("Registro de Usuario")
root.geometry("300x230")  # Tamaño de la ventana
root.resizable(False, False)  # Ventana no redimensionable
root.config(bg="white")  # Fondo blanco

#------------- FRAME --------------------------------------------------------------
frame=Frame(root,bg="white")
frame.pack()
Label(frame,text="REGISTRO DE USUARIO",font=("arial",16,"underline"),bg="white").grid(row=0)


frame1=Frame(frame,bg="white")
frame1.grid()

nombre=StringVar()
apellido=StringVar()
usuario=StringVar()
password=StringVar()

#---------- LABELS -------------------

Label(frame1,text="Nombre",font=("arial",14),bg="white",pady=2).grid(row=0,column=0,sticky="e")
Label(frame1,text="Apellido:",font=("arial",14),bg="white",pady=2).grid(row=1,column=0,sticky="e")
Label(frame1,text="Usuario:",font=("arial",14),bg="white",pady=2).grid(row=2,column=0,sticky="e")
Label(frame1,text="Clave:",font=("arial",14),bg="white",pady=2).grid(row=3,column=0,sticky="e")
#-------------- CUADROS DE TEXTO ----------------------------------------------------------------
cuadronombre=Entry(frame1,textvariable=nombre)
cuadronombre.grid(row=0,column=1,pady=10,columnspan=4)
cuadronombre.config(background="white", fg="black", justify="right")
#########
cuadroape=Entry(frame1,textvariable=apellido)
cuadroape.grid(row=1,column=1,pady=10,columnspan=4)
cuadroape.config(background="white", fg="black", justify="right")
#########
cuadrouser=Entry(frame1,textvariable=usuario)
cuadrouser.grid(row=2,column=1,pady=10,columnspan=4)
cuadrouser.config(background="white", fg="black", justify="right")
#########
cuadropass=Entry(frame1,textvariable=password)
cuadropass.grid(row=3,column=1,pady=10,columnspan=4)
cuadropass.config(background="white", fg="black", justify="right",show="*")
#------------------- BOTONES --------------------------------------------------------
botoncancelar=Button(frame1,text="Cancelar", font=("arial",12),fg="white",width=8,bg="red",command=cancelar).grid(row=5,column=0)
botonguardar=Button(frame1,text="Guardar", width=8,bg="blue" ,font=("arial",12),fg="white",command=registrar).grid(row=5,column=1)
###########################################
root.mainloop()



