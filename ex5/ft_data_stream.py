import random
from typing import Generator

def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    actions = ["run", "eat", "sleep", "grab", "swim", "climb"]
    while True:
        # Yield a random tuple infinitely
        yield (random.choice(players), random.choice(actions))

def consume_event(event_list: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    # While the list still has items
    while event_list:
        # Pick a random index
        idx = random.randrange(len(event_list))
        # Pop it (removes and returns)
        yield event_list.pop(idx)

def main() -> None:
    print("=== Game Data Stream Processor ===")
    
    # 1. Initialize the infinite generator
    stream = gen_event()
    
    # 2. Display 1000 events
    for i in range(1000):
        player, action = next(stream)
        # Only print a few to match subject style or use [...]
        if i < 15 or i > 995:
            print(f"Event {i}: Player {player} did action {action}")
        elif i == 15:
            print("[...]")

    # 3. Build a fixed list of 10 events
    event_buffer = [next(stream) for _ in range(10)]
    print(f"\nBuilt list of 10 events: {event_buffer}")

    # 4. Consume the list randomly
    for event in consume_event(event_buffer):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_buffer}")

if __name__ == "__main__":
    main()
