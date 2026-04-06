import random

def gen_player_achievements(master_list: list[str]) -> set[str]:
    count = random.randint(5, 8)
    return set(random.sample(master_list, count))

def main() -> None:
    master_list = [
        'Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme',
        'Untouchable', 'Boss Slayer', 'Strategist', 'Speed Runner', 'Survivor',
        'Treasure Hunter', 'First Steps', 'Sharp Mind', 'Hidden Path Finder'
    ]

    players = {
        "Alice": gen_player_achievements(master_list),
        "Bob": gen_player_achievements(master_list),
        "Charlie": gen_player_achievements(master_list),
        "Dylan": gen_player_achievements(master_list)
    }

    print("=== Achievement Tracker System ===")
    for name, achs in players.items():
        print(f"Player {name}: {achs}")

    all_distinct = set().union(*players.values())
    print(f"\nAll distinct achievements: {all_distinct}")

    common = set.intersection(*players.values())
    print(f"Common achievements: {common if common else 'set()'}")

    for name, current_set in players.items():
        others = set().union(*(s for n, s in players.items() if n != name))
        only_this = current_set - others
        print(f"Only {name} has: {only_this if only_this else 'set()'}")

    for name, current_set in players.items():
        missing = all_distinct - current_set
        print(f"{name} is missing: {missing}")

if __name__ == "__main__":
    main()
