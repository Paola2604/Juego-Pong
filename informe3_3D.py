def devolver_nombre_usuario(codigo_usuario):
    aux = 0
    with open("archivos/maestroUsuarios.txt", "r") as arch:
        linea = arch.readline()
        while linea != "" and aux == 0:
            lista = linea.strip().split(",")
            usuario = int((lista[0]))
            if usuario == codigo_usuario:
                nombre = str(lista[1])
                aux = 1
            else:
                linea = arch.readline()
                aux = 0
    return(nombre)
    
def partidas(codigo_usuario,partida_ingresada):
    cantpartidas=0
    with open("archivos/colisiones.txt", "r") as arch:
        linea = arch.readline()
        while linea != "":
            lista = linea.strip().split(",")
            usuario=int(lista[0])
            fecha = lista[2]
            dia, mes, anio = fecha.split("/")
            dia = int(dia)
            mes = int(mes)
            anio = int(anio)
            objeto1 = lista[5]
            parentesis, bola = objeto1.split("(")
            bola = int(bola)
            objeto2 = lista[6]
            pala, parentesis = objeto2.split(")")
            pala = int(pala)
            partida=int(lista[1])
            if(usuario==codigo_usuario) and (partida== partida_ingresada):
                with open ("archivos/guardar_partidas.txt","a") as archivo:
                    archivo.write(",".join([str(usuario),str(anio),str(bola),str(pala),str(partida),str(mes),("\n")]))
                cantpartidas+=1
            linea = arch.readline()
        print(cantpartidas)
    return cantpartidas

def analizar_colisiones():
    codigo_ingresado = int(input("Ingrese código de usuario: "))
    nombre = devolver_nombre_usuario(codigo_ingresado)
    print(f"Jugador: {nombre}")

    partida_ingresada = int(input("Ingrese partida: "))
    cantidad_partidas=partidas(codigo_ingresado,partida_ingresada)
    anio_ingresado = int(input("Ingrese año: "))

    # Inicializar la matriz tridimensional
    
    # Número de meses
 # Número de objetos
    matriz=[]

    for x in range(cantidad_partidas):
        matriz.append(x)
        matriz[x]=[]
        for z in range (12):
            matriz[x].append(z)
            matriz[x][z]=[]
            for y in range(5):
                matriz[x][z].append(y)
                matriz[x][z][y]=0

    with open("archivos/guardar_partidas.txt", "r") as arch:
        linea = arch.readline()
        while linea != "":
            lista = linea.strip().split(",")
            codigo = int(lista[0])
            anio = int(lista[1])
            mes=int(lista[5])
            bola = int(lista[2])
            pala = int(lista[3])
            partida=int(lista[4])
            if partida_ingresada == partida and codigo_ingresado == codigo and anio_ingresado == anio:
                if(bola==1):
                    print("hola")
                    matriz[cantidad_partidas - 1][mes - 1][bola - 1] += 1
                if(bola==2):
                    matriz[cantidad_partidas - 1][mes - 1][bola - 1] += 1 

            linea = arch.readline()

    # Imprimir resultados
    for x in range(cantidad_partidas):
        for y in range(12):
            for z in range(5):
                print(f"Partida {x + 1}, Mes {y + 1}, Objeto {z + 1}: {matriz[x][y][z]} colisiones")

analizar_colisiones()




    


