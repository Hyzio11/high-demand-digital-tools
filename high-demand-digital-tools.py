"""CLI tool to list high-demand digital tools with the best ROI.

The script reads a CSV file where each row represents a digital tool with at least the
following columns (case‑insensitive):
    - name: the tool name
    - demand: numeric demand score (higher is better)
    - roi: numeric return‑on‑investment score (higher is better)

The tool outputs the top N entries sorted by ROI descending (and demand as a tie‑breaker).
Usage:
    python best_roi.py --file tools.csv --top 10
"""

import argparse
import csv
import sys
from collections import namedtuple
from operator import attrgetter

Tool = namedtuple("Tool", ["name", "demand", "roi"])


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Show high‑demand digital tools with the best ROI."
    )
    parser.add_argument(
        "--file",
        "-f",
        required=True,
        help="Path to a CSV file containing tool data.",
    )
    parser.add_argument(
        "--top",
        "-t",
        type=int,
        default=10,
        help="Number of top tools to display (default: 10).",
    )
    parser.add_argument(
        "--delimiter",
        "-d",
        default=",",
        help="CSV delimiter (default: ',').",
    )
    return parser.parse_args()


def read_tools(csv_path: str, delimiter: str) -> list[Tool]:
    tools = []
    try:
        with open(csv_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=delimiter)
            required_fields = {"name", "demand", "roi"}
            missing = required_fields - {field.lower() for field in reader.fieldnames}
            if missing:
                raise ValueError(
                    f"CSV file is missing required columns: {', '.join(sorted(missing))}"
                )
            for row in reader:
                try:
                    name = row["name"].strip()
                    demand = float(row["demand"])
                    roi = float(row["roi"])
                    tools.append(Tool(name=name, demand=demand, roi=roi))
                except (KeyError, ValueError) as e:
                    print(
                        f"Warning: Skipping malformed row {reader.line_num}: {e}",
                        file=sys.stderr,
                    )
    except FileNotFoundError:
        print(f"Error: File not found – '{csv_path}'", file=sys.stderr)
        sys.exit(1)
    except IOError as e:
        print(f"Error reading file '{csv_path}': {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        sys.exit(1)

    if not tools:
        print("Error: No valid tool entries found in the CSV file.", file=sys.stderr)
        sys.exit(1)

    return tools


def select_top_tools(tools: list[Tool], top_n: int) -> list[Tool]:
    # Sort by ROI descending, then demand descending
    sorted_tools = sorted(tools, key=attrgetter("roi", "demand"), reverse=True)
    return sorted_tools[:top_n]


def format_tool(tool: Tool) -> str:
    return f"{tool.name}: Demand={tool.demand}, ROI={tool.roi}"


def main() -> None:
    args = parse_arguments()
    if args.top <= 0:
        print("Error: --top must be a positive integer.", file=sys.stderr)
        sys.exit(1)

    tools = read_tools(args.file, args.delimiter)
    top_tools = select_top_tools(tools, args.top)

    print(f"Top {len(top_tools)} high‑demand tools by ROI:")
    for idx, tool in enumerate(top_tools, start=1):
        print(f"{idx}. {format_tool(tool)}")


if __name__ == "__main__":
    main()