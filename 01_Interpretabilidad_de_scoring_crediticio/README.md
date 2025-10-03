# 📌 Interpretabilidad de Scoring Crediticio

Este proyecto implementa un modelo de **clasificación para scoring crediticio** y lo complementa con técnicas de **interpretabilidad de modelos**.  
El enfoque busca no solo obtener buenas métricas de predicción, sino también explicar de manera clara qué variables influyen en las decisiones del modelo.

---

## 🎯 Objetivos
- Construir un modelo de **clasificación** para predecir riesgo crediticio.  
- Aplicar **regularización** para mejorar la generalización del modelo.  
- Implementar técnicas de interpretabilidad como **SHAP** y **LIME**.  
- Evaluar métricas de desempeño (precisión, recall, F1-score, AUC).  
- Generar conclusiones sobre la transparencia y aplicabilidad del modelo en contextos financieros.

---

## 🗂️ Estructura del Proyecto
```
01_Interpretabilidad_de_scoring_crediticio/
├─ funciones.py          # Funciones auxiliares
├─ Notebook_01.ipynb     # Desarrollo principal del proyecto
└─ requirements.txt      # Librerías necesarias
```

---

## 🛠️ Tecnologías Utilizadas
- **Lenguaje:** Python 3.12  
- **Librerías principales:**  
  - scikit-learn → Modelado predictivo  
  - SHAP → Interpretabilidad global y local  
  - LIME → Interpretabilidad local  
  - Pandas, NumPy → Manipulación de datos  
  - Matplotlib, Seaborn → Visualización  

---

## 📊 Resultados Clave
- El modelo entrenado logra un **equilibrio entre precisión y recall**, lo cual es esencial en el contexto crediticio.  
- Con **SHAP** se identificaron las variables con mayor impacto en la predicción de riesgo.  
- Con **LIME** se validaron las predicciones individuales, mostrando la importancia de la transparencia en decisiones sensibles.  

---

## 🧠 Reflexión
Este proyecto permitió comprender que en problemas de **riesgo crediticio** no basta con lograr un modelo de alta precisión, sino que es fundamental **explicar las predicciones**.  
La interpretabilidad aporta confianza tanto a los analistas como a los usuarios finales, ayudando a tomar decisiones más responsables y justas.

---

## ▶️ Ejecución
1. Clonar el repositorio o descargar la carpeta.  
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Abrir el notebook:
   ```bash
   jupyter notebook Notebook_01.ipynb
   ```

---


✍️ Autor: **José Aravena**


