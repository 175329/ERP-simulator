# Proyecto Integrador Multidisciplinario
## ERP Inteligente con GitHub Actions, PostgreSQL, MongoDB, Neo4j e Inteligencia Artificial

**Fecha de entrega final:** 2 de diciembre de 2026

## Descripción General

Este proyecto integra las asignaturas de:

- Sistemas ERP
- Bases de Datos
- Inteligencia Artificial

El objetivo es desarrollar un **MVP (Minimum Viable Product)** de un ERP inspirado en SAP Business One, ejecutado completamente mediante GitHub, GitHub Actions y contenedores Docker.

La plataforma simulará procesos empresariales reales utilizando bases de datos relacionales, bases de datos NoSQL, grafos de conocimiento y agentes inteligentes.

---

# Objetivos

## Objetivo General

Diseñar e implementar una plataforma capaz de simular:

- Ventas
- Compras
- Inventarios
- Producción
- Planeación de Requerimientos de Materiales (MRP)
- Cadena de suministro
- Monitoreo IoT
- Diagnóstico inteligente

Todo ello orquestado mediante GitHub Actions.

---

# Arquitectura Tecnológica

```text
GitHub Actions
       │
       ▼
+----------------+
| Agentes IA     |
+----------------+
       │
       ▼
+----------------+
| PostgreSQL     |
| ERP Core       |
+----------------+
       │
 ┌─────┴─────┐
 ▼           ▼
MongoDB    Neo4j
Eventos    Conocimiento
```

---

# Componentes del Sistema

## PostgreSQL

Sistema transaccional principal.

Módulos:

- Productos
- Materiales
- Inventarios
- Ventas
- Compras
- Producción
- MRP

## MongoDB

Repositorio de eventos empresariales.

Colecciones:

- DemandEvents
- SensorEvents
- SupplyChainEvents

## Neo4j

Grafo de conocimiento empresarial.

Nodos principales:

- Producto
- Material
- Proveedor
- Almacén

## Inteligencia Artificial

Agentes:

- Agente de Ventas
- Agente de Compras
- Agente MRP
- Agente de Almacén
- Agente de Diagnóstico

---

# GitHub Actions

Workflows mínimos:

- ventas.yml
- mrp.yml
- compras.yml
- produccion.yml
- sensores.yml
- integration.yml

---

# Flujo Principal del MVP

```text
Agente de Ventas
      ↓
DemandEvents (MongoDB)
      ↓
MRP
      ↓
Orden de Compra
      ↓
Producción
      ↓
Inventario
      ↓
Sensor IoT
      ↓
Neo4j
      ↓
Agente de Diagnóstico
      ↓
Reporte Final
```

---

# Responsabilidades por Área

## ERP

- Definición de procesos
- Casos de uso
- BPMN
- KPI
- Validación funcional

## Bases de Datos

- Modelo ER
- PostgreSQL
- MongoDB
- Neo4j
- Integridad de datos

## Inteligencia Artificial

- Agentes inteligentes
- Diagnóstico automático
- Simulación IoT
- Automatización de decisiones

---

# Pruebas Automatizadas

## Unitarias

- Procedimientos SQL
- Agentes IA
- Consultas Neo4j

## Integración

Validar:

```text
Ventas → MRP → Compras → Producción
```

## Rendimiento

- Carga de órdenes
- Eventos MongoDB
- Consultas Neo4j

---

# Criterios de Evaluación del MVP

| Área | Valor |
|------|--------|
| Funcionalidad ERP | 25% |
| Bases de Datos | 20% |
| Inteligencia Artificial | 20% |
| GitHub Actions | 15% |
| Pruebas Automatizadas | 10% |
| Documentación | 10% |

---

# Criterio de Aceptación Final

El proyecto será considerado exitoso cuando una ejecución automática de **integration.yml** complete de forma autónoma:

1. Generación de demanda.
2. Registro de eventos.
3. Cálculo MRP.
4. Generación de compras.
5. Generación de producción.
6. Actualización de inventario.
7. Simulación IoT.
8. Diagnóstico utilizando Neo4j.
9. Generación de reporte final.

---

# Entregables

## ERP

- BPMN
- Casos de uso
- Documento funcional

## Bases de Datos

- schema.sql
- procedures.sql
- docker-compose.yml

## Inteligencia Artificial

- Agentes implementados
- Simulaciones
- Integración con Neo4j y MongoDB

## DevOps

- Workflows GitHub Actions
- Evidencias de ejecución
- Reportes de pruebas

---

# Fecha Límite

**2 de diciembre de 2026**

Repositorio único en GitHub con integración continua, documentación y evidencias de funcionamiento.
