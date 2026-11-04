# Guía para Estudiantes
# Proyecto Integrador: ERP Inteligente con GitHub Actions

**Fecha de entrega:** 2 de diciembre de 2026

## ¿Qué van a construir?

Desarrollarán un MVP (Minimum Viable Product) de un ERP inspirado en SAP Business One utilizando:

- GitHub
- GitHub Actions
- Docker
- PostgreSQL
- MongoDB
- Neo4j
- Inteligencia Artificial

El sistema simulará una empresa manufacturera que vende productos, compra materiales, fabrica productos y toma decisiones automáticas mediante agentes inteligentes.

---

# Objetivo General

Construir un sistema capaz de ejecutar de forma automática:

1. Generación de demanda.
2. Planeación MRP.
3. Compras.
4. Producción.
5. Control de inventarios.
6. Monitoreo IoT.
7. Diagnóstico inteligente.

Todo deberá ejecutarse mediante GitHub Actions.

---

# Equipos Participantes

## Sistemas ERP

Responsables de:

- Requerimientos.
- Casos de uso.
- BPMN.
- KPI.
- Validación funcional.

### Entregables

- Documento funcional.
- Diagramas BPMN.
- Casos de uso.
- Historias de usuario.
- Escenarios de simulación.

---

## Bases de Datos

Responsables de:

- PostgreSQL.
- MongoDB.
- Neo4j.
- Integridad de datos.

### Entregables

- DER.
- Diccionario de datos.
- schema.sql.
- data.sql.
- procedures.sql.
- Docker Compose.
- Casos de prueba.

---

## Inteligencia Artificial

Responsables de:

- Agentes inteligentes.
- Simulación IoT.
- Diagnóstico.
- Automatización.

### Entregables

- Código fuente.
- Agentes implementados.
- Pruebas.
- Evidencias.

---

# Arquitectura del Proyecto

```text
Agente de Ventas
      ↓
MongoDB
      ↓
MRP
      ↓
PostgreSQL
      ↓
Compras
      ↓
Producción
      ↓
Inventario
      ↓
Sensor IoT
      ↓
Neo4j
      ↓
Agente Diagnóstico
```

---

# Repositorio GitHub

```text
erp-simulator/
│
├── docs/
├── database/
├── ai-agents/
├── neo4j/
├── mongodb/
├── tests/
└── .github/workflows/
```

---

# Workflows Obligatorios

- ventas.yml
- mrp.yml
- compras.yml
- produccion.yml
- sensores.yml
- integration.yml

---

# Tecnologías

## PostgreSQL

Sistema transaccional principal.

Tablas mínimas:

- productos
- materiales
- inventario
- orden_venta
- orden_compra
- orden_produccion
- bom

## MongoDB

Colecciones:

- DemandEvents
- SensorEvents
- SupplyChainEvents

## Neo4j

Nodos:

- Producto
- Material
- Proveedor
- Almacén

---

# Agentes Inteligentes

## Agente de Ventas

Genera pedidos automáticamente.

## Agente de Compras

Selecciona proveedores.

## Agente MRP

Calcula necesidades de materiales.

## Agente de Almacén

Localiza materiales y rutas.

## Agente de Diagnóstico

Analiza problemas mediante Neo4j.

---

# Evidencias Individuales

Cada estudiante deberá entregar:

1. Un Issue asignado.
2. Un Pull Request aprobado.
3. Un documento técnico en Markdown.
4. Un caso de prueba automatizado.
5. Evidencia de ejecución en GitHub Actions.

---

# Cronograma Resumido

## Semana 1

- Requerimientos.
- Modelo ER.
- Arquitectura.

## Semana 2

- PostgreSQL.
- MongoDB.
- Neo4j.
- Primeros agentes.

## Semana 3

- MRP.
- Compras.
- Producción.
- GitHub Actions.

## Semana 4

- Integración.
- Pruebas.
- Documentación.

## Semana Final

- Presentación.
- Simulación completa.

---

# Criterios de Evaluación

- Funcionalidad ERP: 25%
- Base de Datos: 20%
- Inteligencia Artificial: 20%
- GitHub Actions: 15%
- Pruebas Automatizadas: 10%
- Documentación: 10%

---

# Condición de Éxito

El proyecto será considerado exitoso cuando el workflow integration.yml pueda ejecutar automáticamente:

1. Venta.
2. Evento MongoDB.
3. MRP.
4. Compra.
5. Producción.
6. Inventario.
7. Evento IoT.
8. Consulta Neo4j.
9. Diagnóstico.
10. Reporte final.

---

# Recomendaciones

- Realizar commits frecuentes.
- Trabajar mediante ramas.
- Documentar cada avance.
- Automatizar pruebas desde el inicio.
- Mantener comunicación entre los tres grupos.

¡El éxito del proyecto depende de la integración entre ERP, Bases de Datos e Inteligencia Artificial!
