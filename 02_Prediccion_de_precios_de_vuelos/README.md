# ✈️ Predicción de Precios de Vuelos

Este proyecto desarrolla un modelo predictivo para **estimar precios de vuelos** utilizando datos históricos de tarifas en clases **business** y **economy**.  
Se implementan técnicas de Machine Learning y optimización de hiperparámetros para mejorar la capacidad de predicción.

---

## 🎯 Objetivos
- Analizar datos de vuelos en distintas clases tarifarias.  
- Implementar modelos de regresión para predecir precios.  
- Evaluar el desempeño de diferentes algoritmos (Random Forest, XGBoost).  
- Aplicar técnicas de optimización de hiperparámetros (GridSearchCV, Optuna).  

---

## 🗂️ Estructura del Proyecto
```
02_Prediccion_de_precios_de_vuelos/
├─ business.xlsx         # Dataset de vuelos clase business
├─ economy.xlsx          # Dataset de vuelos clase economy
├─ funciones.py          # Funciones auxiliares
├─ Notebook_02.ipynb     # Desarrollo principal del proyecto
└─ requirements.txt      # Librerías necesarias
```

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.12  
- **Librerías principales:**  
  - scikit-learn → Modelos de ML  
  - XGBoost → Modelos de boosting  
  - Optuna, GridSearchCV → Optimización de hiperparámetros  
  - Pandas, NumPy → Manipulación de datos  
  - Matplotlib, Seaborn → Visualización  

---

## 📊 Resultados Clave
- Los modelos basados en **Random Forest y XGBoost** obtuvieron mejores resultados frente a regresiones simples.  
- La optimización de hiperparámetros mejoró la **precisión y robustez** de las predicciones.  
- Se identificaron variables clave en la determinación de precios de vuelos.  

---

## 🧠 Reflexión
Este proyecto reforzó la importancia de la **optimización de modelos** y la elección adecuada de algoritmos según la naturaleza del problema.  
La predicción de precios es un ejemplo de aplicación práctica con gran impacto en la industria aérea y en la planificación de viajes.

---

## ▶️ Ejecución
1. Clonar el repositorio o descargar la carpeta.  
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Abrir el notebook:
   ```bash
   jupyter notebook Notebook_02.ipynb
   ```

---


✍️ Autor: **José Aravena**

