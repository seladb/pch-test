import shlex
import sys


def echo(phrase: str) -> None:
    """A dummy wrapper around print."""
    # for demonstration purposes, you can imagine that there is some
    # valuable and reusable logic inside this function
    print(phrase)


def echo2(phrase: str) -> None:
    print(f"{phrase} 2")


def main() -> int:
    """Echo the input arguments to standard output"""
    phrase = shlex.join(sys.argv)
    echo(phrase)
    echo2(phrase)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # next section explains the use of sys.exit
