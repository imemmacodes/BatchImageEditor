from batch_image_editor.cli import build_parser


def test_parser_has_expected_flags():
    parser = build_parser()
    args = parser.parse_args(
        [
            "in",
            "out",
            "--width",
            "800",
            "--height",
            "600",
            "--no-keep-aspect",
            "--grayscale",
            "--format",
            "PNG",
            "--dry-run",
        ]
    )

    assert args.input == "in"
    assert args.output == "out"
    assert args.width == 800
    assert args.height == 600
    assert args.no_keep_aspect is True
    assert args.grayscale is True
    assert args.format == "PNG"
    assert args.dry_run is True

