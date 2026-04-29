
hotel = {
    "nombre": "Hotel MST",
    "numero_de_estrellas": 5,
    "habitaciones": [
        {
            "numero": 1,
            "piso": 1,
            "precio_por_noche": 40,
        },
        {
            "numero": 2,
            "piso": 1,
            "precio_por_noche": 60,
        },
        {
            "numero": 3,
            "piso": 2,
            "precio_por_noche": 40,
        },
        {
            "numero": 4,
            "piso": 2,
            "precio_por_noche": 60,
        },
    ]
}

print(hotel["habitaciones"][3]["precio_por_noche"])