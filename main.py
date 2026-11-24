import os

ENTRY = "Senior Apologizer for Self-Driving Cars"
OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    write_entry()
