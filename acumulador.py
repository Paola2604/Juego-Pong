def acumulador():
    with open("archivos/acumulador_partidas.txt","r",encoding="utf-8") as archivo_partidas:
        linea=archivo_partidas.readline()
        if(linea!=""):
            lista=linea.strip().split(",")
            contador=(lista[1])
        return contador           

def reescribir(partida):
    with open("archivos/acumulador_partidas.txt","r",encoding="utf-8") as archivo_partida:
        linea=archivo_partida.readline()
        lista=linea.strip().split(",")
        if lista !="":
            a=lista[0]
       
    with open("archivos/acumulador_partidas.txt","w",encoding="utf-8") as archivo_part:
        nuevalinea=f"{a},{partida}"
        archivo_part.writelines(nuevalinea)