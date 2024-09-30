import csv
import matplotlib.pyplot as plt

# Representamos coordenadas como un diccionario de listas con latitudes y longitudes.

def monumentos_dic():
    """
     monumentos(): None -> List[dict]
     Dado el archivo csv de monumentos, crea una lista de diccionarios
     donde cada diccionario es un monumento
    """
    monumentos = []
    with open('monumentos.csv', 'r') as csv_file:
        lector = csv.DictReader(csv_file, delimiter = ';')
        for monumento in lector:
            monumentos.append(monumento)
        csv_file.close()
    return monumentos


def obtener_columna(monumentos,columna,to_float=False,filtrar_vacio=False,to_int=False):
    """
    obtener_columna: List(Dict) String -> List[String]
    Dada una lista de monumentos y una columna(tipo de dato), 
    devuelve una lista con los valores de la columna, se puede decidir si filtrar o no los '', 
    o si se desea convertir los valores a floats
    Ejemplos:
    obtener_columna([{'a':'pichon','b':'casa'}, {'a':'perro','b':'palacio'}],'b') == ['casa','palacio']
    obtener_columna([{'a':'','b':'casa'}, {'a':'perro','b':''}],'b',filtrar_vacio=True) == ['casa']
    obtener_columna([{'a':'2.3','b':'1.2'}, {'a':'2.3','b':'5.6'}],'b',to_float=True) == [1.2,5.6]
    obtener_columna([{'a':'','b':'1.2'}, {'a':'2.3','b':''}],'b',to_float=True,filtrar_vacio=True) == [1.2]
    """
    valores_de_columna = []

    if filtrar_vacio:
        for monumento in monumentos:
            if monumento[columna] != '':
                valores_de_columna.append(monumento[columna])
    else:
        for monumento in monumentos:
            valores_de_columna.append(monumento[columna])

    valores_columna_largo = len(valores_de_columna)

    if to_float:
        for i in range(valores_columna_largo):
            valores_de_columna[i] = float(valores_de_columna[i])

    if to_int:
        for i in range(valores_columna_largo):
            valores_de_columna[i] = int(valores_de_columna[i])

    return valores_de_columna


def contar_materiales(elementos, eslista=False):
    '''
    contar_materiales: List[Dict] -> Dict  o List[]->Dict
    Dada una lista de monumentos, devuelve un diccionario con el número de materiales por monumento.
    Ejemplo:
    contar_materiales([CEMENTO,CEMENTO GRILLADO],True)=={'CEMENTO':2}
    contar_materiales([{"MATERIAL":"CEMENTO"},{"MATERIAL":"CEMENTO GRILLADO"}],False)=={"CEMENTO":2}
    
    '''

    todosmateriales = []
    materiales = {}
    listapalabraslargas = []

    if eslista:
        todosmateriales=elementos
    else:
        todosmateriales = sorted(obtener_columna(elementos, "MATERIAL", filtrar_vacio = True))

    for claves in todosmateriales:
        if claves in materiales:
            materiales[claves] += 1
        else:
            if " " in claves:
                listapalabraslargas.append(claves)
            else:
                materiales[claves] = 1

    clavesdeldic = list(materiales.keys())
    for palabralarga in listapalabraslargas:
        for clave in clavesdeldic:
            if clave in palabralarga:
                materiales[clave] += 1

    return materiales


def graficador(materiales, coordenadastotales, monumentos , top10grafica=False , graficatorta=False):
    
  '''
  graficador: List[Dict] -> List[Dict]
  Dado un diccionario de materiales contados, crea un diccionario con el nombre de cada material y el número. Depende si se desee el top 10 o la gráfica de torta.	
  Ejemplo:
  devuleve el top10 de los materiales más usados.
  devuelve la gráfica de torta de los 3 materiales más usados.
  '''
    
  graficado={}
    
  if top10grafica:
    ordenado = dict(reversed(sorted(materiales.items(), key=lambda item: item[1])))
    clavesdeldic = tuple(ordenado.keys())
    valoresdic = tuple(ordenado.values())
    top10 = {}
    for i in range(0, 10):
        if i <= 8:
            top10[clavesdeldic[i]] = valoresdic[i]
        else:
            top10["OTROS"] = 0
            for i in range(9, len(clavesdeldic)):
                top10["OTROS"] += valoresdic[i]
    graficado = dict(sorted(top10.items(), key=lambda item: item[1]))   
      
  if graficatorta:
      
    torta={}
    listadematgeriales=materiales_respecto_coordenadas(coordenadastotales,monumentos)
    dicmaterialescontados=contar_materiales(listadematgeriales,True)
    ordenado = dict(reversed(sorted(dicmaterialescontados.items(), key=lambda item: item[1])))
      
    if "" in ordenado:
        del ordenado[""]
        
    clavesdeldic = tuple(ordenado.keys())
    valoresdic = tuple(ordenado.values())
      
    if len(clavesdeldic) >= 3:
        for i in range(0,3):
            torta[clavesdeldic[i]] = valoresdic[i]
    else:
        torta=ordenado         
    graficado=dict(sorted(torta.items(), key=lambda item: item[1]))
      
  return graficado

