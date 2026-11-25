[Español](README.md) · **English**

# AI-Assisted Data Analysis Workshop for Chemical Sciences

Materials for modules 7 and 8 of the graduate course **"Aplicaciones de herramientas de Inteligencia Artificial en Investigación Científica"** (*Applications of Artificial Intelligence Tools in Scientific Research*), Faculty of Chemical Sciences, National University of Córdoba, Argentina, 2026. The course materials are in Spanish.

## Who it is for

PhD and master's students in Chemical Sciences **who do not code**. In each class they work with an AI assistant and Python notebooks: given a task, they write the prompt, read the code the assistant generates, run it and **verify** the result. Verification is part of every activity, because the assistant can be confidently wrong.

## Modules

| Module | Topic | Status |
|---|---|---|
| [7](modulo-7/) | Python with AI assistance, descriptive statistics, visualization and regression: calibration, curve fitting, overfitting and metrics | First version |
| [8](modulo-8/) | Machine learning with blood cell images: classifiers, overfitting, K-Means clustering and PCA | First version |

Each module has the theory slides (`teoria.pdf`, in Spanish) and two notebooks: `guia.ipynb`, for students, with tasks, hints and space to work; and `resuelto.ipynb`, for instructors, with solutions, reference prompts and interpretations. The student notebook is generated automatically from the instructor notebook.

## Module 7 at a glance

The whole class uses real **ELISA calibration data** (the DNase dataset: 11 assay runs, 8 standard concentrations, duplicate readings):

- **Environment and debugging:** load the data from a file and from a URL; read a real error message and fix it with the assistant.
- **Dirty data:** find 4 readings altered on purpose. A boxplot flags 10 suspicious readings, 6 of which are genuine; comparing the duplicate readings within each run isolates exactly the 4 altered ones.
- **Publication-ready figure:** adapt a plot to a journal's figure guidelines (ACS in the example) and check the saved file against the official guidelines.
- **Calibration:** a straight line over the linear range (slope 0.380, R² = 0.980), reading its slope, intercept and R².
- **Curve fitting:** the four-parameter logistic, the standard model for immunoassays, lowers the RMSE from 0.206 (straight line) to 0.017. A third-degree polynomial reaches a similar RMSE with a physically meaningless shape.
- **Overfitting:** the test error is lowest at degree 4 (RMSE 0.036) and explodes at degree 10 (RMSE 28), where the training R² is 1.000 and the test R² is −1932.

<p align="center">
  <img src="docs/figuras/modulo7-ajuste-curvas.png" alt="Four models fitted to the calibration curve" width="48%">
  <img src="docs/figuras/modulo7-sobreajuste.png" alt="Training and test error by polynomial degree" width="48%">
</p>

The overfitting block uses 18 **simulated** points generated from the curve and noise of the real data, because each real run has only 8 distinct concentrations. This is stated in the notebook and in [`data/README.md`](data/README.md).

## Module 8 at a glance

The whole class uses **microscopy images of blood cells** (BloodMNIST: 28 × 28 color pixels, 8 cell types). Models are trained on a balanced subsample of 5000 images and evaluated on the 3421 official test images, using the macro F1 score:

- **First classifier:** logistic regression reaches F1 = 1.000 on training and 0.704 on test. The confusion matrix shows that errors concentrate among large cells with bulky nuclei, which look very similar at this resolution.
- **Trees and forests:** an unrestricted tree memorizes and scores 0.574; a 100-tree random forest rises to 0.794. The tree's test F1 stops improving from depth 8 onwards.
- **Neural networks and the loss curve:** the validation loss is lowest at epoch 5 and rises afterwards, while the F1 barely changes: the network becomes overconfident. Without standardizing the pixels, the test F1 drops from 0.793 to 0.718.
- **Clustering:** without using the labels, K-Means separates 4 clearly distinct cell types with an ARI of 0.71, and each cluster center can be drawn as an "average cell". With all 8 types the ARI drops to 0.34, and neither the elbow nor the silhouette method finds the number of types on its own.
- **PCA (optional):** 37 components explain 80% of the variance of the 2352 columns of each image.

<p align="center">
  <img src="docs/figuras/modulo8-curva-perdida.png" alt="Training and validation loss by epoch, with the validation minimum at epoch 5" width="48%">
  <img src="docs/figuras/modulo8-centros-kmeans.png" alt="Centers of the four K-Means clusters drawn as cell images" width="48%">
</p>

## How to run

The course uses **VS Code** with the **OpenCode** assistant:

1. Clone or download this repository and open the folder in VS Code.
2. Create a Python 3.12 environment and install the libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. For module 8, download the images (35 MB, not included in the repository):
   ```bash
   python herramientas/descargar_bloodmnist.py data/bloodmnist.npz
   ```
4. Open the module's student notebook (`modulo-7/guia.ipynb` or `modulo-8/guia.ipynb`), select that environment as the kernel and ask OpenCode for the code of each task.

Without VS Code, the notebooks can also be opened with `jupyter notebook`.

## Repository structure

```
modulo-7/       module 7 slides and notebooks (student and instructor versions), and a README with the instructor checklist
modulo-8/       the same for module 8
data/           datasets, with source, license and description in data/README.md
herramientas/   scripts that generate the student notebook and the dataset with anomalies, and download BloodMNIST
docs/           figures in this README
```

## Data and licenses

The code and course materials are released under the [MIT license](LICENSE).

The datasets have their own provenance and licenses. DNase comes from Davidian and Giltinan (1995) and is distributed with R (`datasets` package). BloodMNIST comes from MedMNIST v2 (Yang et al., 2023), built from the images of Acevedo et al. (2020), under a CC BY 4.0 license. Details for each dataset, and the description of the simulated and altered data, are in [`data/README.md`](data/README.md) (in Spanish).
