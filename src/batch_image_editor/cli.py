import argparse
from pathlib import Path

from .fsutils import ensure_directory, validate_input_folder
from .processing import ProcessingOptions, ResizeOptions, process_images


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
    parser.add_argument(
        "--width",
        type=int,
        help="Resize images to this width while keeping aspect ratio.",
    )
    parser.add_argument(
        "--height",
        type=int,
        help="Resize images to this height while keeping aspect ratio.",
    )
    parser.add_argument(
        "--no-keep-aspect",
        action="store_true",
        help="Resize without keeping the original aspect ratio.",
    )
    parser.add_argument(
        "--grayscale",
        action="store_true",
        help="Convert images to grayscale.",
    )
    parser.add_argument(
        "--format",
        choices=["JPEG", "PNG", "GIF", "BMP", "TIFF"],
        help="Convert images to a different format.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    input_root = validate_input_folder(
        Path(args.input).expanduser().resolve(),
    )
    output_root = ensure_directory(
        Path(args.output).expanduser().resolve(),
    )

    resize_opts: ResizeOptions | None = None
    if args.width or args.height:
        resize_opts = ResizeOptions(
            width=args.width,
            height=args.height,
            keep_aspect=not args.no_keep_aspect,
        )

    options = ProcessingOptions(
        resize=resize_opts,
        grayscale=args.grayscale,
        format=args.format,
    )

    processed = process_images(
        input_root=input_root,
        output_root=output_root,
        options=options,
        dry_run=args.dry_run,
    )

    if args.dry_run:
        for target in processed:
            print(target)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