# Información de ubicación - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def coordenadas_por_elemento_diccionario(elemento):
    
    """
    coordenadas_por_elemento_diccionario: Dict -> List[Float]
    Dado un elemento de un diccionario, devuelve una lista con las coordenadas del elemento.
    Ejemplo:
    coordenadas_por_elemento_diccionario({"a":0,'LATITUD':32.123,'LONGITUD':-58.123}) == [32.123,-58.123]
    coordenadas_por_elemento_diccionario({"a":0,'LATITUD':32.123,'LONGITUD':-58.123,'MATERIAL':'piedra'}) == [32.123,-58.123]    
    coordenadas_por_elemento_diccionario({'LATITUD':435.2345,'LONGITUD': -432452.2345,'MATERIAL':'piedra'}) == [435.2345,-432452.2345]    
    """
    
    resultado_latitudes = ""
    resultado_longitudes = ""

    if elemento['LATITUD'] != "":
        resultado_latitudes=float(elemento['LATITUD'])
        resultado_longitudes=float(elemento['LONGITUD'])

    return [resultado_latitudes,resultado_longitudes]


def buscador_indvidual_coordenadas(monumentos, coordenadas): 
    
    """
    buscador_indvidual_coordenadas: List[Dict] List[] -> List[Dict]
    Dado un diccionario de monumentos y un diccionario con coordenadas, devuelve una lista de materiales.
    Ejemplo:
    buscador_indvidual_coordenadas([{'a':0,'LATITUD':32.123,'LONGITUD':-58.123,'MATERIAL':'piedra'},{'a':1, 'LATITUD':99.234,'LONGITUD':1.234,'MATERIAL':'oro'}],[32.123,-58.123]) == 'piedra'
    buscador_indvidual_coordenadas([{'a':0,'LATITUD':32.123,'LONGITUD':-58.123,'MATERIAL':''},{'a':1, 'LATITUD':99.234,'LONGITUD':1.234,'MATERIAL':'piedra'}],[32.123,-58.123])==''
    buscador_indvidual_coordenadas([{'a':0,'LATITUD':32.123,'LONGITUD':-58.123,'MATERIAL':'oro'},{'a':1, 'LATITUD':99.234,'LONGITUD':1.234,'MATERIAL':'piedra'}],[32.123,-58.123])=='oro'
    """
    
    materiales = ''
    salida = 0

    while salida != 1:
        for elementos in monumentos:
            if  coordenadas_por_elemento_diccionario(elementos) == coordenadas:
                materiales = elementos["MATERIAL"]
                salida = 1
        salida = 1
    return materiales

def materiales_respecto_coordenadas(totalcoordenadas,monumentos):
    """
    materiales_respecto_coordenadas: Dict[List] List[Dict] -> List[]
    Dado un diccionario de coordenadas y una lista de monumentos, devuelve una lista.
    Ejemplos:
    materiales_respecto_coordenadas({'lat':[32.123,43.2333],'lon':[-58.123,-43.2333]},[{'LATITUD':32.123,'LONGITUD':-58.123,'MATERIAL':'piedra'},{'LATITUD':43.2333,'LONGITUD':-43.2333,'MATERIAL':'oro'}]) == ['piedra','oro']
    """
    
    totalesmateriales=[]
    latitudes = totalcoordenadas["lat"]
    longitudes = totalcoordenadas["lon"]
    
    for i in range(0,len(totalcoordenadas["lat"])):
        coordenadas = [float(latitudes[i]),float(longitudes[i])]
        totalesmateriales.append(buscador_indvidual_coordenadas(monumentos,coordenadas))
        
    return totalesmateriales


