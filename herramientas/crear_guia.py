"""Genera la guía para estudiantes a partir del notebook resuelto.

La fuente única de cada módulo es resuelto.ipynb. Sus celdas pueden llevar
etiquetas (en Colab o Jupyter: Ver → Etiquetas de celda) que indican qué hacer
con ellas en la guía:

  solo-docente    se elimina (prompts de referencia, notas para docentes)
  solucion        se reemplaza por un espacio para anotar el prompt y una celda vacía
  interpretacion  se reemplaza por un espacio "Tu interpretación"

Las celdas sin etiqueta pasan igual, salvo los tiempos estimados de los títulos
(por ejemplo "(25 min)"), que son para el docente y se quitan en la guía. Uso:

  python herramientas/crear_guia.py modulo-7/resuelto.ipynb modulo-7/guia.ipynb
"""
import re
import sys

import nbformat

TEXTO_RESUELTO = "**Versión resuelta para docentes.**"
TEXTO_GUIA = "**Guía para estudiantes.**"

# Tiempo estimado al final de un título, por ejemplo " (25 min)"
PATRON_TIEMPO = re.compile(r" \(\d+ min\)$", re.MULTILINE)


def etiquetas(celda):
    return celda.metadata.get("tags", [])


def celda_tu_prompt():
    return nbformat.v4.new_markdown_cell("**Tu prompt:**\n\n*...*")


def celda_codigo_vacia():
    return nbformat.v4.new_code_cell("# Pegá o escribí aquí el código que generó el asistente\n")


def celda_tu_interpretacion():
    return nbformat.v4.new_markdown_cell("#### Depende del dataset\n\n**Tu interpretación:**\n\n*...*")


def crear_guia(ruta_resuelto, ruta_guia):
    resuelto = nbformat.read(ruta_resuelto, as_version=4)
    celdas_guia = []

    for celda in resuelto.cells:
        marcas = etiquetas(celda)
        if "solo-docente" in marcas:
            continue
        if "solucion" in marcas:
            celdas_guia.append(celda_tu_prompt())
            celdas_guia.append(celda_codigo_vacia())
            continue
        if "interpretacion" in marcas:
            celdas_guia.append(celda_tu_interpretacion())
            continue

        # Celda sin etiqueta: se copia sin salidas, para que la guía empiece limpia
        copia = nbformat.from_dict(celda)
        if copia.cell_type == "code":
            copia.outputs = []
            copia.execution_count = None
        else:
            copia.source = PATRON_TIEMPO.sub("", copia.source)
        celdas_guia.append(copia)

    # La portada del resuelto dice que es la versión docente; en la guía se cambia
    portada = celdas_guia[0]
    if TEXTO_RESUELTO not in portada.source:
        sys.exit(f"No se encontró '{TEXTO_RESUELTO}' en la primera celda del resuelto.")
    portada.source = portada.source.replace(TEXTO_RESUELTO, TEXTO_GUIA)

    guia = nbformat.v4.new_notebook(metadata=resuelto.metadata)
    guia.cells = celdas_guia
    nbformat.write(guia, ruta_guia)
    print(f"Guía escrita en {ruta_guia}: {len(celdas_guia)} celdas (resuelto: {len(resuelto.cells)})")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python herramientas/crear_guia.py <resuelto.ipynb> <guia.ipynb>")
    crear_guia(sys.argv[1], sys.argv[2])
