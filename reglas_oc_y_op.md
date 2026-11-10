Documento de Requerimientos - MRP (Órdenes de Compra y Producción)

1. Definición de Requerimientos Funcionales
El sistema MRP debe gestionar los flujos de creación, seguimiento y cierre de Órdenes de Compra 
(OC) y Órdenes de Producción (OP). Flujo de Órdenes de Compra: Generación de OC por 
desabasto, aprobación, recepción de inventario y registro de proveedores. Flujo de Órdenes de 
Producción: Creación de OP, validación/reserva de componentes, ejecución y registro de producto 
terminado.

Datos y entidades requeridas:

• Materia Prima/Componente: ID Material, Descripción, Stock Físico, Stock Reservado, 
Punto de Reorden, Unidad de Medida.
• Producto Terminado: ID Producto, Descripción, Lista de Materiales (BOM).
• Orden de Compra (OC): ID OC, Proveedor, Fecha de Creación, Ítems (Materia Prima, 
Cantidad, Precio Unitario), Estado (Pendiente, Parcialmente Recibida, Recibida, Pagada).
• Orden de Producción (OP): ID OP, ID Producto Terminado, Cantidad a Fabricar, Ítems 
Consumidos (Materiales requeridos), Estado (Planeada, En Proceso, Completada, 
Cancelada).
2. Descripción de las Reglas de Negocio
Restricción de Inventario: El inventario físico de cualquier materia prima o producto terminado 
nunca puede ser negativo.

Validación de Pago: No se permite autorizar o realizar el pago de una Orden de Compra (o sus 
partidas) si los artículos correspondientes no han sido marcados como "Recibidos" en el sistema.

Reserva de Materiales: Una Orden de Producción solo puede pasar a estado "En Proceso" si existe 
stock físico suficiente para cubrir todos los componentes de su Lista de Materiales. Al pasar a "En 
Proceso", dicho stock se mueve a "Stock Reservado".

Generación de Demanda: El sistema debe sugerir una Orden de Compra cuando el inventario 
disponible (Stock Físico - Stock Reservado + Stock en Tránsito) caiga por debajo de su Punto de 
Reorden.

3. Integridad de los Datos
Atomicidad de transacciones: Al confirmar una recepción de OC, se debe actualizar el inventario 
físico y cambiar el estado de la OC en la misma transacción para evitar inconsistencias de datos. Lo 
mismo aplica al completar una OP.

Referencias Obligatorias: Toda OC debe tener asociado un ID de Proveedor activo; toda OP debe 
tener un BOM vigente.

Restricciones de Dominio: Los campos de "Cantidad", "Precio Unitario" y "Stock" deben aceptar 
únicamente valores numéricos mayores o iguales a cero.

Inmutabilidad de Documentos Cerrados: Una vez que una OP está "Completada" o una OC está 
"Pagada", sus líneas de detalle no pueden ser modificadas.

4. Pruebas Unitarias
test_inventario_no_negativo: Verificar que el método descontar_stock(id, cantidad) arroje una 
excepción si cantidad > stock_fisico.

test_validacion_pago_oc: Verificar que el método aprobar_pago_oc(id_oc) retorne un error si el 
estado de la OC es distinto a "Recibida".

test_calculo_reorden: Validar que la función requiere_compra(stock, punto_reorden) retorne 
Verdadero si stock < punto_reorden.

test_validar_tipos_datos: Insertar valores negativos en la función crear_linea_oc() y asegurar que 
el sistema devuelva un error.

test_consumo_forecast: Validar que si el Forecast es de 100 unidades y se reciben pedidos por 40 
unidades, la demanda bruta calculada siga siendo 100 (y no 140).

test_explosion_bom: Verificar que una propuesta de OP por 10 unidades de producto terminado 
multiplique correctamente las cantidades en el BOM para generar las propuestas de OC de 
materia prima correspondientes.

