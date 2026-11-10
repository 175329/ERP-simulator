# Modelo de Procesos de Negocio (BPMN) - Módulo MRP: Reglas de Orden de Compra y Producción
# Documento de requerimientos iniciales

## Simulador ERP, sistema MRP

### Módulo: Reglas de orden de compra y de orden de producción

**Autor/a:** Yazmin Guerrero Guevara - 182483

\---

# 1\) Definición de requerimientos funcionales

* **Límites de Stock:** El sistema debe permitir registrar y actualizar los límites de stock (stock mínimo, stock máximo y punto de reorden) para cada material o componente en el inventario.
* **Generación de Órdenes de Compra:** El motor MRP debe ser capaz de respetar estrictamente los límites de stock definidos al calcular las necesidades, generando propuestas o registros automáticos de Órdenes de Compra (OC) solo cuando el inventario disponible esté por debajo del punto de reorden.
* **Generación de Órdenes de Producción:** El sistema debe detonar automáticamente Órdenes de Producción (OP) basadas en la explosión de materiales (BOM) cuando exista demanda de productos terminados y se valide la disponibilidad de componentes necesarios.

\---

# 2\) Descripción de las reglas de negocio que aplican

* **Validación de Stock Mínimo para Compras:** Ninguna Orden de Compra de materia prima puede ser procesada por debajo de la cantidad necesaria para alcanzar el stock óptimo o para cubrir el faltante calculado por el MRP, evitando compras innecesarias.
* **Restricción de Lotes de Producción:** Las Órdenes de Producción deben ajustarse a los múltiplos o tamaños de lote establecidos en el catálogo de manufactura (no se pueden lanzar fracciones de productos).
* **Disponibilidad de Materiales para Producción:** El sistema debe verificar que los componentes de la Lista de Materiales (BOM) estén disponibles en inventario antes de liberar una Orden de Producción; de lo contrario, el MRP debe frenar la orden o sugerir de manera simultánea la Orden de Compra del componente faltante.

\---

# 3\) Pruebas unitarias

* **Cálculo de punto de reorden:** Verificar que la función lógica devuelva `true` para la generación de una Orden de Compra únicamente cuando $\\text{Stock Actual} \\le \\text{Stock Mínimo}$.
* **Validación de lotes de producción:** Comprobar que el algoritmo de cálculo de órdenes de producción redondee correctamente hacia arriba o aplique el múltiplo de lote configurado para el producto ensamblado.
* **Detección de faltantes en BOM:** Evaluar de forma aislada que el método de desglose de materiales identifique correctamente qué componentes faltan en el inventario al simular una orden de producción.

\---

# 4\) Pruebas funcionales

* **Flujo completo de Orden de Compra:** Simular una reducción de inventario por debajo del mínimo establecido y comprobar que el sistema genera exitosamente el registro de la Orden de Compra con los datos correctos del proveedor y la cantidad faltante.
* **Flujo completo de Orden de Producción:** Ingresar un pedido de venta de producto terminado, ejecutar el MRP y verificar que se genera la Orden de Producción junto con el bloqueo o descuento correcto de los insumos en el almacén.
* **Restricción por falta de insumos:** Validar que, si se intenta liberar una Orden de Producción sin tener la materia prima necesaria, el sistema impida el flujo y emita la alerta correspondiente o sugiera la compra.

\---

# 5\) Integridad de los datos (Enfoque de integración en Git/GitHub)

Para garantizar la consistencia, calidad y confiabilidad de la información dentro del módulo de órdenes de compra y producción, se establecen las siguientes reglas de integridad:

* **Validación de tipos de datos y restricciones de nulos:** Todos los campos monetarios, cantidades de materiales, fechas de entrega y folios deben contar con validaciones estrictas en el modelo y base de datos que impidan valores nulos (`NOT NULL`) y me aseguren el tipo de dato correcto (por ejemplo, enteros positivos para cantidades y flotantes con precisión para costos).
* **Prevención estricta de stock negativo:** Ninguna transacción derivada de una orden de compra (entradas) o de una orden de producción (salidas/consumo de insumos) podrá permitir que el inventario disponible de un material caiga en números negativos. El sistema debe rechazar la operación si el stock es insuficiente.
* **Valores lógicos y rangos permitidos:** Los estados de las órdenes (ej. *Pendiente*, *Aprobada*, *En Proceso*, *Cancelada*, *Finalizada*) deben estar restringidos a un catálogo o enumeración fija (`Enum`), evitando la inserción de cadenas de texto erróneas, vacías o valores atípicos.
* **Consistencia referencial - Llaves foráneas:** Las órdenes de compra y de producción deben mantener una relación de integridad referencial estricta con las tablas de catálogo de materiales, proveedores y almacenes, evitando la creación de registros huérfanos o asociados a elementos inexistentes en el sistema.


Este documento traslada los requerimientos funcionales, reglas de negocio y validaciones del **Simulador ERP - Módulo MRP** a una representación de diagrama de proceso bajo el estándar **Business Process Model and Notation (BPMN)**, utilizando la sintaxis gráfica de **Mermaid**.