def coordenadas_por_cantidad_de_objetos(monumentos,limitador):
    """ 
    coordenadas_por_cantidad_de_objetos: List[int] -> Dict(Coordenadas)
    donde coordenadas es: List[float]
    Dado un intervalo de enteros, devuelve un diccionario con las coordenadas de los monumentos que tengan 
    una cantidad de objetos entre ese intervalo
    Ejemplo: 
    coordenadas_por_cantidad_de_objetos((10,15))=={'lat':[-34.57726337495626, -34.57642343306996, -34.57642343306996], 'lon': [-58.429310773058354, 
    -58.41177107651361, -58.41177107651361]}
    coordenadas_por_cantidad_de_objetos((0,0))=={'lat':[],'lon':[]}
    coordenadas_por_cantidad_de_objetos((100,100))=={'lat:':[],'lon':[]}
    coordenadas_por_cantidad_de_objetos((5,5))=={'lat': [-34.57296045683345, -34.562488436456256], 'lon': [-58.41922807306269, 
    -58.45483961383647]}
    """

    resultado_latitudes = []
    resultado_longitudes = []
    menor, mayor = limitador
    for monumento in monumentos:
        cantidad_objetos = int(monumento['CANTIDAD_OBJETOS'])
        if cantidad_objetos <= mayor and cantidad_objetos >= menor and monumento[
                'LATITUD'] != "":
            resultado_latitudes.append(float(monumento['LATITUD']))
            resultado_longitudes.append(float(monumento['LONGITUD']))

    return {'lat': resultado_latitudes, 'lon': resultado_longitudes}


def coordenadas_por_columna(monumentos,columna, elementos_seleccionados):
    
    """
    coordenadas_por_columna(str,List[str])->Dic
    Dada una columna y una lista de elementos, devuelve las coordenadas de los monumentos 
    filtrandolos por los elementos seleccionadaos como un diccionario
    Ejemplo:
    coordenadas_por_columna('MATERIAL',['FIBROCEMENTO'])
    {'lat': [-34.62231365012345, -34.60820167772438, -34.63636013663657, -34.603694227045764, 
    -34.590083360820245, -34.61648285649215, -34.62948768324498, -34.57642343306996], 'lon': 
    [-58.473507224857585, -58.373573345960764, -58.444334694272904, -58.38292044962602, -58.500902093893195, 
    -58.381571440181396, -58.37066543894277, -58.41177107651361]}
    """

    resultado_latitudes = []
    resultado_longitudes = []
    for monumento in monumentos:
        if monumento[columna] in elementos_seleccionados and monumento[
                'LATITUD'] != "":
            resultado_latitudes.append(float(monumento['LATITUD']))
            resultado_longitudes.append(float(monumento['LONGITUD']))

    return {'lat': resultado_latitudes, 'lon': resultado_longitudes}


def columna_sin_duplicados(monumentos,columna):
    """columna_sin_duplicados: List(Dict) String -> List
    Dada una columna, devuelve la misma en orden y filtrando los elementos repetidos
    Ejemplos:
    columna_sin_duplicados([{'a':'pichon','b':'casa'}, {'a':'perro','b':'casa'}],'b') == ['casa'])
    columna_sin_duplicados([{'a':'pichon','b':'casa'}, {'a':'perro','b':'palacio'}],'a') == ['perro','pichon'])
    columna_sin_duplicados([{'a':'','b':'casa'}, {'a':'perro','b':''}],'b') == ['casa'])
    """

    valores_de_columna = obtener_columna(monumentos,columna,filtrar_vacio = True)
    columna_filtrada = []

    for valor in valores_de_columna:
        if valor not in columna_filtrada:
            columna_filtrada.append(valor)

    columna_filtrada.sort()
    if columna == "COMUNA":
        columna_filtrada = columna_filtrada[:15]
        
    return columna_filtrada


def numero_comuna(comuna):
    """
    numero_de_comuna: str -> int
    Dada una comuna, devuelve el número de la misma
    Ejemplos:
    numero_comuna('COMUNA 1') == 1
    numero_comuna('COMUNA 10') == 10
    numero_comuna('COMUNA11') == ''
    """
    numero = ""
    if " " in comuna:
        numero = int(comuna.split()[1])
    return numero


