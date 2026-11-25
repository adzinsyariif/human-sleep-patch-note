"""Write the one-line patch note entry to /output/entry.txt."""

import os

ENTRY = "Fixed human sleep: you will now fall asleep instantly and stay asleep all night."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
