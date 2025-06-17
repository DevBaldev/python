#!/usr/bin/python3.13
"""Yazi Bulk Rename"""

import argparse


def main() -> None:
    """Print new names for episodes."""
    start, end, file_type = get_args()
    print(generate_episode_names(start, end, file_type))


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


def generate_episode_names(start: int, end: int, file_type: str) -> str:
    """Generate episode names in the format '01.mp4', '10.mp4', etc.,
       one per line."""
    seen: set[int] = set()
    episode_numbers: list[int] = []
    for i in range(start, end + 1):
        if i not in seen:
            seen.add(i)
            episode_numbers.append(i)
        j_start: int = i * 10
        j_end: int = j_start + 10
        for j in range(j_start, j_end):
            if j not in seen and start <= j <= end:
                seen.add(j)
                episode_numbers.append(j)
    return "\n".join(f"{num:02d}.{file_type}" for num in episode_numbers)


if __name__ == "__main__":
    main()
