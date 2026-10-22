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
