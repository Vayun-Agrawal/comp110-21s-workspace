"""EX03 - palindromify function."""

__author__: str = "730358299"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", True))
    print(palindromify("han", False))
    print(palindromify("red", False))
    print(palindromify("live on time ", True))
    # Put print statements here to test your function
    # ex. print(palindromify("race", false))

def palindromify(x : str, y : bool) -> str:
    string: str = x
    xyz: str = ""
    if y == True:
        xy: int = len(string)
        while len(xyz) <= len(string):
            

    return string



if __name__ == "__main__":
    main()