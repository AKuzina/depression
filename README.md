# depression

**Задачи:**
* 4 класса (D, E, DE, C)
* Диагностирование депрессии, 100 пациентов (D+DE vs E+C)
* Диагностирование депрессии, 50 пациентов (D vs C)
* Диагностирование депрессии у эпилептиков, 50 пациентов (DE vs E)
* Диагностирование эпилепсии, 100 пациентов (E+DE vs D+C)
* Диагностирование эпилепсии, 50 пациентов (E vs C)
* Диагностирование эпилепсии (temporal lobe), 81 пациент (TLE (31) vs C+D (50))
* Диагностирование эпилепсии (temporal lobe), 56 пациентов (TLE (31) vs C (25))
* MRI-positive/negative

**Datasets**
* MRI features (volumes + thicknesses), 100 пациентов
* fMRI features (processed by CONN), 100 пациентов
* MRI features (volumes + thicknesses) with mprage, 90 пациентов


**Preprocessing**
* No dimensionality reduction or feature selection
* With dimensionality reduction (*\[2, 3, 5, 10, 15, 20\] components*)
  * PCA
  * LDA
  * LLE
* With features selection (*\[5, 10, 20, 50, 100\] features*)
  * ExtraTreesClassifier
  * LogisticRegression
  * SelectKBest(chi2)
  * SelectKBest(f_classif)

**Baseline classifiers**
* kNN
  * n_neighbours, p, weightning scheme
* SVC
  * kernel, C, gamma
* LR
   * C
* RF
  * n_estimators


