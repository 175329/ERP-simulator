# ERP MRP Demo

Proyecto académico para demostrar:

- GitHub Actions
- PostgreSQL
- MongoDB
- Neo4j
- MRP
- Pruebas Unitarias

## Empresa

TechAssembly S.A.

## Producto

Gaming PC

## Componentes

- CPU Ryzen 7
- Motherboard B650
- RAM 16GB DDR5
- SSD 1TB NVMe
- Power Supply 750W
- Graphics Card RTX

## Ejecutar

```bash
pytest
```

## Workflow

GitHub Actions levanta:

- PostgreSQL
- MongoDB
- Neo4j

y ejecuta automáticamente:

1. Espera servicios
2. Crea esquema ERP
3. Carga datos semilla
4. Ejecuta validación MRP
5. Ejecuta pruebas unitarias
```
