import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    actions = ["run", "eat", "sleep", "grab", "swim", "climb"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(
        event_list: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while event_list:
        idx = random.randrange(len(event_list))
        yield event_list.pop(idx)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for i in range(1000):
        player, action = next(stream)
        if i < 15 or i > 995:
            print(f"Event {i}: Player {player} did action {action}")
        elif i == 15:
            print("[...]")

    event_buffer = [next(stream) for _ in range(10)]
    print(f"\nBuilt list of 10 events: {event_buffer}")

    for event in consume_event(event_buffer):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_buffer}")


if __name__ == "__main__":
    main()
