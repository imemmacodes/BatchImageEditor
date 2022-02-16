import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="batch-image-editor",
        description="Apply simple batch edits to a folder of images.",
    )
    parser.add_argument(
        "input",
        help="Path to the input folder containing images.",
    )
    parser.add_argument(
        "output",
        help="Path to the output folder where edited images will be written.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show which files would be processed without writing anything.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    parser.parse_args(argv)
    # The actual editing logic will be implemented later.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