5. Pruebas Funcionales
• Flujo Completo de OP Exitoso: Crear una OP, validar que el sistema reserva los 
componentes. Completar la OP y verificar que el stock de materiales disminuye y el del 
producto terminado aumenta.
• Prevención de Producción sin Stock: Intentar iniciar una OP sin material suficiente. Validar 
que el sistema lanza el mensaje de error y no avanza la OP a estado "En Proceso".
• Recepción y Pago de OC: Crear una OC e intentar pagarla (validar rechazo). Registrar la 
recepción, verificar incremento de stock y volver a intentar el pago (validar éxito).
• Manejo de Transacciones Fallidas: Simular un fallo de sistema justo después de marcar 
una OC como "Recibida" pero antes de actualizar el stock, comprobando que se ejecuta un 
rollback manteniendo la integridad.
6. Roles, Permisos y Autorizaciones
• Comprador / Analista de Compras: Tiene permisos para crear, editar (solo en estado 
"Pendiente") y cancelar Órdenes de Compra. No tiene autorización para aprobar pagos ni 
modificar el inventario físico directamente.
• Planeador de Producción: Autorizado para crear Órdenes de Producción, asignarles el 
estado "Planeada" y liberar las órdenes a "En Proceso", lo cual detona la reserva de 
materiales. No puede modificar las Listas de Materiales (BOM).
• Almacenista / Recepcionista de Inventario: Único rol autorizado para confirmar la 
recepción física de mercancía de las OC (cambiando el estado a "Recibida") y para reportar 
la culminación de una OP (cambiando el estado a "Completada" y dando ingreso al 
producto terminado).
• Finanzas / Cuentas por Pagar: Tiene acceso de solo lectura a las OC y al inventario. Es el 
único rol con privilegios para cambiar el estado de una OC a "Pagada" una vez que el 
sistema valida la recepción de los artículos.
7. Gestión de Demanda y Pronósticos (Forecast)
• Ingreso de Pronósticos: El sistema debe permitir la carga de un pronóstico de ventas 
(Forecast) por producto terminado para un periodo de tiempo determinado (ej. semanal o 
mensual).
• Consumo de Pronóstico (Forecast Consumption): Los pedidos de venta reales (Órdenes de 
Cliente) ingresados en el sistema deben "consumir" el forecast del mismo periodo. La 
Demanda Bruta será el mayor valor entre el Forecast total y los Pedidos Reales, evitando 
así duplicar la necesidad de producción.
• Cálculo de Demanda Neta: El sistema debe calcular la Demanda Neta restando el 
inventario disponible actual de la Demanda Bruta.
• Explosión de Materiales (MRP): Si la Demanda Neta de un producto terminado es mayor a 
cero, el sistema debe detonar automáticamente una propuesta de Orden de Producción. 
Simultáneamente, debe realizar la "explosión" de la Lista de Materiales (BOM) para 
calcular la demanda dependiente de las materias primas.

```mermaid
flowchart TD
%% Definición de Carriles (Swimlanes) a través de subgrafos
subgraph Produccion [Planeación y Producción]
E_Inicio((Inicio: Ingreso de Demanda o Pronóstico))
T_AprobarProd[Revisar y Aprobar Órdenes de Producción]
E_Fin((Fin: Órdenes Liberadas para Ejecución))
end
subgraph Sistema [Sistema MRP]
T_Explosion[Ejecutar Explosión de Lista de Materiales - BOM]
T_Calculo[Evaluar Inventario y Requerimientos Netos]
G_Materiales{¿Se requiere material de proveedores?}
T_GenCompra[Generar Propuestas de Órdenes de Compra]
T_GenProd[Generar Propuestas de Órdenes de Producción]
end
subgraph Compras [Departamento de Compras]
T_AprobarCompra[Revisar y Autorizar Órdenes de Compra]
end
%% Flujo de Secuencia (Sequence Flow)
E_Inicio --> T_Explosion
T_Explosion --> T_Calculo
T_Calculo --> G_Materiales
%% Bifurcación (Compuerta)
G_Materiales -- Sí --> T_GenCompra
G_Materiales -- No --> T_GenProd
%% Interacciones interdepartamentales
T_GenCompra --> T_AprobarCompra
T_AprobarCompra --> T_GenProd
T_GenProd --> T_AprobarProd
T_AprobarProd --> E_Fin
%% Estilos visuales para cumplir con la notación estándar BPMN
classDef eventoInicio fill:#d4edda,stroke:#28a745,stroke-width:2px;
classDef eventoFin fill:#f8d7da,stroke:#dc3545,stroke-width:3px;
classDef compuerta fill:#fff3cd,stroke:#ffc107,stroke-width:2px,shape:diamond;
classDef tarea fill:#e2e3e5,stroke:#6c757d,stroke-width:1px,rx:5px,ry:5px;
class E_Inicio eventoInicio;
class E_Fin eventoFin;
class G_Materiales compuerta;
class T_AprobarProd,T_Explosion,T_Calculo,T_GenCompra,T_GenProd,T_AprobarCompra tarea;
