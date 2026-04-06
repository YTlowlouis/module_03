import sys


def mainn() -> None:
    scores = []
    count = 0
    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3",
              "ft_score_analytics.py <score1> <score2> ...")
        return

    for i in sys.argv:
        if count == 0:
            count = 1
        else:
            try:
                scores.append(int(i))
            except ValueError:
                print("Invalid input only numbers accepted")

    if not scores:
        print("No scores provided. "
              "Usage: python3 ft_score_analytics.py <score1> ...")
        return

    total: int = sum(scores)
    count: int = len(scores)
    avg: float = float(total / count)

    print(f"Scores processed: {scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {avg}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    mainn()
