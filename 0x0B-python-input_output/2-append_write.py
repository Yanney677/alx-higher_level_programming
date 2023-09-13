#!/usr/bin/python3
"""A function that appends a string
at the end of a text file (UTF8) and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text
        file (UTF8) and returns the number of characters added
        Args:
            filename (str): name of the file
            text (str): text to write
        Returns:
            int: number of characters
    """
    with open(filename, "a", encoding="utf-8") as myFile:
        count = myFile.write(text)

    return count


if __name__ == "__main__":
    num_characters_append = append_write(
        "file_append.txt", "This School is so cool!\n")
    print(num_characters_append)
