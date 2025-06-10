# ENLACE VIDEO #

    https://www.youtube.com/watch?v=4NYK3fhhV00

# ENLACE VIDEO #


# Representación de Fixtures Deportivos como Árboles Binarios en Python

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema de fixtures deportivos utilizando árboles binarios representados con listas anidadas en Python, sin usar programación orientada a objetos. El sistema permite crear, visualizar y simular el progreso de torneos de eliminación directa.

## 👥 Equipo de Desarrollo

- **Luciano José Cartagena** - lucianocartagena17@gmail.com
- **Santiago Arroquigaray** - arroqui192@gmail.com

**Materia:** Programación I  
**Profesor:** Sebastián Bruselario  
**Tutora:** Verónica Carbonari  
**Fecha:** Junio 2025

## 🎯 Objetivos

- Implementar árboles binarios usando únicamente listas de Python
- Modelar torneos deportivos de eliminación directa
- Simular el progreso de partidos y avance de ganadores
- Demostrar aplicaciones prácticas de estructuras de datos

## 🏗️ Estructura del Proyecto

```
fixture-deportivo-arboles/
│
├── fixture_arbol.py          # Código principal
│
├── docs/
│   ├── TP_Integrador_Fixtures_Arboles.pdf    # Documento completo
│   └── Presentacion_Fixtures_Arboles.pptx    # Slides del proyecto
│   └── Presentacion_Fixtures_Arboles.pdf     # Slides del proyecto
│
├── README.md                     # Este archivo
```

## 🚀 Instalación y Uso

### Requisitos
- Python 3.8 o superior
- No requiere librerías externas

### Instalación
```bash
git https://github.com/Pitdog192/tp_integrador_arboles_listas.git
cd fixture-deportivo-arboles
```

### Ejecución
```bash
python fixture_arbol.py
```

### Ejemplo de Uso
```python
# Crear fixture de 8 equipos
fixture = crear_fixture_8_equipos()

# Simular resultados
simular_cuartos_de_final(fixture)
simular_semifinales(fixture)
simular_final(fixture)

# Visualizar resultado
imprimir_fixture_completo(fixture)
```

## 📊 Funcionalidades

- ✅ Creación de fixtures con estructura de árbol binario
- ✅ Visualización rotada del torneo
- ✅ Simulación de partidos y avance de ganadores
- ✅ Recorridos preorden, inorden y postorden
- ✅ Análisis de complejidad algorítmica

## 📈 Análisis de Complejidad

| Operación | Complejidad Temporal | Complejidad Espacial |
|-----------|---------------------|---------------------|
| Crear fixture | O(n) | O(n) |
| Simular partido | O(1) | O(1) |
| Imprimir árbol | O(n) | O(h) |
| Recorridos | O(n) | O(h) |

Donde n = número de partidos, h = altura del árbol

## 🤔 Reflexiones del Equipo

### Aprendizajes Obtenidos
- **Luciano**: "Comprendí cómo las estructuras de datos abstractas pueden modelar problemas reales. "

- **Santiago**: "La implementación con listas me ayudó a entender mejor la recursión, aunque es menos eficiente que usar clases, es muy didáctico para aprender."

### Desafíos Enfrentados
- Visualización clara del árbol rotado
- Manejo de casos edge (equipos impares, torneos incompletos)
- Balance entre simplicidad y funcionalidad

### Mejoras Futuras
- Implementar torneos de doble eliminación
- Agregar interfaz gráfica
- Soporte para torneos con número variable de equipos
- Estadísticas y métricas del torneo

## 📚 Recursos Utilizados

- Documentación oficial de Python
- "Introduction to Algorithms" - Cormen et al.
- "Algorithms" - Sedgewick & Wayne
- Tutoriales de GeeksforGeeks

## 📄 Licencia

Este proyecto es de uso académico para la materia Programación I.

## 🤝 Contribuciones

Este es un proyecto académico. Para sugerencias o mejoras, contactar a los autores.

---
*Trabajo Práctico Integrador - Programación I - 2025*
