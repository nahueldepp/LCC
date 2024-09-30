import monumentos_data as md


def test_obtener_columna():
  assert(md.obtener_columna([{"a":"pichon","b":"casa"},{"a":"perro","b":"palacio"}], "b") == ["casa","palacio"])
  assert(md.obtener_columna([{"a":"123","b":"casa"},{"a":"567","b":"palacio"}],"a") == ["123","567"])
  assert(md.obtener_columna([{"a":"","b":"casa"},{"a":"perro","b":""}],"a") == ["","perro"])

def test_coordenadas_por_cantidad_de_objetos():
  assert(md.coordenadas_por_cantidad_de_objetos(md.monumentos_dic(),(10,15)) == {'lat': [-34.57726337495626, -34.57642343306996, -34.57642343306996], 
  'lon': [-58.429310773058354, 
  -58.41177107651361, -58.41177107651361]})
  assert (md.coordenadas_por_cantidad_de_objetos(md.monumentos_dic(),(0,0))=={'lat':[],'lon':[]})
  assert(md.coordenadas_por_cantidad_de_objetos(md.monumentos_dic(),(100,100))=={'lat': [], 'lon': []})


def test_coordenadas_por_columna():
  assert(md.coordenadas_por_columna(md.monumentos_dic(),'MATERIAL',['FIBROCEMENTO']) == {'lat': [-34.62231365012345, -34.60820167772438, 
  -34.63636013663657, 
  -34.603694227045764, -34.590083360820245, -34.61648285649215, -34.62948768324498, -34.57642343306996], 'lon': 
   [-58.473507224857585, 
  -58.373573345960764, -58.444334694272904, -58.38292044962602, -58.500902093893195, -58.381571440181396, -58.37066543894277, 
  -58.41177107651361]})
  assert(md.coordenadas_por_columna(md.monumentos_dic(),"MATERIAL",['PIEDRA TOBA']) == {'lat': [-34.58946607638585], 'lon': [-58.42508060293869]})


def test_columna_sin_duplicados():
  assert (md.columna_sin_duplicados([{'a':'pichon','b':'casa'}, {'a':'perro','b':'casa'}],'b') == ['casa'])
  assert (md.columna_sin_duplicados([{'a':'pichon','b':'casa'}, {'a':'perro','b':'palacio'}],'a') == ['perro','pichon'])
  assert (md.columna_sin_duplicados([{'a':'','b':'casa'}, {'a':'perro','b':''}],'b') == ['casa'])

def test_numero_comuna():
  assert(md.numero_comuna('COMUNA 1')  == 1)
  assert(md.numero_comuna('COMUNA 10') == 10)
  assert(md.numero_comuna('COMUNA11')  == '')

def test_frecuencia_rel_abs_comuna():
  assert (md.frecuencia_rel_abs_comuna(md.monumentos_dic(),"COMUNA 1") == [413, 18.495])
  assert (md.frecuencia_rel_abs_comuna(md.monumentos_dic(),"COMUNA 10") == [53, 2.373])
  assert (md.frecuencia_rel_abs_comuna(md.monumentos_dic(),"COMUNA11") == [0, 0.0])

def test_union_coordenadas():
  assert(md.union_coordenadas({'lat':[],'lon':[]},{'lat':[],'lon':[]}) == {'lat': [], 'lon': []})
  assert(md.union_coordenadas({'lat':[1,2],'lon':[5,6]},{'lat':[2,4],'lon':[5,6,7]}) == {'lat': [1, 2, 2, 4], 'lon': [ 5, 6, 5, 6, 7]})
  assert(md.union_coordenadas({'lat':[34,11],'lon':[11,45]},{'lat':[34,11],'lon':[11,45]}) == {'lat': [34, 11, 34, 11], 'lon': [11, 
  45, 11, 45]})

def test_interseccion_coordenadas():
  assert(md.interseccion_coordenadas({'lat':[1],'lon':[4]},{'lat':[2],'lon':[7]}) == {'lat': [], 'lon': []})
  assert(md.interseccion_coordenadas({'lat':[],'lon':[]},{'lat':[1,2],'lon':[3,4]}) == {'lat': [1, 2], 'lon': [3, 4]})
  assert(md.interseccion_coordenadas({'lat':[6,9],'lon':[9,2]},{'lat':[6,7],'lon':[9,4]}) == {'lat': [6], 'lon': [9]})

def test_coordenadas_por_elemento_diccionario():
  assert (md.coordenadas_por_elemento_diccionario({"a":0,'LATITUD':32.123,'LONGITUD':-58.123}) == [32.123,-58.123])
  assert(md.coordenadas_por_elemento_diccionario({"a":0,'LATITUD':32.123,'LONGITUD':-58.123,'MATERIAL':'piedra'}) == [32.123,-58.123])
  assert(md.coordenadas_por_elemento_diccionario({'LATITUD':435.2345,'LONGITUD': -432452.2345,'MATERIAL':'piedra'}) == [435.2345,-432452.2345])

def test_buscador_indvidual_coordenadas():
  assert(md.buscador_indvidual_coordenadas([{'a':0,'LATITUD':32.123,'LONGITUD':-58.123,'MATERIAL':'piedra'},{'a':1, 'LATITUD':99.234,'LONGITUD':1.234,'MATERIAL':'oro'}],[32.123,-58.123]) == 'piedra')
  assert(md.buscador_indvidual_coordenadas([{'a':0,'LATITUD':32.123,'LONGITUD':-58.123,'MATERIAL':''},{'a':1, 'LATITUD':99.234,'LONGITUD':1.234,'MATERIAL':'piedra'}],[32.123,-58.123])=='')
  assert(md.buscador_indvidual_coordenadas([{'a':0,'LATITUD':32.123,'LONGITUD':-58.123,'MATERIAL':'oro'},{'a':1, 'LATITUD':99.234,'LONGITUD':1.234,'MATERIAL':'piedra'}],[32.123,-58.123])=='oro')

def test_materiales_respecto_coordenadas():
  assert( md.materiales_respecto_coordenadas({'lat':[32.123,43.2333],'lon':[-58.123,-43.2333]},[{'LATITUD':32.123,'LONGITUD':-58.123,'MATERIAL':'piedra'},{'LATITUD':43.2333,'LONGITUD':-43.2333,'MATERIAL':'oro'}]) == ['piedra','oro'])
  assert ( md.materiales_respecto_coordenadas( {'lat':[32.123,43.2333],'lon':[-58.123,-43.2333]} , [{'LATITUD':32.123,'LONGITUD':-58.123,'MATERIAL':'madera'},{'LATITUD':43.2333,'LONGITUD':43.2333,'MATERIAL':'oro'}])==['madera', ''])

def test_contador_materiales():

 assert(md.contar_materiales(["CEMENTO","CEMENTO GRILLADO"],True)=={'CEMENTO':2})
 assert(md.contar_materiales([{"MATERIAL":"CEMENTO"},{"MATERIAL":"CEMENTO GRILLADO"}],False)=={"CEMENTO":2})


def main():

  test_obtener_columna()
  test_coordenadas_por_cantidad_de_objetos()
  test_coordenadas_por_columna()
  test_columna_sin_duplicados()  
  test_numero_comuna()
  test_frecuencia_rel_abs_comuna()
  test_union_coordenadas()
  test_interseccion_coordenadas()
  test_coordenadas_por_elemento_diccionario()
  test_buscador_indvidual_coordenadas()
  test_materiales_respecto_coordenadas()
  test_contador_materiales()
  
if __name__ == "__main__":
  main()
