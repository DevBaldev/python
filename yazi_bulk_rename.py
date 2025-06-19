#!/usr/bin/env python
"""Yazi Bulk Rename"""

import argparse


def get_args():
    """
    Parse command-line arguments for the bulk renamer.

    Returns:
        argparse.Namespace: Parsed arguments with attributes 'start', 'end', 'type'.
    """
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
    return parser.parse_args()


def generate_episode_names(start, end, ext):
    """
    Generate formatted episode names in a custom order.

    The function outputs episode filenames in the form:
        01.mp4
        10.mp4
        11.mp4
        ...
    according to a specific ordering logic.

    Args:
        start (int): The starting episode number (inclusive).
        end (int): The ending episode number (inclusive).
        ext (str): The file extension/type.

    Returns:
        str: Newline-separated string of episode filenames.
    """
    seen = set()
    order = []
    for i in range(start, end + 1):
        if i not in seen:
            seen.add(i)
            order.append(i)
        for j in range(max(i * 10, start), min(i * 10 + 10, end + 1)):
            if j not in seen:
                seen.add(j)
                order.append(j)
    return "\n".join(f"{n:02d}.{ext}" for n in order)


def main():
    """
    Main entry point for the script.

    Parses arguments and prints the generated episode names.
    """
    args = get_args()
    print(generate_episode_names(args.start, args.end, args.type))


if __name__ == "__main__":
    main()
