<!--
Sync Impact Report:
- Version change: Initial template -> 1.0.0
- Modified principles:
  - [PRINCIPLE_1_NAME] -> I. Cero Sobreingeniería (Simplicidad Radical)
  - [PRINCIPLE_2_NAME] -> II. Prohibición Estricta de Spark, PySpark y display()
  - [PRINCIPLE_3_NAME] -> III. Desarrollo Dirigido por Especificación (SDD)
  - [PRINCIPLE_4_NAME] -> IV. Validación de Contrato mediante Aserciones Puras
  - [PRINCIPLE_5_NAME] -> V. Salida Estándar Nativa
- Added sections:
  - Restricciones Tecnológicas de Plataforma (Databricks)
  - Ciclo de Vida SDD
- Removed sections: None
- Follow-up TODOs: None
-->

# Databricks Minimalist Python Constitution

## Core Principles

### I. Cero Sobreingeniería (Simplicidad Radical)
Toda solución debe implementarse utilizando la mínima expresión sintáctica y funcional necesaria para cumplir con el requerimiento. Queda prohibida la introducción de clases auxiliares, decoradores, fábricas, wrappers o abstracciones innecesarias cuando una función nativa satisface el caso de uso. Para emisión de texto estándar, el código final debe consistir estrictamente en la invocación de `print()`.

### II. Prohibición Estricta de Spark, PySpark y display()
En la ejecución dentro de Databricks Notebooks para tareas básicas de scripts o Hello World, queda terminantemente prohibido el uso o importación de `pyspark`, `pyspark.sql`, inicialización de `SparkSession`, creación de DataFrames o RDDs, y la llamada a la función propietaria de Databricks `display()`.

### III. Desarrollo Dirigido por Especificación (SDD)
Ninguna línea de código de producción o script debe escribirse sin una especificación formal previa que defina claramente: Objetivo, Entradas, Proceso y Salidas. La especificación gobierna la implementación y no al revés.

### IV. Validación de Contrato mediante Aserciones Puras
Antes de dar por válida cualquier implementación o emisión de efectos secundarios, las precondiciones, el estado de las variables y las postcondiciones deben ser verificadas mediante contratos ejecutables expresados exclusivamente a través de la instrucción nativa `assert` de Python, sin frameworks de testing pesados.

### V. Salida Estándar Nativa
La entrega del resultado al usuario final o al entorno del notebook debe realizarse exclusivamente a través de la interfaz estándar de salida de Python (`print()`), garantizando portabilidad absoluta y desacoplamiento del runtime de Databricks.

## Restricciones Tecnológicas de Plataforma (Databricks)

El entorno de ejecución objetivo es una celda de Notebook en Databricks con kernel de Python:
- No se deben utilizar comandos mágicos (`%spark`, `%sql`) si el requerimiento es puramente Python.
- No se deben invocar utilidades de `dbutils` a menos que sea explícitamente requerido por el contrato.
- El costo computacional en el clúster debe limitarse a la ejecución en el driver sin distribuir tareas en nodos de trabajo.

## Ciclo de Vida SDD

Todo desarrollo en este repositorio debe seguir secuencialmente las cuatro fases operativas:
1. **Fase 1: Especificación**: Documentar objetivo, entrada, proceso y salida esperada.
2. **Fase 2: Contrato de Prueba**: Definir los criterios inmutables de aceptación.
3. **Fase 3: Implementación**: Producir el código fuente mínimo, exacto y sin sobreingeniería.
4. **Fase 4: Ejecución del Contrato**: Evaluar las aserciones formales antes y/o después de la emisión del efecto secundario.

## Governance

Esta constitución rige como ley suprema para el desarrollo de scripts y flujos en el proyecto. Cualquier intento de sobrediseñar o incluir dependencias innecesarias de Spark requerirá una propuesta de enmienda constitucional y justificación técnica fundada. Las revisiones de código deben rechazar cualquier solución que viole el principio de Simplicidad Radical.

**Version**: 1.0.0 | **Ratified**: 2026-11-09 | **Last Amended**: 2026-11-09
