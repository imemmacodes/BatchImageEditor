from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

from PIL import Image


SUPPORTED_SUFFIXES = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}


@dataclass
class ResizeOptions:
    width: int | None = None
    height: int | None = None
    keep_aspect: bool = True


@dataclass
class ProcessingOptions:
    resize: ResizeOptions | None = None
    grayscale: bool = False
    format: str | None = None


def iter_image_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() in SUPPORTED_SUFFIXES:
            yield path


def build_output_path(input_root: Path, output_root: Path, file_path: Path) -> Path:
    relative = file_path.relative_to(input_root)
    return output_root / relative


def apply_processing(
    image: Image.Image,
    options: ProcessingOptions,
) -> Image.Image:
    result = image

    if options.resize:
        result = _resize_image(result, options.resize)

    if options.grayscale:
        result = result.convert("L")

    return result


def _resize_image(image: Image.Image, opts: ResizeOptions) -> Image.Image:
    width, height = image.size

    target_w = opts.width or width
    target_h = opts.height or height

    if opts.keep_aspect:
        image.thumbnail((target_w, target_h))
        return image

    return image.resize((target_w, target_h))


def process_images(
    input_root: Path,
    output_root: Path,
    options: ProcessingOptions,
    dry_run: bool = False,
) -> list[Path]:
    processed: list[Path] = []

    for file_path in iter_image_files(input_root):
        destination = build_output_path(input_root, output_root, file_path)
        processed.append(destination)

        if dry_run:
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)

        with Image.open(file_path) as img:
            result = apply_processing(img, options)

            save_kwargs: dict[str, object] = {}
            save_format = options.format or img.format

            if save_format:
                save_kwargs["format"] = save_format

            result.save(destination, **save_kwargs)

    return processed

