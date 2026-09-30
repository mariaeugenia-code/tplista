class Superheroe:
    def __init__(self, nombre, anio, casa, biografia):
        self.nombre = nombre
        self.anio = anio
        self.casa = casa
        self.biografia = biografia

def resolver_ejercicio_6(lista_superheroes):
    aux = lista_superheroes.inicio
    anterior = None
    
    while aux is not None and aux.info.nombre != "Linterna Verde":
        anterior = aux
        aux = aux.sig
    
    if aux is not None:
        if anterior is None:
            lista_superheroes.inicio = aux.sig
        else:
            anterior.sig = aux.sig
        lista_superheroes.tamanio -= 1

    cantidad_marvel = 0
    cantidad_dc = 0

    aux = lista_superheroes.inicio
    while aux is not None:
        heroe = aux.info
        
        if heroe.nombre == "Wolverine":
            print("Año de aparición de Wolverine:", heroe.anio)
            
        if heroe.nombre == "Dr. Strange":
            heroe.casa = "Marvel"
            
        bio = heroe.biografia.lower()
        if "traje" in bio or "armadura" in bio:
            print(heroe.nombre, "tiene traje o armadura en su bio.")
            
        if heroe.anio < 1963:
            print("Anterior a 1963:", heroe.nombre, "Casa:", heroe.casa)
            
        if heroe.nombre == "Capitana Marvel" or heroe.nombre == "Mujer Maravilla":
            print("La casa de", heroe.nombre, "es", heroe.casa)
            
        if heroe.nombre == "Flash" or heroe.nombre == "Star-Lord":
            print("Info:", heroe.nombre, "- Año:", heroe.anio, "- Casa:", heroe.casa, "- Bio:", heroe.biografia)
            
        letra = heroe.nombre[0].upper()
        if letra == 'B' or letra == 'M' or letra == 'S':
            print("Empieza con B, M o S:", heroe.nombre)
            
        if heroe.casa.upper() == "MARVEL":
            cantidad_marvel += 1
        elif heroe.casa.upper() == "DC":
            cantidad_dc += 1
            
        aux = aux.sig

    print("Total de Marvel:", cantidad_marvel)
    print("Total de DC:", cantidad_dc)



// ejercicio 15

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas

class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

def resolver_ejercicio_15(lista_entrenadores, entrenador_x_ingresado, pokemon_y_ingresado):
    aux = lista_entrenadores.inicio
    
    max_torneos = -1
    nodo_mejor_entrenador = None
    
    while aux is not None:
        entrenador = aux.info
        
        if entrenador.torneos_ganados > max_torneos:
            max_torneos = entrenador.torneos_ganados
            nodo_mejor_entrenador = aux

        total_batallas = entrenador.batallas_ganadas + entrenador.batallas_perdidas
        if total_batallas > 0:
            porcentaje = (entrenador.batallas_ganadas * 100) / total_batallas
            if porcentaje > 79:
                print(entrenador.nombre, "tiene porcentaje de victorias > 79%:", porcentaje)

        if entrenador.torneos_ganados > 3:
            print(entrenador.nombre, "ganó más de 3 torneos.")

        print("Entrenador:", entrenador.nombre, "Torneos:", entrenador.torneos_ganados, "Ganadas:", entrenador.batallas_ganadas, "Perdidas:", entrenador.batallas_perdidas)
        
        aux_poke = aux.sublista.inicio
        
        cantidad_pokemons = 0
        suma_niveles = 0
        tiene_tipos_especificos = False
        nombres_vistos = []
        tiene_repetidos = False
        tiene_tyrantrum_terrakion_wingull = False
        tiene_pokemon_y = False
        
        while aux_poke is not None:
            poke = aux_poke.info
            cantidad_pokemons += 1
            suma_niveles += poke.nivel
            
            print("  - Pokemon:", poke.nombre, "Nivel:", poke.nivel, "Tipo:", poke.tipo, "Subtipo:", poke.subtipo)
            
            if (poke.tipo == "fuego" and poke.subtipo == "planta") or (poke.tipo == "agua" and poke.subtipo == "volador"):
                tiene_tipos_especificos = True
                
            if poke.nombre in nombres_vistos:
                tiene_repetidos = True
            else:
                nombres_vistos.append(poke.nombre)
                
            if poke.nombre == "Tyrantrum" or poke.nombre == "Terrakion" or poke.nombre == "Wingull":
                tiene_tyrantrum_terrakion_wingull = True
                
            if poke.nombre == pokemon_y_ingresado:
                tiene_pokemon_y = True

            aux_poke = aux_poke.sig
            
        print(entrenador.nombre, "tiene", cantidad_pokemons, "Pokémons en total.")
        
        if tiene_tipos_especificos:
            print(entrenador.nombre, "tiene Pokémons fuego/planta o agua/volador.")
            
        if cantidad_pokemons > 0:
            promedio = suma_niveles / cantidad_pokemons
            print("Promedio de nivel de", entrenador.nombre, ":", promedio)
            
        if tiene_repetidos:
            print(entrenador.nombre, "tiene Pokémons repetidos.")
            
        if tiene_tyrantrum_terrakion_wingull:
            print(entrenador.nombre, "tiene a Tyrantrum, Terrakion o Wingull.")
            
        if entrenador.nombre == entrenador_x_ingresado and tiene_pokemon_y:
            print("El entrenador X (", entrenador.nombre, ") SÍ tiene al Pokemon Y (", pokemon_y_ingresado, ")")
        
        aux = aux.sig
        
    if nodo_mejor_entrenador is not None:
        aux_poke = nodo_mejor_entrenador.sublista.inicio
        mayor_nivel = -1
        poke_mayor = None
        while aux_poke is not None:
            if aux_poke.info.nivel > mayor_nivel:
                mayor_nivel = aux_poke.info.nivel
                poke_mayor = aux_poke.info
            aux_poke = aux_poke.sig
            
        if poke_mayor is not None:
            print("Pokémon de mayor nivel del mejor entrenador:", poke_mayor.nombre, "con nivel", poke_mayor.nivel)

    pokemon_a_buscar = "Pikachu"
    contador_tienen_pokemon = 0
    aux = lista_entrenadores.inicio
    while aux is not None:
        aux_poke = aux.sublista.inicio
        while aux_poke is not None:
            if aux_poke.info.nombre == pokemon_a_buscar:
                contador_tienen_pokemon += 1
                break
            aux_poke = aux_poke.sig
        aux = aux.sig
    print(contador_tienen_pokemon, "entrenadores tienen a", pokemon_a_buscar)
 
