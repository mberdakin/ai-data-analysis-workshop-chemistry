# Datos

Conjuntos de datos que usan los notebooks del curso. Para cada uno se registra la fuente, la licencia y una descripción comprobada al cargarlo.

## `dnase.csv` (módulo 7)

Calibración de un ensayo ELISA para la proteína DNasa recombinante en suero de rata.

### Fuente

- **Origen:** Davidian, M. y Giltinan, D. M. (1995). *Nonlinear Models for Repeated Measurement Data*. Chapman & Hall, sección 5.2.4, p. 134. También en Pinheiro, J. C. y Bates, D. M. (2000). *Mixed-effects Models in S and S-PLUS*. Springer.
- **Distribución:** conjunto `DNase` del paquete `datasets` de R (originalmente del paquete `nlme`).
- **Archivo:** copia sin modificar del CSV publicado por [Rdatasets](https://github.com/vincentarelbundock/Rdatasets) (`csv/datasets/DNase.csv`), descargado el 20 de octubre de 2026.
- **SHA-256:** `d9af548405c6772dfbc7caf9998544f27fc133b7dbaa4340ae198787da98d5f4`

### Licencia

- El paquete `datasets` declara la licencia *"Part of R"*. Su archivo de documentación de `DNase` se distribuye bajo GPL 2 o posterior.
- Rdatasets publica su código bajo GPL-3. Sobre los datos en sí, su autor indica que no pudo determinar una licencia definitiva y que entiende que se pueden redistribuir libremente.
- No encontramos una licencia explícita para los valores numéricos fuera de su distribución con R.

### Estructura

176 filas, 4 columnas, sin valores faltantes.

| Columna | Tipo | Descripción |
|---|---|---|
| `rownames` | entero | Número de fila heredado de R. No es un dato; los notebooks lo descartan. |
| `Run` | entero (1 a 11) | Corrida del ensayo. |
| `conc` | real | Concentración conocida del patrón de DNasa. La documentación no indica la unidad. |
| `density` | real | Densidad óptica medida (adimensional). |

- **Corridas:** cada corrida es una ejecución completa del ensayo. Las 11 corridas tienen las mismas 8 concentraciones (0,049; 0,195; 0,391; 0,781; 1,563; 3,125; 6,25 y 12,5), cada una medida por duplicado: 16 filas por corrida.
- **Numeración:** en R, `Run` es un factor ordenado por respuesta máxima creciente (10 < … < 3). Los números son etiquetas, no un orden cronológico.
- **Lo que no dice la documentación:** qué cambió entre una corrida y otra (día, placa, operador o lote de reactivos).
- **Rangos:** `conc` de 0,049 a 12,5; `density` de 0,011 a 2,003.
- **Variabilidad:** el desvío de `density` entre corridas crece con la concentración, de 0,024 a 0,031 en los cinco patrones más bajos a 0,069 y 0,085 en los dos más altos.

## `dnase_con_anomalias.csv` (módulo 7, bloque 2): datos alterados a propósito

Copia de `dnase.csv` con **4 lecturas de densidad óptica alteradas** por el equipo docente, para la actividad de detección y depuración de lecturas anómalas. No son datos reales en esas 4 filas; el resto es idéntico al original.

- **Cómo se genera:** `python herramientas/crear_datos_anomalos.py data/dnase.csv data/dnase_con_anomalias.csv`. El script contiene la clave de la actividad (qué lecturas se alteraron y cómo), así que no conviene mostrarlo a los estudiantes antes de la clase.
- **Diseño:** cada anomalía reemplaza una de las dos lecturas duplicadas de una corrida y concentración; la otra queda intacta. Así, la diferencia entre duplicados permite encontrarlas: en los datos reales, esa diferencia es como máximo 0,15; en los pares alterados, va de 0,29 a 9,5.
- **Tipos de anomalía:** un error de tipeo (lectura multiplicada por 10), un pocillo contaminado (lectura alta en una concentración baja), un pocillo sin reactivo (lectura cercana a cero en una concentración alta) y un desvío sutil (lectura alta, pero dentro del rango general de los datos).

## Datos simulados (módulo 7, bloque 4.3)

El bloque de sobreajuste usa **18 puntos simulados**. No hay archivo: el notebook los genera al ejecutarse. Se simulan porque cada corrida real tiene solo 8 concentraciones distintas, demasiado pocas para mostrar el sobreajuste.

- **Concentraciones:** 18 valores espaciados en escala logarítmica entre la mínima y la máxima de `dnase.csv`, como en una dilución seriada.
- **Curva verdadera:** logística de cuatro parámetros en función de ln(concentración), ajustada a las 176 mediciones reales.
- **Ruido:** gaussiano, con desvío igual al de los residuos de ese ajuste (≈ 0,046), constante en toda la curva. Es una simplificación: en los datos reales el desvío crece con la concentración.
- **Reproducibilidad:** semilla fija (`SEMILLA` en la celda de configuración).

## `bloodmnist.npz` (módulo 8): no se versiona, se descarga

Imágenes de microscopía de células sanguíneas normales de sangre periférica, clasificadas en 8 tipos celulares. Es el subconjunto BloodMNIST de la colección MedMNIST.

### Cómo obtenerlo

El archivo pesa 35 MB y no está en el repositorio (`data/*.npz` figura en `.gitignore`). Se descarga una vez con:

```
python herramientas/descargar_bloodmnist.py data/bloodmnist.npz
```

El script baja la versión oficial de 28 × 28 píxeles desde Zenodo y comprueba su MD5 (`7053d0359d879ad8a5505303e11de1dc`). Los notebooks lo leen con NumPy (`np.load`), sin instalar el paquete `medmnist`, que arrastra PyTorch.

### Fuente

- **Colección:** Yang, J. et al. (2023). MedMNIST v2: A large-scale lightweight benchmark for 2D and 3D biomedical image classification. *Scientific Data*, 10, 41. https://doi.org/10.1038/s41597-022-01721-8
- **Datos originales:** Acevedo, A., Merino, A., Alférez, S., Molina, Á., Boldú, L. y Rodellar, J. (2020). A dataset of microscopic peripheral blood cell images for development of automatic recognition systems. *Data in Brief*, 30, 105474. https://doi.org/10.1016/j.dib.2020.105474
- **Archivo:** `bloodmnist.npz` del registro [Zenodo 10519652](https://doi.org/10.5281/zenodo.10519652) (MedMNIST+, versión 3.0), descargado el 27 de octubre de 2026. URL y MD5 tomados de `medmnist/info.py` en el repositorio oficial de MedMNIST.
- **SHA-256:** `062023e186f537e26b3c21ea3b2614ddfc475e8a14825dfd20663bbb7e37bddc`
- **Preprocesamiento de MedMNIST:** según su documentación, las imágenes originales (360 × 363 píxeles) se recortan al centro a 200 × 200 y se reducen a 28 × 28.

### Licencia

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), tanto en el registro de Zenodo como en el README de MedMNIST y en el artículo original. Permite redistribuir y adaptar con atribución: citar los dos trabajos de arriba. MedMNIST aclara que los datos no están pensados para uso clínico.

### Estructura

Seis arreglos de NumPy, sin objetos de Python (se cargan con `allow_pickle=False`):

| Arreglo | Forma | Tipo |
|---|---|---|
| `train_images` / `train_labels` | (11 959, 28, 28, 3) / (11 959, 1) | `uint8` |
| `val_images` / `val_labels` | (1712, 28, 28, 3) / (1712, 1) | `uint8` |
| `test_images` / `test_labels` | (3421, 28, 28, 3) / (3421, 1) | `uint8` |

- **Imágenes:** 17 092 en total, de 28 × 28 píxeles en color (canales rojo, verde y azul), con valores de 0 a 255. Aplanada, cada imagen tiene 2352 variables.
- **Divisiones:** entrenamiento, validación y prueba vienen predefinidas (proporción 7:1:2).
- **Clases:** la etiqueta es un entero de 0 a 7.

| Etiqueta | Tipo celular | Entrenamiento | Validación | Prueba | % del total |
|---|---|---|---|---|---|
| 0 | basófilo | 852 | 122 | 244 | 7,1 |
| 1 | eosinófilo | 2181 | 312 | 624 | 18,2 |
| 2 | eritroblasto | 1085 | 155 | 311 | 9,1 |
| 3 | granulocito inmaduro (mielocito, metamielocito, promielocito) | 2026 | 290 | 579 | 16,9 |
| 4 | linfocito | 849 | 122 | 243 | 7,1 |
| 5 | monocito | 993 | 143 | 284 | 8,3 |
| 6 | neutrófilo | 2330 | 333 | 666 | 19,5 |
| 7 | plaqueta | 1643 | 235 | 470 | 13,7 |

- **Balance:** moderado. La clase menos frecuente tiene el 36 % de imágenes que la más frecuente, con la misma proporción en las tres divisiones. Por eso conviene medir con F1 macro, que pesa igual a todas las clases.
- **Excepción a los criterios de datos del curso:** son muchas más filas y variables que en el resto de los conjuntos. Se acepta por decisión del autor; en clase se trabaja con una submuestra (ver el módulo 8).
