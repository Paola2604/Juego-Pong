def detalle(cod,partida,puntA,puntB,fecha):
    with open("archivos/partida_jugador.txt","a",encoding="utf-8") as archivo_part:
        nuevalinea=f"{cod},{partida},{puntA},{puntB},{fecha}"
        archivo_part.write(nuevalinea)

def colisiones(cod,partida,fecha,coordenada,observacion):
        with open("archivos/colisiones.txt","a",encoding="utf-8") as archivo_part:
            nuevalinea=f"{cod},{partida},{fecha},{coordenada},{observacion}\n"
            archivo_part.write(nuevalinea)