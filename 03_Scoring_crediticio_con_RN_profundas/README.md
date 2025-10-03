# 🤖 Scoring Crediticio con Redes Neuronales Profundas

Este proyecto implementa un modelo de **Redes Neuronales Profundas (DNN)** aplicado al **scoring crediticio**, con el objetivo de clasificar clientes en función de su nivel de riesgo financiero.  
Se emplea el dataset `german_credit_data.csv` como base de entrenamiento y validación.

---

## 🎯 Objetivos
- Implementar un modelo de clasificación basado en **Deep Learning**.  
- Comparar el desempeño con modelos tradicionales.  
- Evaluar métricas clave como **precisión, recall, F1-score y AUC**.  
- Identificar las principales variables que afectan el riesgo crediticio.  

---

## 🗂️ Estructura del Proyecto
```
03_Scoring_crediticio_con_RN_profundas/
├─ german_credit_data.csv    # Dataset de crédito alemán
├─ funciones.py              # Funciones auxiliares
├─ Notebook_03.ipynb         # Desarrollo principal del proyecto
└─ requirements.txt          # Librerías necesarias
```

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.12  
- **Librerías principales:**  
  - TensorFlow/Keras → Modelado de redes neuronales profundas  
  - scikit-learn → Preprocesamiento y métricas  
  - Pandas, NumPy → Manipulación de datos  
  - Matplotlib, Seaborn → Visualización  

---

## 📊 Resultados Clave
- El modelo de **Red Neuronal Profunda** logró un mejor rendimiento en términos de recall y AUC comparado con modelos básicos.  
- Se detectaron problemas de **overfitting**, mitigados con técnicas de regularización y dropout.  
- El dataset `german_credit_data` permitió identificar patrones relevantes en clientes de alto y bajo riesgo.  

---

## 🧠 Reflexión
Este proyecto permitió explorar las ventajas y desafíos de las **Redes Neuronales Profundas** frente a métodos tradicionales.  
Si bien ofrecen mayor capacidad de representación, requieren **cuidadoso preprocesamiento y regularización** para evitar problemas de sobreajuste.

---

## ▶️ Ejecución
1. Clonar el repositorio o descargar la carpeta.  
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Abrir el notebook:
   ```bash
   jupyter notebook Notebook_03.ipynb
   ```

---


✍️ Autor: **José Aravena**
