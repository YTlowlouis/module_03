import sys

def main() -> None:
    inventory: dict[str, int] = {}

    print("=== Inventory System Analysis ===")

    # 1. Parsing des arguments
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name, qty_str = arg.split(":", 1) # On split une seule fois

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            qty = int(qty_str)
            inventory[name] = qty
        except ValueError:
            print(f"Quantity error for '{name}': invalid literal for int()")

    if not inventory:
        return

    # 2. Affichages de base
    print(f"Got inventory: {inventory}")
    items_list = list(inventory.keys())
    print(f"Item list: {items_list}")

    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    # 3. Statistiques et Pourcentages
    for name, qty in inventory.items():
        percentage = (qty / total_qty) * 100
        print(f"Item {name} represents {percentage:.1f}%")

    # 4. Plus et Moins abondant
    # On utilise min/max avec une fonction de clé (key) pour plus d'élégance
    most_abundant = max(inventory, key=lambda k: inventory[k])
    least_abundant = min(inventory, key=lambda k: inventory[k])

    print(f"Item most abundant: {most_abundant} with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} with quantity {inventory[least_abundant]}")

    # 5. Mise à jour finale
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
    main()