def frecuencia_rel_abs_comuna(monumentos,ncomuna):
    """
    frecuencia_rel_abs_comuna(int)->List[float,float]
    Dada una comuna, devuelve la frecuencia relativa y absoluta de la cantidad de monumentos que hay en ella
    Ejemplos:
    frecuencia_rel_abs_comuna("COMUNA 1") == [413, 18.495]
    frecuencia_rel_abs_comuna("COMUNA 10") == [53, 2.373]
    frecuencia_rel_abs_comuna("COMUNA11") == [0, 0.0]
    """
    lista_comunas = obtener_columna(monumentos, 'COMUNA')
    total_comunas = len(obtener_columna(monumentos, 'COMUNA'))
    frecuencia_abs: int = 0
    for comuna in lista_comunas:
        if comuna == ncomuna:
            frecuencia_abs += 1
    frecuencia_rel = round((frecuencia_abs / total_comunas) * 100, 3)

    return [frecuencia_abs, frecuencia_rel]


def data_comunas(monumentos):
    """
    data_comunas()->List[Dato_comuna]
    Donde Dato_comuna es: {'comuna':str,'frec_rel':str,'frec_absoluta':str}
    Devuelve una lista de Dato_comuna
    Ejemplo:
    Devuelve todo el set de datos de las comunas
    """
    comunas = sorted(columna_sin_duplicados(monumentos,'COMUNA'), key=numero_comuna)
    data_ = []
    for comuna in comunas:
        frecuencia_rel = frecuencia_rel_abs_comuna(monumentos,comuna)[1]
        frecuencia_abs = frecuencia_rel_abs_comuna(monumentos,comuna)[0]
        data_.append({
            'Comuna': comuna,
            'Porcentaje de monumentos': f" {frecuencia_rel}%",
            'Cantidad de monumentos': frecuencia_abs
        })
    return data_


def union_coordenadas(coordenadas, diccionario_seleccion):
    """
    union_coordenadas: Dict Dict -> Dict
    Dado un diccionario de coordenadas y un diccionario de seleccion, devuelve las coordenas.
    Ejemplos:
    union_coordenadas({'lat':[],'lon':[]},{'lat':[],'lon':[]}) == {'lat': [], 'lon': []})
    union_coordenadas({'lat':[1,2],'lon':[5,6]},{'lat':[2,4],'lon':[5,6,7]}) == {'lat': [1, 2, 2, 4], 'lon': [ 5, 6, 5, 6, 7]})
    """
    coordenadas['lat'] = coordenadas['lat'] + diccionario_seleccion['lat']
    coordenadas['lon'] = coordenadas['lon'] + diccionario_seleccion['lon']

    return coordenadas


def interseccion_coordenadas(coordenadas, diccionario_seleccion):
    """
    interseccion_coordenadas: Dict Dict -> Dict
    Dado dos diccionarios con coordenadas, devuelve un diccionario con las coordenadas 
    que se encuentran en ambos diccionarios.
    Ejemplos: 
    interseccion_coordenadas({'lat':[1],'lon':[4]},{'lat':[2],'lon':[7]}) == {'lat': [], 'lon': []}
    interseccion_coordenadas({'lat':[],'lon':[]},{'lat':[1,2],'lon':[3,4]}) == {'lat': [1,2], 'lon': [3, 4]}
    interseccion_coordenadas({'lat':[5,6],'lon':[9,2]},{'lat':[6,7],'lon':[9,4]} == {'lat': [6],'lon': [9]}
    """

    if coordenadas['lat'] == [] and coordenadas['lon'] == []:
        coordenadas['lat'] = coordenadas['lat'] + diccionario_seleccion['lat']
        coordenadas['lon'] = coordenadas['lon'] + diccionario_seleccion['lon']

    #Planteo un intento de interseccion
    else:
        interseccion_coordenadas = {'lat': [], 'lon': []}
        largo_coordenada = len(coordenadas['lat'])
        largo_seleccion = len(diccionario_seleccion['lat'])
        for i in range(largo_coordenada):
            for j in range(largo_seleccion):
                if coordenadas['lat'][i] == diccionario_seleccion['lat'][j] and coordenadas['lon'][i] == diccionario_seleccion['lon'][j]:
                    interseccion_coordenadas['lat'].append(diccionario_seleccion['lat'][j])
                    interseccion_coordenadas['lon'].append(diccionario_seleccion['lon'][j])

        coordenadas = interseccion_coordenadas

    return coordenadas

