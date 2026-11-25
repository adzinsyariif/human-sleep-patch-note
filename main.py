"""Write the one-line patch note entry to /output/entry.txt."""

import os

ENTRY = "Fixed: sleep() no longer reopens 47 tabs at 3am to replay that awkward thing you said in 2019; brain now closes all tabs at bedtime."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
