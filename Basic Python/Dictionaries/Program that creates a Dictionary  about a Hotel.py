hotel = {
    "name": "Hotel MST",
    "number_of_stars": 5,
    "rooms": [
        {
            "number": 1,
            "floor": 1,
            "price_per_night": 40,
        },
        {
            "number": 2,
            "floor": 1,
            "price_per_night": 60,
        },
        {
            "number": 3,
            "floor": 2,
            "price_per_night": 40,
        },
        {
            "number": 4,
            "floor": 2,
            "price_per_night": 60,
        },
    ]
}

print(hotel["rooms"][3]["price_per_night"])