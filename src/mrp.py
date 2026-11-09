BOM = {
    "Gaming PC": {
        "CPU Ryzen 7": 1,
        "Motherboard B650": 1,
        "RAM 16GB DDR5": 2,
        "SSD 1TB NVMe": 1,
        "Power Supply 750W": 1,
        "Graphics Card RTX": 1
    }
}


def calculate_mrp(product, quantity):
    requirements = {}
    for material, qty in BOM[product].items():
        requirements[material] = qty * quantity
    return requirements
