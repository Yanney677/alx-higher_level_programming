#!/usr/bin/python3
"""defines a text-indentation"""

def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
    text: string to be printed

    Raises:
    TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    n = 0
    while n < len(text) and text[n] == ' ':
        n += 1

    while n < len(text):
        print(text[n], end="")
        if text[n] == "\n" or text[i] in ".?:":
            if text[n] in ".?:":
                print("\n")
            n += 1
            while n < len(text) and text[n] == ' ':
                n += 1
            continue
        n += 1
