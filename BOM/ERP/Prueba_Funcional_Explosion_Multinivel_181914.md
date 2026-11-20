# Prueba funcional PF-BOM-004 — Explosión multinivel de Lista de Materiales (BOM)

## Objetivo
Validar que el módulo BOM entregue correctamente la estructura multinivel y las necesidades **brutas** de componentes de un producto terminado, respetando cantidades base, versiones aprobadas y acumulación de materiales, para que el MRP pueda calcular posteriormente las necesidades netas con información de inventario.

> **Alcance:** esta prueba verifica la explosión y las cantidades brutas proporcionadas por BOM. El descuento de existencias, reservas y suministros en tránsito corresponde a la integración con inventarios/MRP y no se considera validado por esta prueba aislada.

## Identificación
- **ID:** PF-BOM-004
- **Módulo:** Bill of Materials (BOM)
- **Tipo:** Prueba funcional positiva, multinivel
- **Requerimientos:** RF03, RF05, RF07; reglas RN04, RN07 y RN08
- **Responsable:** Equipo BOM
- **Estado:** Pendiente de ejecución

## Precondiciones
1. Existen artículos activos MESA (fabricable), KIT (fabricable), TABLERO, PATA y TORNILLO (componentes de compra).
2. Las BOM de MESA y KIT están aprobadas y vigentes en la fecha de la demanda; no contienen ciclos.
3. La cantidad base de ambas BOM es **1 pieza**; todas las cantidades se expresan en piezas y no hay merma.
4. El usuario de planeación tiene permisos para consultar y explotar las BOM.
5. Se utiliza un ambiente de pruebas con datos controlados, sin modificar órdenes reales.

## Datos de prueba

| Nivel | Artículo padre | Componente | Cantidad por 1 padre | Tipo |
|---|---|---|---:|---|
| 0 → 1 | MESA | TABLERO | 1 | Materia prima |
| 0 → 1 | MESA | PATA | 4 | Materia prima |
| 0 → 1 | MESA | KIT | 1 | Subensamble |
| 1 → 2 | KIT | TORNILLO | 8 | Materia prima |

**Demanda:** 10 MESAS, con fecha dentro de la vigencia de ambas BOM.

## Procedimiento
1. Registrar o verificar los cinco artículos en el catálogo.
2. Crear y aprobar la BOM de KIT con 8 TORNILLOS por KIT.
3. Crear y aprobar la BOM de MESA con 1 TABLERO, 4 PATAS y 1 KIT por MESA.
4. Ingresar al módulo de planeación o al endpoint de explosión de BOM.
5. Solicitar la explosión de **10 MESAS** para la fecha de demanda indicada.
6. Consultar el árbol de componentes y el detalle de cantidades calculadas.
7. Verificar las versiones de BOM utilizadas en MESA y KIT.
8. Comparar los resultados con la tabla de resultados esperados y registrar evidencia.

## Resultados esperados

| Artículo | Cálculo | Necesidad bruta esperada |
|---|---|---:|
| TABLERO | 10 × 1 | **10 piezas** |
| PATA | 10 × 4 | **40 piezas** |
| KIT | 10 × 1 | **10 piezas (subensamble)** |
| TORNILLO | 10 × 1 × 8 | **80 piezas** |

- El sistema representa correctamente los niveles MESA → KIT → TORNILLO.
- KIT se identifica como subensamble y **no se suma como materia prima final** junto a sus TORNILLOS.
- Las necesidades brutas de los materiales hoja son 10 TABLEROS, 40 PATAS y 80 TORNILLOS.
- El cálculo emplea únicamente versiones aprobadas y vigentes en la fecha de demanda.
- No se duplican componentes ni se omiten niveles de la estructura.
- Si un material aparece en varias ramas, sus cantidades se acumulan antes del redondeo final.

## Criterios de aceptación
- **Aprobado:** todas las cantidades, niveles, tipos y versiones coinciden con los resultados esperados.
- **Fallido:** existe alguna diferencia de cantidad, omisión de un componente, duplicación indebida, selección de versión no vigente o interpretación incorrecta del subensamble.
- **Bloqueado:** faltan datos maestros, permisos o funcionalidades necesarias para ejecutar el flujo.

## Evidencia a registrar
- Captura o respuesta de API de las BOM aprobadas y sus versiones.
- Captura o respuesta de API de la demanda de 10 MESAS.
- Árbol de explosión y tabla de necesidades brutas resultantes.
- Fecha de ejecución, versión/commit del sistema, usuario de prueba, resultado observado y estado final.

## Registro de ejecución

| Campo | Valor |
|---|---|
| Fecha de ejecución | Pendiente |
| Ambiente y versión | Pendiente |
| Responsable | Equipo BOM |
| Resultado observado | Pendiente |
| Estado | **No ejecutada** |
| Evidencia | Pendiente |

## Referencia
Caso basado en la sección **PF03 Explosión multinivel** de `BOM/ERP/BOM requeriments.md` y en el escenario de explosión multinivel propuesto para el MRP.
