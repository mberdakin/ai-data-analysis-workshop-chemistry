"""Genera data/dnase_con_anomalias.csv: una copia de DNase con 4 lecturas alteradas.

Lo usa el bloque 2 del módulo 7, donde los estudiantes tienen que encontrar las
lecturas anómalas sin saber cuáles son. Cada anomalía reemplaza UNA de las dos
lecturas duplicadas de una corrida y concentración; la otra queda intacta.

Esta lista es la clave de la actividad: no mostrarla a los estudiantes.

Uso:
  python herramientas/crear_datos_anomalos.py data/dnase.csv data/dnase_con_anomalias.csv
"""
import sys

import pandas as pd

# (corrida, concentración, cuál de los dos duplicados, tipo de anomalía)
ANOMALIAS = [
    (7, 3.125, 0, "error de tipeo: la lectura se multiplica por 10 (coma corrida)"),
    (4, 0.1953125, 0, "pocillo contaminado: lectura alta en una concentración baja"),
    (9, 6.25, 1, "pocillo sin reactivo: lectura cercana a cero en una concentración alta"),
    (5, 1.5625, 1, "desvío sutil: lectura alta pero dentro del rango general de los datos"),
]

# Valor que toma la lectura alterada (salvo el error de tipeo, que se calcula)
VALORES_NUEVOS = {
    (4, 0.1953125): 0.900,
    (9, 6.25): 0.030,
    (5, 1.5625): 0.950,
}


def crear_datos_anomalos(ruta_entrada, ruta_salida):
    datos = pd.read_csv(ruta_entrada)

    for corrida, concentracion, duplicado, descripcion in ANOMALIAS:
        filas_del_par = datos.index[(datos["Run"] == corrida) & (datos["conc"] == concentracion)]
        if len(filas_del_par) != 2:
            sys.exit(f"Se esperaban 2 lecturas para corrida {corrida} y concentración {concentracion}.")
        fila = filas_del_par[duplicado]
        valor_original = datos.loc[fila, "density"]

        if (corrida, concentracion) in VALORES_NUEVOS:
            valor_nuevo = VALORES_NUEVOS[(corrida, concentracion)]
        else:
            valor_nuevo = round(valor_original * 10, 3)

        datos.loc[fila, "density"] = valor_nuevo
        print(f"Corrida {corrida}, conc {concentracion}: {valor_original} -> {valor_nuevo} ({descripcion})")

    datos.to_csv(ruta_salida, index=False)
    print(f"Escrito {ruta_salida}: {len(datos)} filas")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python herramientas/crear_datos_anomalos.py <dnase.csv> <salida.csv>")
    crear_datos_anomalos(sys.argv[1], sys.argv[2])
