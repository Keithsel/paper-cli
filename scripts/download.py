import argparse

from papercli.cli import download


def main() -> None:
    parser = argparse.ArgumentParser(description="Download pending PDFs.")
    parser.add_argument("--venue", default=None, help="Limit to a specific venue")
    parser.add_argument("--year", default=None, help="Limit to a specific year")
    parser.add_argument(
        "--delay",
        type=float,
        default=0.5,
        help="Delay between requests in seconds",
    )
    args = parser.parse_args()

    venue = args.venue if args.venue else None
    year = int(args.year) if args.year else None

    download(venue=venue, year=year, delay=args.delay)


if __name__ == "__main__":
    main()
