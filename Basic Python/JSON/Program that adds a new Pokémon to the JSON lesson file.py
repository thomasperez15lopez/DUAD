import json

def read_pokemons(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found. Creating a new one...")
        return []


def add_new_pokemon(pokemons):
    while True:
        print("\nCurrent pokemons:")
        for p in pokemons:
            print(p['name']['english'])

        try:
            name = input("Enter pokemon name: ")
            level = int(input("Enter level : "))
            pokemon_type = input("Enter type: ")

            hp = int(input("HP: "))
            attack = int(input("Attack: "))
            defense = int(input("Defense: "))
            sp_attack = int(input("Sp. Attack: "))
            sp_defense = int(input("Sp. Defense: "))
            speed = int(input("Speed: "))

        except ValueError as e:
            print(f"Invalid number input, please try again. Details: {e}")
            continue

        except Exception as e:
            print(f"invalid input, please try again. Details: {e}")
            continue


        new_pokemon = {
            "name": {"english": name},
            "level": level,
            "type": [pokemon_type],
            "base": {
                "HP": hp,
                "Attack": attack,
                "Defense": defense,
                "Sp. Attack": sp_attack,
                "Sp. Defense": sp_defense,
                "Speed": speed
            }
        }

        pokemons.append(new_pokemon)

        print("\n Pokémon added successfully!")
        break

    return pokemons


def save_pokemons(path, pokemons):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(pokemons, file, indent=4)


def main():
    file_path = 'json file.json'

    pokemons = read_pokemons(file_path)

    updated_pokemons = add_new_pokemon(pokemons)

    save_pokemons(file_path, updated_pokemons)

    print("\n File updated successfully!")


if __name__ == "__main__":
    main()