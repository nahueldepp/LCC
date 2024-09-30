import monumentos_data as md
import csv
import streamlit as st
import matplotlib.pyplot as plt


def grafica(monumentos):
    '''
    grafica: None -> None
    Devuelve una gráfica con el top10 de materiales más usados.
    '''

    diccionario_materiales = md.graficador(md.contar_materiales(monumentos,eslista=False),coordenadastotales=False, monumentos=False, top10grafica=True , graficatorta=False)

    etiquetas = list(diccionario_materiales.keys())
    valores = list(diccionario_materiales.values())

    fig_kw = {'facecolor': "#2E2E2E", 'linewidth' : 1,'edgecolor' : "#2E2E2E"}
    fig_words = {'fontsize' : 9, 'fontweight' : 'roman', 'fontstyle':'italic'}

    fig = plt.figure(**fig_kw)

    plt.barh(etiquetas, valores, color="black")
    plt.title('Los diez materiales más usados en los monumentos:',color ="white")

    plt.xticks(color="white", **fig_words)
    plt.yticks(color="white",**fig_words)

    plt.xlabel("Cantidad",color = "white")
    plt.ylabel("Material",color = "white")

    return fig

def grafica_dinamica_materiales(coordenadas,monumentos_seleccionados):

 diccionario_materiales = md.graficador(False , coordenadas, monumentos_seleccionados, top10grafica=False , graficatorta=True)

 
    
 labels = list(diccionario_materiales.keys())
 sizes = tuple(diccionario_materiales.values())

 fig_kw = {'facecolor': "#2E2E2E", 'linewidth' : 1,'edgecolor' : "#2E2E2E"}
    
 fig, ax = plt.subplots(**fig_kw)
 
 plt.title('Los tres materiales más usados por monumentos en el mapa:',color ="white")
 ax.pie(sizes, labels=labels,autopct='%1.1f%%')

 return fig
