# Módulo 7 · Python con asistencia de IA, estadística y regresión

Clase de 3 horas. Los estudiantes no escriben código desde cero: a partir de consignas, piden el código a un asistente de IA, lo leen, lo ejecutan y verifican el resultado.

## Archivos

| Archivo | Para quién | Qué es |
|---|---|---|
| `resuelto.ipynb` | docentes | Fuente única del módulo: consignas, prompts de referencia, código, salidas, interpretaciones y notas docentes. |
| `guia.ipynb` | estudiantes | Se genera desde el resuelto con `herramientas/crear_guia.py`. **No editarla a mano.** |
| [`teoria.pdf`](teoria.pdf) | docentes y estudiantes | Diapositivas de la teoría del comienzo de la clase. |

## Datos

**DNase**: calibración de un ensayo ELISA para la DNasa recombinante en suero de rata (176 lecturas: 11 corridas × 8 concentraciones patrón × duplicado). Además, una copia con 4 lecturas alteradas a propósito para el bloque 2 y 18 puntos simulados para el bloque de sobreajuste. Fuente, licencia y detalles en [`../data/README.md`](../data/README.md).

## Estructura de la clase

| Bloque | Consignas | Producto |
|---|---|---|
| Teoría | — | La pregunta que se responde en el bloque 4 |
| 1. Entorno: VS Code, OpenCode y carga de datos | 1.1 a 1.3 | Los datos cargados de dos formas y un error depurado |
| 2. Estadística descriptiva | 2.1 a 2.4 | Tabla resumen y datos depurados de lecturas anómalas |
| 3. Visualización | 3.1 a 3.3 | Una figura con las normas de una revista |
| Descanso | | |
| 4.1 Recta de calibración | 4.1 | Recta de calibración con su pendiente, ordenada y R² |
| 4.2 Ajuste de curvas | 4.2 y 4.3 | Comparación de recta, polinomios y logística |
| 4.3 Sobreajuste | 4.4 a 4.6 | Gráfico de error por grado del polinomio |
| 4.4 Métricas (opcional) | 4.7 y 4.8 | Tabla de R², RMSE y MAE |

## Checklist docente

**Antes de la clase**

- [ ] Confirmar que el entorno quedó instalado en la clase anterior: VS Code, OpenCode y Python con `requirements.txt`.
- [ ] Comprobar que la carpeta del curso incluya `data/` (el notebook lee los CSV desde `../data/`) y que haya conexión a internet para la consigna 1.1.
- [ ] Si se editó el resuelto, regenerar la guía y ejecutar las dos versiones:
  ```bash
  python herramientas/crear_guia.py modulo-7/resuelto.ipynb modulo-7/guia.ipynb
  jupyter nbconvert --to notebook --execute --inplace modulo-7/resuelto.ipynb
  jupyter nbconvert --to notebook --execute --inplace modulo-7/guia.ipynb
  ```
- [ ] No compartir `herramientas/crear_datos_anomalos.py`: contiene la clave de las lecturas alteradas del bloque 2.

**Durante la clase**

- La celda de la consigna 1.3 falla a propósito. Si alguien usa *Ejecutar todas*, la ejecución se detiene ahí: es lo esperado.
- En la consigna 2.2, el boxplot marca también 6 lecturas reales de las corridas 2 y 3. No son errores: es el punto de la actividad.
- En la consigna 3.2, insistir en verificar contra la guía oficial de la revista y revisar el archivo guardado, no la vista en pantalla.
- La curva de sobreajuste depende de la semilla: con la configuración del notebook, la forma en U clara aparece en unas 78 de cada 100 semillas. La semilla fija (32) muestra un perfil limpio.

**Si falta tiempo**

- La sección 4.4 (consignas 4.7 y 4.8) es opcional. Si no se hace, conviene igual discutir las preguntas de la sección 4.4 con la tabla de métricas del resuelto: en grado 10, el R² de entrenamiento es prácticamente 1 y el de prueba es muy negativo.
