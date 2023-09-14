#!/usr/bin/python3

"""
A script that reads stdin line by by line and computes metrics
"""


def print_stat(myfile_size, status_code):
    """Print metrics of print_stat.
    Args:
        size (int): The read file size.
        status_codes (dict): The count of status codes.
    """
    print("File size: {}".format(myfile_size))
    for key in sorted(status_code):
        print("{}: {}".format(key, status_code[key]))


if __name__ == "__main__":
    import sys

    myfile_size = 0
    status_code = {}
    possible_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    num_count = 0

    try:
        for line in sys.stdin:
            if num_count == 10:
                print_stat(myfile_size, status_code)
                num_count = 1
            else:
                num_count += 1

            line = line.split()

            try:
                myfile_size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in possible_codes:
                    if status_code.get(line[-2], -1) == -1:
                        status_code[line[-2]] = 1
                    else:
                        status_code[line[-2]] += 1
            except IndexError:
                pass

        print_stat(myfile_size, status_code)

    except KeyboardInterrupt:
        print_stat(myfile_size, status_code)
        raise
