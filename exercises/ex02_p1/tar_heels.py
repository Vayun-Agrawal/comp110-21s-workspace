"""Tar Heels exercise redux as a structured program."""

__author__ = "730358299"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    # TODO 2: Print the response of calling the tar_heels function here.
    print(tar_heels(choice))


# TODO 1: Define the tar_heels function, and its logic, here.
def tar_heels(x: int) -> str:
    """Tar Heel Function!"""
    if((x % 2) > 0):
        if((x % 7) > 0):
            return("CAROLINA")
        else:
            return("HEELS")
    else:
        if((x % 7) > 0):
            return("TAR")
        else:
            return("TAR HEELS")            


if __name__ == "__main__":
    main()