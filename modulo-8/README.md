# Módulo 8 · Aprendizaje automático con imágenes de células sanguíneas

Clase de 3 horas. Recorre el flujo completo del aprendizaje automático sobre un mismo conjunto de imágenes: clasificar, diagnosticar el sobreajuste y agrupar sin etiquetas. Como en el módulo 7, los estudiantes no escriben código desde cero: a partir de consignas, piden el código a un asistente de IA, lo leen, lo ejecutan y verifican el resultado. Con imágenes se suma una regla: antes de confiar en un resultado, mirar imágenes reales.

## Archivos

| Archivo | Para quién | Qué es |
|---|---|---|
| `resuelto.ipynb` | docentes | Fuente única del módulo: consignas, prompts de referencia, código, salidas, interpretaciones y notas docentes. |
| `guia.ipynb` | estudiantes | Se genera desde el resuelto con `herramientas/crear_guia.py`. **No editarla a mano.** Debajo de cada «Tu interpretación» trae las conclusiones del resuelto en un bloque plegado, para quien se trabe. |
| [`teoria.pdf`](teoria.pdf) | docentes y estudiantes | Diapositivas de la teoría: datos, métricas, regresión logística, árboles y bosques, K-Means y PCA. |

## Datos

**BloodMNIST** (colección MedMNIST): 17 092 imágenes de microscopía de células normales de sangre periférica, de 28 × 28 píxeles en color, clasificadas en 8 tipos celulares: basófilo, eosinófilo, eritroblasto, granulocito inmaduro, linfocito, monocito, neutrófilo y plaqueta. Licencia CC BY 4.0.

- **Entrenamiento:** una submuestra fija de 5000 imágenes, balanceada a mano (625 por tipo celular, semilla 42).
- **Prueba:** la partición oficial completa (3421 imágenes), con el desbalance real del archivo.
- **Medida:** F1 macro, que pesa igual a todos los tipos celulares.

El archivo (35 MB) no está en el repositorio. Fuente, licencia, balance de clases y cómo descargarlo en [`../data/README.md`](../data/README.md).

## Estructura de la clase

| Bloque | Consignas | Producto |
|---|---|---|
| Teoría | — | Datos, métricas, regresión logística, árboles y bosques, K-Means y PCA |
| 1. Imágenes y primer clasificador | 1.1 a 1.3 | Matriz de confusión interpretada |
| 2. Árbol, bosque y sobreajuste | 2.1 a 2.4 | Tabla de modelos y curva de F1 por profundidad del árbol |
| Descanso | | |
| 3. Redes neuronales y curva de pérdida | 3.1 a 3.4 | Curva de pérdida con la época de parada marcada |
| 4. Agrupamiento con K-Means | 4.1 a 4.3 | Centros de los grupos y tabla de grupos frente a tipos celulares |
| Cierre | Consigna final | Elección justificada de un modelo |
| 5. PCA (optativo) | 5.1 y 5.2, resueltas | Proyección en 2 componentes y varianza explicada acumulada |

## Resultados clave

| Modelo | F1 macro, entrenamiento | F1 macro, prueba |
|---|---|---|
| Bosque aleatorio (100 árboles) | 1,000 | 0,794 |
| Red neuronal (100 neuronas, 40 épocas) | 1,000 | 0,793 |
| Red neuronal con parada temprana | 0,980 | 0,789 |
| Regresión logística | 1,000 | 0,704 |
| Árbol sin límite de profundidad | 1,000 | 0,574 |

- **Sobreajuste en el árbol:** el F1 de prueba deja de mejorar a partir de la profundidad 8 (cerca de 0,60), mientras el de entrenamiento sigue subiendo hasta 1,00.
- **Sobreajuste en la red:** la pérdida de validación es mínima en la época 5 y después sube, aunque el F1 de validación casi no cambia. La red se vuelve demasiado segura cuando se equivoca.
- **Estandarizar:** sin estandarizar, la red aprende más lento y su F1 de prueba baja de 0,793 a 0,718. Para K-Means y PCA no hace falta, porque todos los píxeles están en la misma escala.
- **K-Means:** con 4 tipos bien distintos (linfocito, monocito, neutrófilo y plaqueta), los grupos coinciden bastante con los tipos celulares (ARI 0,71). Con los 8 tipos, el ARI baja a 0,34. Ni el codo ni la silueta señalan k = 4.
- **PCA:** 37 componentes explican el 80 % de la varianza de las 2352 columnas.

## Checklist docente

**Antes de la clase**

- [ ] Confirmar que el entorno quedó instalado en una clase anterior: VS Code, OpenCode y Python con `requirements.txt`.
- [ ] Descargar los datos en la carpeta del curso:
  ```bash
  python herramientas/descargar_bloodmnist.py data/bloodmnist.npz
  ```
  Si el archivo falta, el notebook lo baja de Zenodo la primera vez, pero eso requiere conexión en el aula.
- [ ] Si se editó el resuelto, regenerar la guía y ejecutar las dos versiones:
  ```bash
  python herramientas/crear_guia.py modulo-8/resuelto.ipynb modulo-8/guia.ipynb
  jupyter nbconvert --to notebook --execute --inplace modulo-8/resuelto.ipynb
  jupyter nbconvert --to notebook --execute --inplace modulo-8/guia.ipynb
  ```

**Durante la clase**

- En el bloque 1, la regresión logística llega a F1 = 1,000 en entrenamiento. Es el primer contacto con el sobreajuste: lo que importa es el F1 de prueba.
- En la consigna 3.1, la pérdida de validación sube desde la época 5 pero el F1 casi no cambia. Conviene detenerse ahí: la pérdida mide también la confianza de cada predicción, el F1 no.
- La parada temprana de scikit-learn no se detiene en la época 5: su criterio es la exactitud sobre una parte de los datos de entrenamiento, y espera 10 épocas sin mejora.
- En la consigna 4.3, ni el codo ni la silueta eligen k = 4. No es un error del código: es la conclusión del bloque.

**Si falta tiempo**

- El bloque 5 (PCA) es optativo y va resuelto en la guía. Ningún otro bloque depende de él.
