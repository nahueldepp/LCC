import streamlit as st
import monumentos_data as md
import grafica_materiales as gm

st.set_page_config(page_title="Monumentos Capital Federal",
                   page_icon="🗿",
                   layout="wide",
                   initial_sidebar_state="collapsed")


def metodo_visualizacion(coordenadas, diccionario_seleccion):
    if metodo == "Unión de filtros":
        return md.union_coordenadas(coordenadas, diccionario_seleccion)
    else:
        return md.interseccion_coordenadas(coordenadas, diccionario_seleccion)


fila_mapa = st.columns(1)
graficas, grafica2 = st.columns(2)

with fila_mapa[0], st.container(border=True):
    # Esta es la unica vez que cargamos el csv en memoria
    monumentos = md.monumentos_dic()
    # Valor maximo de objetos para el slider
    max_objetos = max(
        md.obtener_columna(monumentos,
                           'CANTIDAD_OBJETOS',
                           filtrar_vacio=True,
                           to_int=True))

    metodo = st.radio(
        'Seleccione el método de visualización: ',
        ["Unión de filtros", "Intersección de filtros"],
        help=
        "Unión: Muestra en el mapa los monumentos que corresponden al menos a un filtro seleccionado \n\nIntersección: Muestra en el mapa los monumentos que verifican todos los filtros seleccionados",
        horizontal=True)

    add_slider = st.sidebar.slider('Número de partes del monumento',
                                   step=1,
                                   max_value=max_objetos,
                                   value=[0, max_objetos])

    add_multiselect = st.sidebar.multiselect(
        'Seleccione uno o varios autores:',
        options=md.columna_sin_duplicados(monumentos, 'AUTORES'),
        placeholder='Autor')

    add_selectbox_barrio = st.sidebar.selectbox(
        'Seleccione un Barrio:',
        options=md.columna_sin_duplicados(monumentos, 'BARRIO'),
        index=None,
        placeholder='Barrio')

    add_selectbox_comuna = st.sidebar.selectbox(
        'Seleccione una Comuna:',
        options=sorted(md.columna_sin_duplicados(monumentos, 'COMUNA'),
                       key=md.numero_comuna),
        index=None,
        placeholder='Comuna')

    coordenadas = {'lat': [], 'lon': []}

    if add_slider != ():
        cantidad_monumentos = md.coordenadas_por_cantidad_de_objetos(
            monumentos, add_slider)
        coordenadas = metodo_visualizacion(coordenadas, cantidad_monumentos)

    if add_multiselect != []:
        autores_coordenadas = md.coordenadas_por_columna(
            monumentos, 'AUTORES', add_multiselect)
        coordenadas = metodo_visualizacion(coordenadas, autores_coordenadas)

    if add_selectbox_barrio != None:
        barrio_coordenadas = md.coordenadas_por_columna(
            monumentos, 'BARRIO', [add_selectbox_barrio])
        coordenadas = metodo_visualizacion(coordenadas, barrio_coordenadas)

    if add_selectbox_comuna != None:
        comuna_coordenadas = md.coordenadas_por_columna(
            monumentos, 'COMUNA', [add_selectbox_comuna])
        coordenadas = metodo_visualizacion(coordenadas, comuna_coordenadas)

    if coordenadas['lat'] != [] and coordenadas['lon'] != []:
        st.map(coordenadas, color='#FE2E2E', size=1)
    else:
        st.map({
            'lat': [-34.62231365012345],
            'lon': [-58.473507224857585]
        },
               color='#00FF0000',
               size=100)

    with graficas, st.container(border=True):
        st.pyplot(gm.grafica_dinamica_materiales(coordenadas, monumentos),
                  use_container_width=True)
        st.pyplot(gm.grafica(monumentos), use_container_width=True)
        
    with grafica2, st.container(border=True):
        add_figure = st.table(md.data_comunas(monumentos))
        
  
