# Guía Completa para Estudiantes
# Proyecto Integrador: ERP Inteligente con GitHub Actions, PostgreSQL, MongoDB, Neo4j e Inteligencia Artificial

**Fecha límite:** 2 de diciembre de 2026

---

# 1. Introducción

Este proyecto integra conocimientos de Sistemas ERP, Bases de Datos e Inteligencia Artificial para construir un simulador empresarial inspirado en SAP Business One.

El propósito no es replicar un ERP completo, sino desarrollar un MVP (Minimum Viable Product) capaz de automatizar procesos de negocio mediante GitHub Actions y agentes inteligentes.

---

# 2. Objetivos de Aprendizaje

Al finalizar el proyecto, el estudiante será capaz de:

- Modelar procesos empresariales.
- Diseñar bases de datos relacionales.
- Implementar bases de datos NoSQL.
- Utilizar grafos de conocimiento.
- Crear agentes inteligentes.
- Automatizar procesos mediante CI/CD.
- Aplicar pruebas automatizadas.
- Trabajar colaborativamente utilizando GitHub.

---

# 3. Contexto Empresarial

La empresa ficticia SmartTech Manufacturing fabrica equipos electrónicos.

Productos:

- Laptop Industrial X100
- Mini PC Industrial X200
- Controlador IoT X300

Materiales:

- Procesadores
- RAM
- SSD
- Tarjetas madre
- Carcasas
- Pantallas

---

# 4. Arquitectura General

```text
                    GitHub Actions
                           |
     -------------------------------------------------
     |                     |                         |
     V                     V                         V
 PostgreSQL           MongoDB                    Neo4j
 ERP Core        Eventos Empresariales      Grafo de Conocimiento
     |                     |                         |
     -------------------------------------------------
                           |
                           V
                  Agentes Inteligentes
```

---

# 5. Flujo Principal del Sistema

```text
Agente de Ventas
        |
        V
DemandEvents (MongoDB)
        |
        V
MRP
        |
        V
Orden de Compra
        |
        V
Orden de Producción
        |
        V
Inventario
        |
        V
Sensor IoT
        |
        V
Neo4j
        |
        V
Agente Diagnóstico
        |
        V
Reporte Final
```

---

# 6. MRP Explicado

## Escenario

Pedido:

100 laptops.

BOM:

- 1 tarjeta madre
- 2 memorias RAM
- 1 SSD

Inventario:

- Tarjetas: 50
- RAM: 100
- SSD: 60

## Cálculo

```text
Necesidad tarjetas = 100
Inventario = 50
Comprar = 50

Necesidad RAM = 200
Inventario = 100
Comprar = 100

Necesidad SSD = 100
Inventario = 60
Comprar = 40
```

Resultado:

El agente MRP genera órdenes de compra.

---

# 7. Responsabilidades del Equipo ERP

## Actividades

- Definir requerimientos.
- Elaborar BPMN (Business Process Model and Notation o Modelo y Notación de Procesos de Negocio).
- Diseñar casos de uso.
- Definir KPI.
- Validar funcionalidad.

## Entregables

- Documento funcional.
- Casos de uso.
- Historias de usuario.
- Diagramas BPMN.

---

# 8. Responsabilidades del Equipo de Bases de Datos

## PostgreSQL

Tablas mínimas:

```text
productos
materiales
inventario
orden_venta
orden_compra
orden_produccion
bom
```

## MongoDB

Colecciones:

```text
DemandEvents
SensorEvents
SupplyChainEvents
```

## Neo4j

Nodos:

```text
Producto
Material
Proveedor
Almacen
```

---

# 9. Responsabilidades del Equipo de IA

## Agente de Ventas

Genera pedidos.

## Agente de Compras

Selecciona proveedores.

## Agente MRP

Calcula requerimientos.

## Agente de Almacén

Busca materiales mediante algoritmos de búsqueda.

## Agente de Diagnóstico

Determina causas raíz usando Neo4j.

---

# 10. Definición Detallada de Agentes

## Agente de Ventas

Entradas:

- Clientes
- Historial

Salidas:

- Órdenes de venta

## Agente de Compras

Entradas:

- Recomendaciones MRP

Salidas:

- Órdenes de compra

## Agente de Producción

Entradas:

- Órdenes de fabricación

Salidas:

- Producto terminado

## Agente IoT

Entradas:

- Datos simulados

Salidas:

- Eventos MongoDB

---

# 11. Estructura del Repositorio GitHub

```text
erp-simulator/
│
├── docs/
│   ├── requerimientos
│   ├── arquitectura
│   └── manuales
│
├── database/
│   ├── schema.sql
│   ├── data.sql
│   ├── procedures.sql
│   └── tests
│
├── mongodb/
├── neo4j/
├── ai-agents/
├── tests/
│
└── .github/
    └── workflows/
```

---

# 12. GitHub Flow

```text
Issue
  |
  V
Branch
  |
  V
Commit
  |
  V
Pull Request
  |
  V
Review
  |
  V
Merge
```

---

# 13. Ejemplo de Issue

Título:

```text
Crear procedimiento sp_generar_mrp
```

Descripción:

```text
Implementar la lógica para calcular materiales requeridos.
```

Criterios de aceptación:

```text
- Ejecuta correctamente.
- Genera recomendaciones.
- Incluye pruebas.
```

---

# 14. Ejemplo de Pull Request

Título:

```text
Implementación de sp_generar_mrp
```

Debe incluir:

- Descripción.
- Capturas.
- Evidencias.
- Resultados de pruebas.

---

# 15. Estrategia de Testing

## Unitarias

- SQL
- Python
- Neo4j

## Integración

```text
Ventas -> MRP -> Compras -> Producción
```

## Rendimiento

- Miles de registros.
- Eventos simultáneos.

---

# 16. Workflows Obligatorios

```text
ventas.yml
mrp.yml
compras.yml
produccion.yml
sensores.yml
integration.yml
```

---

# 17. Evidencias Individuales

Cada alumno deberá entregar:

1. Issue asignado.
2. Pull Request aprobado.
3. Documento Markdown.
4. Caso de prueba.
5. Evidencia en GitHub Actions.

---

# 18. Rúbrica Individual

## Excelente (90-100)

- Entregables completos.
- Código funcional.
- PR aprobado.
- Evidencias completas.

## Bueno (80-89)

- Cumple objetivos principales.
- Algunos detalles menores.

## Suficiente (70-79)

- Funciona parcialmente.

## Insuficiente (<70)

- No entrega o no integra.

---

# 19. Presentación Final

Duración recomendada:

20 minutos.

## Estructura

### Parte 1

Problema empresarial.

### Parte 2

Arquitectura.

### Parte 3

Demostración.

### Parte 4

Resultados.

### Parte 5

Lecciones aprendidas.

---

# 20. Checklist Final

## ERP

- [ ] BPMN
- [ ] Casos de uso
- [ ] KPI

## Bases de Datos

- [ ] PostgreSQL
- [ ] MongoDB
- [ ] Neo4j

## IA

- [ ] Agentes
- [ ] Diagnóstico

## DevOps

- [ ] Workflows
- [ ] Pruebas
- [ ] Integración

---

# 21. Criterio de Aceptación del MVP

La simulación debe ejecutar automáticamente:

```text
Venta
  ↓
MongoDB
  ↓
MRP
  ↓
Compra
  ↓
Producción
  ↓
Inventario
  ↓
IoT
  ↓
Neo4j
  ↓
Diagnóstico
  ↓
Reporte
```

Si el flujo completo puede ejecutarse desde GitHub Actions sin intervención manual, el MVP se considera exitoso.
