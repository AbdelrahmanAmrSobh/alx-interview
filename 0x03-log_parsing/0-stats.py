#!/usr/bin/python3
"""Module to get stats."""
import sys


def print_stats(stats, filesize):
    """Helper method that handles printing stats in required format."""
    stats = dict(sorted(stats.items(), key=lambda item: item[1], reverse=True))
    print(f"File size: {filesize}")
    for k, v in stats.items():
        if v == 0:
            break
        print(f"{k}: {v}")


if __name__ == "__main__":
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    total_size = 0
    line_count = 0
    for line in sys.stdin:
        line_count = line_count + 1
        status_code, file_size = line.split()[-2:]
        try:
            status_code, file_size = int(status_code), int(file_size)
        except TypeError:
            continue
        total_size = total_size + file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
        if line_count % 10 == 0:
            print_stats(status_codes, total_size)
    if line_count % 10 > 0:
        print_stats(status_codes, total_size)
