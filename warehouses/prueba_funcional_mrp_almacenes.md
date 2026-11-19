# 🧪 Prueba Funcional: Gestión de Almacenes (Warehouses) en MRP

**Equipo:** Módulo de Almacenes (*Warehouses*)  
**Módulo ERP:** Planificación de Requerimientos de Materiales (MRP) / Gestión de Inventarios  
**Artículo de Prueba:** `A50009` (*J.B. Officeprint 5000*)  
**Escenario MRP:** `Q2_A5_2026`  

---

## 📋 Descripción de la Prueba Funcional

### **Ejecución de MRP por Almacén Específico vs. Consolidado (Multi-almacén)**

**Objetivo:**  
Validar que el Asistente de MRP discrimine correctamente la disponibilidad de inventario físico, oferta y demanda según la configuración de ejecución (*Por Almacén* vs. *Consolidado por Empresa*), asegurando que no se asuma disponibilidad errónea de stock ubicado en almacenes excluidos o independientes.

---

## ⚙️ Precondiciones y Datos de Entrada

1. **Configuración de Almacenes:**
   * **Almacén `01` (General Warehouse / Producción):** Stock físico inicial = `0 unidades`.
   * **Almacén `02` (Backup Warehouse / Central):** Stock físico inicial = `50 unidades` del artículo `A50009`.
   * **Almacén `03` (Drop Ship):** Excluido de la planificación estándar.
2. **Demanda Activa:**
   * Se registra una **Orden de Venta** (o Pronóstico `PSF1`) por `20 unidades` del artículo `A50009` con fecha de entrega dentro del horizonte (`26/10/2026` – `27/10/2026`), asignada exclusivamente al **Almacén `01`**.
3. **Configuración del Escenario (`Q2_A5_2026`):**
   * En el **Paso 4 (*Inventory Data Source*)** del Asistente de MRP, la opción de ejecución (*Run By*) debe estar configurada en **Warehouse** (*Incluir inventario, demanda y suministro por separado para cada almacén*).

---

## 🚀 Pasos de Ejecución

1. Ingresar al módulo **MRP > MRP Wizard** y seleccionar el escenario `Q2_A5_2026`.
2. Verificar en el **Paso 2** que el horizonte de planificación comprenda del `26/10/2026` al `27/10/2026`.
3. Confirmar en el **Paso 3** que el criterio de selección filtre el artículo `A50009`.
4. En el **Paso 4 (*Inventory Data Source*)**:
   * Seleccionar el radio button **Warehouse**.
   * Marcar las casillas *Include Existing Inventory*, *Include Demand* e *Include Supply* **únicamente** para el **Almacén `01`** (dejando desmarcado el Almacén `02`).
5. En el **Paso 5 (*Documents Data Source*)**, incluir Órdenes de Venta y el Pronóstico `PSF1`, seleccionando generar recomendaciones hacia el almacén con la demanda (*Generate to Warehouse with the Demand*).
6. Hacer clic en **Run** para ejecutar el cálculo y revisar los resultados en el **Paso 6**.

---

## ✅ Resultado Esperado (Criterios de Aceptación)

* **En la pestaña *Report* (Paso 6):** El sistema debe mostrar un *Initial Inventory* de `0` para el Almacén `01`, ignorando las `50 unidades` almacenadas en el Almacén `02`. El balance proyectado debe reflejar un déficit de `-20 unidades`.
* **En la pestaña *Recommendations* (Paso 6):** El MRP debe generar una recomendación de **Orden de Compra** (*Purchase Order*) por `20 unidades` del artículo `A50009` dirigidas específicamente al **Almacén `01`** (o sugerir una Solicitud de Traslado desde el Almacén `02` si las reglas de reabastecimiento interno están activas).
* **Prueba de Contraste (Validación Negativa):** Si se repite la ejecución cambiando el parámetro a **Company** (Consolidado) e incluyendo ambos almacenes, el sistema deberá cubrir la demanda de `20 unidades` con el stock del Almacén `02` y **no** generar ninguna orden de compra externa.