#!/usr/bin/python3.13
"""Yazi Bulk Rename"""

import argparse


def get_args() -> tuple[int, int, str]:
    """Parse user arguments."""
    parser = argparse.ArgumentParser(description="Yazi bulk renamer.")
    parser.add_argument("-s",
                        "--start",
                        type=int,
                        default=1,
                        help="Start episode number (default: 1)")
    parser.add_argument("-e",
                        "--end",
                        type=int,
                        default=10,
                        help="End episode number (default: 10)")
    parser.add_argument("-t",
                        "--type",
                        type=str,
                        default="mp4",
                        help="File extension/type (default: mp4)")
    args = parser.parse_args()
    return args.start, args.end, args.type


def generate_episode_names(args: tuple[int, int, str]) -> str:
    """
    Generate episode names in the format
    01.mp4
    10.mp4
    11.mp4
    12.mp4
    02.mp4
    03.mp4
    04.mp4
    05.mp4
    06.mp4
    07.mp4
    08.mp4
    09.mp4
    $ ./yazi_bulk_rename.py -t mp4 -s 1 -e 12
    """
    seen: set[int] = set()
    episode_numbers: list[int] = list()
    for i in range(args[0], args[1] + 1):
        if i not in seen:
            seen.add(i)
            episode_numbers.append(i)
        j_start: int = max(i * 10, args[0])
        j_end: int = min(i * 10 + 10, args[1] + 1)
        for j in range(j_start, j_end):
            if j not in seen and args[0] <= j <= args[1]:
                seen.add(j)
                episode_numbers.append(j)
    return "\n".join(f"{num:02d}.{args[2]}" for num in episode_numbers)


def main() -> None:
    """Print new names for episodes."""
    print(generate_episode_names(get_args()))


if __name__ == "__main__":
    main()
