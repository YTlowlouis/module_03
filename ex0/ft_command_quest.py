import sys


def main() -> None:
    total_count: int = len(sys.argv)
    script_name: str = sys.argv[0]

    print("=== Command Quest ===")
    print(f"Program name: {script_name}")

    if total_count == 1:
        print("No arguments provided!")
    else:
        args_received: int = total_count - 1
        print(f"Arguments received: {args_received}")

        for index, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {index}: {arg}")

    print(f"Total arguments: {total_count}")


if __name__ == "__main__":
    main()
