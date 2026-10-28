"""Descarga data/bloodmnist.npz: imágenes de células sanguíneas para el módulo 8.

El archivo (35 MB) no se versiona en el repositorio: cada equipo lo descarga una
vez con este script. Se baja la versión oficial de 28 x 28 píxeles desde Zenodo
y se comprueba su MD5 contra el publicado por MedMNIST, para asegurar que el
archivo llegó completo y es el mismo con el que se ejecutaron los notebooks.

No usa el paquete medmnist (que arrastra PyTorch): solo la biblioteca estándar.

Uso:
  python herramientas/descargar_bloodmnist.py data/bloodmnist.npz
"""
import hashlib
import sys
import urllib.request
from pathlib import Path

# URL y MD5 oficiales, tomados de medmnist/info.py (MedMNIST v3, Zenodo 10519652)
URL = "https://zenodo.org/records/10519652/files/bloodmnist.npz?download=1"
MD5_ESPERADO = "7053d0359d879ad8a5505303e11de1dc"


def md5_de(ruta):
    suma = hashlib.md5()
    with open(ruta, "rb") as archivo:
        for bloque in iter(lambda: archivo.read(1024 * 1024), b""):
            suma.update(bloque)
    return suma.hexdigest()


def descargar_bloodmnist(ruta_salida):
    ruta_salida = Path(ruta_salida)

    if ruta_salida.exists() and md5_de(ruta_salida) == MD5_ESPERADO:
        print(f"{ruta_salida} ya existe y su MD5 es correcto: no hace falta descargarlo.")
        return

    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    print(f"Descargando {URL} (35 MB, puede tardar unos minutos)...")
    urllib.request.urlretrieve(URL, ruta_salida)

    md5_obtenido = md5_de(ruta_salida)
    if md5_obtenido != MD5_ESPERADO:
        ruta_salida.unlink()
        sys.exit(f"El MD5 no coincide ({md5_obtenido}): se borró el archivo. Volvé a intentar.")
    print(f"Escrito {ruta_salida}: MD5 correcto.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Uso: python herramientas/descargar_bloodmnist.py <salida.npz>")
    descargar_bloodmnist(sys.argv[1])
