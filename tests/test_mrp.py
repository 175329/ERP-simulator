from src.mrp import calculate_mrp


def test_gaming_pc():
    result = calculate_mrp(
        "Gaming PC",
        30
    )
    assert result["CPU Ryzen 7"] == 30
    assert result["Motherboard B650"] == 30
    assert result["RAM 16GB DDR5"] == 60
    assert result["SSD 1TB NVMe"] == 30
    assert result["Power Supply 750W"] == 30
    assert result["Graphics Card RTX"] == 30
