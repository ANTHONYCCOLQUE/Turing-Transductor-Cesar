# Máquina de Turing Determinista como Transductor para el Cifrado César

### Con Trazabilidad y Visualización del Proceso Computacional

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📋 Descripción del Proyecto

Este proyecto implementa una **Máquina de Turing Determinista (DTM)** configurada como un transductor criptográfico para resolver el problema del **Cifrado César Generalizado** (Aritmética Modular sobre $\mathbb{Z}_{26}$).

A diferencia de los simuladores educativos tradicionales, este sistema adopta un enfoque de **Ingeniería de Software** utilizando una arquitectura modular **MVC (Modelo-Vista-Controlador)**. El objetivo principal no es solo simular el proceso de cifrado, sino proveer herramientas de **auditoría forense de datos**, generando trazabilidad visual (mapas de calor) y registros detallados de ejecución.

### 🚀 Características Principales

* **Arquitectura MVC Desacoplada:** Separación estricta entre la lógica del autómata (`Modelo`), la orquestación del flujo (`Controlador`) y la generación de gráficos (`Vista`).
* **Eficiencia Algorítmica:** Implementación de la función de transición $\delta$ mediante **Tablas Hash** (Diccionarios), garantizando un acceso de tiempo constante $O(1)$ y una complejidad total lineal $O(n)$.
* **Generación Dinámica de Reglas:** El autómata no usa reglas *hardcoded*. Calcula las transiciones matemáticamente basándose en la clave $K$ ingresada ($f(x) = (x + K) \pmod{26}$).
* **Auditoría y Trazabilidad (Data Lineage):**
    * Exportación automática de logs de ejecución a **CSV**.
    * Visualización científica de la memoria mediante **Mapas de Calor (Heatmaps)**.
    * Diagramas de estados generados dinámicamente con **NetworkX**.
* **Validación de Integridad (QA):** Sistema de auto-verificación que ejecuta una máquina inversa ($K' = -K$) para certificar matemáticamente la reversibilidad del cifrado sin pérdida de datos.

---

## 🛠️ Instalación y Requisitos

El proyecto requiere **Python 3.8** o superior. Las dependencias externas son mínimas y están enfocadas en la visualización científica.

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/tu-usuario/turing-transductor-cesar.git](https://github.com/tu-usuario/turing-transductor-cesar.git)
    cd turing-transductor-cesar
    ```

2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

    *Contenido de `requirements.txt`:*
    * `matplotlib` (Generación de Heatmaps)
    * `networkx` (Grafos de Estados)
    * `pandas` (Opcional, para manejo avanzado de CSV)

---

## 💻 Uso

Ejecuta el controlador principal desde la terminal:

```bash
python main.py
