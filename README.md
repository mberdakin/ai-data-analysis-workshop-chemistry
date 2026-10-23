**Español** · [English](README.en.md)

# Taller de IA para análisis de datos en Ciencias Químicas

Materiales de los módulos 7 y 8 del curso de posgrado **"Aplicaciones de herramientas de Inteligencia Artificial en Investigación Científica"** (Facultad de Ciencias Químicas, Universidad Nacional de Córdoba, ciclo 2026).

## A quién va dirigido

Estudiantes de doctorado y maestría en Ciencias Químicas **que no programan**. En cada clase trabajan con un asistente de IA y notebooks de Python: a partir de una consigna escriben el prompt, leen el código que genera el asistente, lo ejecutan y **verifican** el resultado. La verificación es parte de cada actividad, porque el asistente puede equivocarse con total seguridad.

## Módulos

| Módulo | Tema | Estado |
|---|---|---|
| [7](modulo-7/) | Python con asistencia de IA, estadística descriptiva, visualización y regresión: calibración, ajuste de curvas, sobreajuste y métricas | Primera versión |
| 8 | Flujo de machine learning: árboles, bosques, K-Means, PCA y redes neuronales | En preparación |

Cada módulo tiene dos notebooks: `guia.ipynb`, para estudiantes, con consignas, pistas y espacios para completar; y `resuelto.ipynb`, para docentes, con soluciones, prompts de referencia e interpretaciones. La guía se genera automáticamente desde el resuelto.

## Módulo 7 en una mirada

Toda la clase usa datos reales de **calibración de un ensayo ELISA** (conjunto DNase: 11 corridas, 8 concentraciones patrón, lecturas por duplicado):

- **Entorno y depuración:** cargar los datos desde un archivo y desde una URL; leer un error real y corregirlo con el asistente.
- **Datos sucios:** encontrar 4 lecturas alteradas a propósito. Un boxplot marca 10 lecturas sospechosas, y 6 de ellas son reales; comparar los duplicados de cada corrida aísla exactamente las 4 alteradas.
- **Figura para publicar:** adaptar un gráfico a las normas de figuras de una revista (en el ejemplo, ACS) y verificar el archivo contra la guía oficial.
- **Calibración y predicción inversa:** recta en el tramo lineal (pendiente 0,380, R² = 0,980) y concentración de una muestra desconocida.
- **Ajuste de curvas:** la logística de cuatro parámetros, el modelo estándar de los inmunoensayos, reduce el RMSE de 0,206 (recta) a 0,017. Un polinomio de grado 3 logra un RMSE parecido con una forma sin sentido físico.
- **Sobreajuste:** el error de prueba es mínimo en grado 4 (RMSE 0,036) y se dispara en grado 10 (RMSE 28), donde el R² de entrenamiento es 1,000 y el de prueba es −1932.

<p align="center">
  <img src="docs/figuras/modulo7-ajuste-curvas.png" alt="Cuatro modelos ajustados a la curva de calibración" width="48%">
  <img src="docs/figuras/modulo7-sobreajuste.png" alt="Error de entrenamiento y de prueba por grado del polinomio" width="48%">
</p>

El bloque de sobreajuste usa 18 puntos **simulados** a partir de la curva y el ruido de los datos reales, porque cada corrida real tiene solo 8 concentraciones distintas. Está declarado en el notebook y en [`data/README.md`](data/README.md).

## Cómo ejecutar

En el curso se trabaja con **VS Code** y el asistente **OpenCode**:

1. Clonar o descargar este repositorio y abrir la carpeta en VS Code.
2. Crear un entorno de Python 3.12 e instalar las librerías:
   ```bash
   pip install -r requirements.txt
   ```
3. Abrir `modulo-7/guia.ipynb`, elegir ese entorno como *kernel* y pedirle a OpenCode el código de cada consigna.

Sin VS Code, los notebooks también se pueden abrir con `jupyter notebook`.

## Estructura

```
modulo-7/       notebooks del módulo 7 (guía y resuelto) y su README con el checklist docente
data/           conjuntos de datos, con fuente, licencia y descripción en data/README.md
herramientas/   scripts para generar la guía y los datos con anomalías
docs/           figuras de este README
```

## Datos y licencias

El código y los materiales del curso se distribuyen bajo la [licencia MIT](LICENSE).

Los conjuntos de datos tienen su propia procedencia y licencia. DNase proviene de Davidian y Giltinan (1995) y se distribuye con R (paquete `datasets`). Los detalles de cada conjunto, y la descripción de los datos simulados y alterados, están en [`data/README.md`](data/README.md).
