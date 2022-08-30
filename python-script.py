

import os


def read_file(filename):
    """Reads and returns the contents of a file in a list of strings"""
    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath(f"./data/{filename}", cur_path)
    f = open(new_path, "r", encoding="utf-8")
    lines = [i.strip() for i in f.readlines()]
    f.close()
    return lines


def main():
    """Main function"""
    raw_input = read_file("data.txt")
    for i in raw_input:
        print(i, end=" ")
    print()


if __name__ == "__main__":
    main()