---

## 1. Mapeo de Elementos BPMN

De acuerdo con la especificación de BPMN, el diagrama se estructuró utilizando los siguientes elementos básicos:

* **Carriles de Nado (Swimlanes / Pools):**
  * **Ventas / Cliente:** Detonador inicial de demanda.
  * **Motor MRP (Sistema):** Evaluación de inventarios, explosión de materiales (BOM) y toma de decisiones.
  * **Almacén / Inventario:** Gestión e inspección de stock y límites de reorden.
  * **Compras / Proveedores:** Generación y procesamiento de Órdenes de Compra (OC).
  * **Producción:** Liberación de Órdenes de Producción (OP) ajustadas a lotes.

* **Eventos:**
  * **Iniciales:** Ingreso de pedido de venta / Reducción de stock.
  * **Intermedios:** Alertas por insumos faltantes o validaciones.
  * **Finales:** OC procesada, OP liberada, Proceso bloqueado/frenado.

* **Compuertas de Control (Gateways):**
  * Evaluaciones condicionales para:
    * $\text{Stock Actual} \le \text{Punto de Reorden}$
    * Disponibilidad completa de insumos según Lista de Materiales (BOM).

---

## 2. Diagrama de Proceso BPMN (Mermaid)

```mermaid
graph TD
    %% Evento de Inicio
    SubGraph1[Ventas] -->|1. Ingreso de Pedido de Venta / Demanda PT| StartEvent(("● Evento Inicial:<br>Demanda Registrada"))

    subgraph MRP_Engine [" Motor MRP (Sistema) "]
        StartEvent --> Activity1["Explosión de Materiales (BOM)"]
        Activity1 --> Activity2["Consultar Stock Disponible de Componentes"]
        
        %% Compuerta 1: Disponibilidad de BOM
        Activity2 --> Gateway1{"¿Componentes BOM<br>Disponibles?"}
        
        %% Ruta No Disponible
        Gateway1 -- No --> IntermediateAlert["Emite Alerta de Insuficiencia"]
        IntermediateAlert --> Activity3["Calcular Faltante según Stock Óptimo"]
        
        %% Ruta Disponible
        Gateway1 -- Sí --> Activity4["Ajustar Lote a Múltiplos de Manufactura"]
        Activity4 --> Activity5["Bloquear/Reservar Insumos en Almacén"]
        Activity5 --> EndProduction(("● Evento Final:<br>Liberar Orden de Producción (OP)"))
    end

    subgraph Almacen_Compras [" Almacén / Compras "]
        Activity3 --> Gateway2{"¿Stock Actual <=<br>Punto de Reorden?"}
        
        Gateway2 -- Sí --> Activity6["Generar Propuesta/Registro de Orden de Compra (OC)"]
        Gateway2 -- No --> CancelEvent(("● Evento Final:<br>Frenar Orden (Sin Recompra)"))
        
        Activity6 --> Activity7["Validar Datos de Proveedor y Cantidad Mínima"]
        Activity7 --> Activity8["Procesar Entrada de Materia Prima"]
        Activity8 --> Activity9["Actualizar Stock (Evitar Stock Negativo)"]
        Activity9 --> Activity2
    end

    %% Estilos de Nodos
    style StartEvent fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:#fff
    style EndProduction fill:#e74c3c,stroke:#c0392b,stroke-width:2px,color:#fff
    style CancelEvent fill:#e74c3c,stroke:#c0392b,stroke-width:2px,color:#fff
    style Gateway1 fill:#f1c40f,stroke:#f39c12,stroke-width:2px
    style Gateway2 fill:#f1c40f,stroke:#f39c12,stroke-width:2px
```

---

## 3. Especificación de Reglas e Integridad de Datos

### Reglas de Negocio Incorporadas
1. **Límites de Stock:** Se valida que la Orden de Compra sólo sea generada si $\text{Stock Actual} \le \text{Punto de Reorden}$.
2. **Restricción de Lotes:** La actividad de ajuste de lote aplica redondeo hacia arriba / múltiplos configurados para evitar fracciones.
3. **Disponibilidad BOM:** Antes de liberar una Orden de Producción, se verifica el stock de insumos. Si faltan componentes, se emite una alerta y se sugiere/genera la Orden de Compra correspondiente.

### Reglas de Integridad (Git/Base de Datos)
* **Prevención de Stock Negativo:** Toda salida/consumo de insumos exige validación previa de disponibilidad suficiente antes de proceder.
* **Tipos de Datos y Enum:** Campos monetarios, folios y cantidades con restricciones estrictas `NOT NULL` y estados de las órdenes acotados a enumeraciones fijas (`Pendiente`, `Aprobada`, `En Proceso`, `Cancelada`, `Finalizada`).
* **Integridad Referencial:** Claves foráneas asociadas a catálogos existentes de materiales, proveedores y almacenes.
