"""Write the one-line patch note entry to /output/entry.txt."""

import os

ENTRY = "v1.0.1: Fixed bug where brain reopened every embarrassing moment at 3am; sleep now stays closed until morning."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
