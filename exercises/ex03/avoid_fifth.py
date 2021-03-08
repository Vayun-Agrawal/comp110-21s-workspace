"""EX03 - avoid_fifth function."""

__author__: str = "730358299"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello there"))
    print(avoid_fifth("The sentence we have here possesses E's galore! "))
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))

def avoid_fifth(x : str) -> str:
    "Remove E!"
    xyz: str = x 
    y: str = "" 
    for i in xyz:
        if i != "e":
            if i != "E":
                y = y + i
    return y

if __name__ == "__main__":
    main()