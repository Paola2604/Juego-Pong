codigo_usuario=(input("Ingrese el código del usuario: "))
def buscar_usuario(codigo_usuario):
    global x
    x=False
    archivo = open("usuarios.txt","r",encoding="utf-8")
    linea = archivo.readline()
    while linea!="":
        lista=linea.strip().split(',')
        if lista[0] == codigo_usuario:
            numero=int(lista[2])
            diccusuario={"codigousuaio":lista[0],"nombreyap":lista[1],"posinic":numero,"posfin":lista[3]}
            x=True
            return diccusuario
        linea = archivo.readline()
    if(x==False):
        print("El usuario no existe")
        exit(0)
    archivo.close()

def buscarNovedad():
    with open('novedades.txt', 'r') as archivo1:
        line_count = sum(1 for linea in archivo1)
        print(f'Número de líneas: {line_count}')
        diccionario=buscar_usuario(codigo_usuario)
        pos=int(diccionario["posinic"])
        nya=diccionario["nombreyap"]
        posfin=diccionario["posfin"]
        #########carga la primera partida en novedad
        if(pos==0):
            print("es la primera partida")
            posiRegistro=(line_count*30)-30
            print(posiRegistro)
            archivo1.seek(posiRegistro,0)
            print(archivo1.tell())
            nropartida=line_count+1
            reg_sig=0
            reg_ant=pos
            fecha=input("Ingrese fecha: ")
            puntos=input("ingrese puntuacion: ")
            lineas=f"{codigo_usuario},{fecha},{nropartida},{puntos},{reg_sig},{reg_ant}\n"
            archivo1=open("novedades.txt","a",encoding="utf-8")
            archivo1.write(lineas)
            nuevo_registro=f"{codigo_usuario},{nya},{nropartida},{pos}"
            
                ###########################
        else:
            ###########
            print("ya jugo")
            posiRegistro=int((pos*30)-30)
            archivo1.seek(posiRegistro,0)
            print("posicion del registro= ",posiRegistro)
            fecha=input("Ingrese fecha aqui: ")
            puntos=input("Ingrese puntos aqui: ")
            nropartida=(line_count)
            linea2=archivo1.readline()
            lista2=linea2.strip().split(",")
            regsig=int(lista2[4])
            regant=int(lista2[5])
            print(regsig,regant)
            if(regsig==0):##################el registro siguiente es cero, jugo solo una vez
                print("tiene solo 1")
                archivo1.seek(0,2)####se posiciona al final del archivo para cargar el registro
                print("esta es la posicion actual",archivo1.tell())

                ####se carga el nuevo registro de la segunda partida
                lineas=f"{codigo_usuario},{fecha},{nropartida},{puntos},{regsig},{regant}\n"
                archivo2=open("novedades.txt","a",encoding="utf-8")
                archivo2.write(lineas)
                nuevo_registro=f"{codigo_usuario},{nya},{pos},{nropartida}"
            else:
                print("tiene varias")
                while(regsig!=0):
                    posiRegistro2=int(regsig*30)-30
                    archivo1.seek(posiRegistro2,0)
                    linea2=archivo1.readline()
                    lista2=linea2.strip().split(",")
                    regsig=int(lista2[4])
                    print("regsig= ",regsig)
                    if(regsig==0):
                        print("entro")
                        archivo1.seek(0,2)
                        lineas2=f"{codigo_usuario},{fecha},{nropartida},{puntos},{0},{lista2[2]}"
                        archivo1=open("novedades.txt","a",encoding="utf-8")
                        archivo1.write(lineas2)
                        nuevo_registro=f"{codigo_usuario},{nya},{pos},{nropartida}"
                    
        return nuevo_registro

def reemplazar_linea_usuario(codigo_usuario, nueva_linea):
    with open("usuarios.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    with open("usuarios.txt", "w", encoding="utf-8") as archivo:
        for linea5 in lineas:
            lista8 = linea5.strip().split(",")
            if (lista8[0]) == (codigo_usuario):
                archivo.write(nueva_linea +"\n")
            else:
                archivo.write(linea5)

nueva=buscarNovedad()
reemplazar_linea_usuario(codigo_usuario,nueva)




