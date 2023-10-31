def detalle(cod,partida,puntA,puntB,fecha):
    with open("archivos/partida_jugador.txt","r",encoding="utf-8") as archivo_partida:
        linea=archivo_partida.readline()
        lista=linea.strip().split(",")
        if lista !="":
          linea=archivo_partida.readline()
          linea_justificada=linea.ljust(40," ")
          print(linea_justificada)
       
    with open("archivos/partida_jugador.txt","w",encoding="utf-8") as archivo_part:
        nuevalinea=f"{cod},{partida},{puntA},{puntB},{fecha}\n"
        archivo_part.write(nuevalinea)
        

